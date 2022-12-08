import re
from app.schemas import *
from transformers import GPT2TokenizerFast

tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

class PromptCreator:
  def __init__(self, classifier = Classifier, prompt_objects = PromptObjects):
    self.classifier = classifier
    self.prompt_objects = prompt_objects
    self.keys = []
    self.number_of_labels = 0
    self.example_rows = []
    self.base_prompt_token_size = 0
    self.model_specific_token_size = classifier.model_specific_token_size

  def get_data_from_examples(self):
    for example in self.classifier.examples_for_prompt:
      [self.keys.append(key) for key in sorted(list(example.classifications.keys())) if key not in self.keys]
    self.prompt_objects.labels = [re.sub("_", " ", key.title()) for key in self.keys]
    self.number_of_labels = len(self.prompt_objects.labels)

  def get_main_prompt(self):
    return re.sub("NUMBER_OF_LABELS", "{}".format(self.number_of_labels), self.classifier.main_prompt)

  def get_example_lines(self):
    return "\n".join([example.text for example in self.classifier.examples_for_prompt])

  def get_desired_lines(self, lines):
    desired_lines_string = "\n" + "\n".join(lines) + "\n"
    return desired_lines_string
  
  def get_table_labels(self):
    table_labels_string = "|" + "".join(([" {} |".format(label) for label in self.prompt_objects.labels ])) + "\n"
    return table_labels_string

  def get_table_separator(self):
    table_separator_string = "|" + "".join([" --- |" for i in self.prompt_objects.labels]) + "\n"
    return table_separator_string

  def get_example_rows(self):
    for example in self.classifier.examples_for_prompt:
      row_text = "|"
      for key in self.keys:
        if key in example.classifications:
          row_text = row_text + " {} |".format(example.classifications[key])
        else:
          row_text = row_text + " - |"
      row_text = row_text + "\n"
      self.example_rows.append(row_text)
    self.example_rows = "".join(self.example_rows)
    self.example_rows = self.example_rows[0:-1]
    return self.example_rows

  def calculate_token_size(self, line):
    tokenized = tokenizer(line)['input_ids']
    return len(tokenized)

  def get_maximum_token_size(self, previous_max_token_size, line):
    token_size = self.number_of_labels + (2 * self.calculate_token_size(line)) + 2 # abc\n|1|abc|-|-|\n
    return previous_max_token_size + token_size

  def separate_for_calls(self):
    token_sizes_of_lines = [(5 + self.calculate_token_size(line)) for line in self.prompt_objects.desired_lines]
    
    invalid_lines_indexes = []
    valid_calls = []
    valid_call = []
    previous_max_token_size = 0
    for size, line, i in zip(token_sizes_of_lines, self.prompt_objects.desired_lines, range(0, len(token_sizes_of_lines))):
      previous_max_token_size = self.get_maximum_token_size(previous_max_token_size, line)
      if (self.base_prompt_token_size + size) > self.model_specific_token_size:
        invalid_lines_indexes.append(i)
      elif (self.base_prompt_token_size + previous_max_token_size) > self.model_specific_token_size:
        valid_call.append(line)
      elif (self.base_prompt_token_size + previous_max_token_size) < self.model_specific_token_size:
        previous_max_token_size = 0
        valid_calls.append(valid_call)
        valid_call = []
      elif i == len(token_sizes_of_lines) - 1:
        valid_calls.append(valid_call)

    self.prompt_objects.invalid_lines_indexes = invalid_lines_indexes

    return valid_calls

  def get_prompts(self):
    self.get_data_from_examples()
    main_prompt_string = self.get_main_prompt()
    example_lines_string = self.get_example_lines()
    desired_lines_string = self.get_desired_lines(self.prompt_objects.desired_lines)
    table_labels_string = self.get_table_labels()
    table_separator_string = self.get_table_separator()
    example_rows = self.get_example_rows()
    
    prompt = "".join([
      main_prompt_string,
      example_lines_string,
      desired_lines_string,
      table_labels_string,
      table_separator_string,
      example_rows
    ])
    
    max_tokens_size = self.get_maximum_token_size(0, prompt)
    total_estimated_token_size = self.calculate_token_size(prompt) + max_tokens_size

    if total_estimated_token_size > self.model_specific_token_size:
      base_prompt = "".join([
        main_prompt_string,
        example_lines_string,
        table_labels_string,
        table_separator_string,
        example_rows
      ])
      self.base_prompt_token_size = self.calculate_token_size(base_prompt)
      valid_calls = self.separate_for_calls()

      if valid_calls == []:
        self.prompt_objects.prompts = []
      else:
        for i in range(0,len(valid_calls)):
          desired_lines_string = self.get_desired_lines(valid_calls[i])
          valid_calls[i] = "".join([
            main_prompt_string,
            example_lines_string,
            desired_lines_string,
            table_labels_string,
            table_separator_string,
            example_rows
          ])
        self.prompt_objects.prompts = valid_calls
    else:
      self.prompt_objects.prompts = [prompt]
      self.prompt_objects.invalid_lines_indexes = []

    return self.classifier, self.prompt_objects