import asyncio
import aiohttp
import re
from app.schemas import *

class Results:
  def __init__(self, targets = Targets, classifier = Classifier, prompt_objects = PromptObjects):
    self.targets = targets
    self.classifier = classifier
    self.prompt_objects = prompt_objects
    if targets.parse_only != None and targets.parse_only.responses != None:
      self.responses = targets.parse_only.responses
    else:
      self.responses = []

  def get_results_from_openai(self):
    async def call_openai(session, prompt):
      self.classifier.data.prompt = prompt + "\n"
      headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(self.targets.openai_key)
      }
      try:
        async with session.post(self.classifier.openai_endpoint, headers=headers, json=self.classifier.data.dict()) as resp:
          return await resp.json()
      except:
        return {"error": "Error from Local Machine"}
    
    async def get_results(concurrent_prompts):
      connector = aiohttp.TCPConnector(limit=None)
      async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for prompt in concurrent_prompts:
          tasks.append(asyncio.ensure_future(call_openai(session, prompt)))
        return await asyncio.gather(*tasks, return_exceptions=False)

    if self.targets.allowed_concurrency == 1:
      self.responses = asyncio.run(get_results(self.prompt_objects.prompts))
    else:
      all_prompt_calls = []
      remainder = len(self.prompt_objects.prompts) % self.targets.allowed_concurrency
      if remainder != 0 and remainder != len(self.prompt_objects.prompts):
        remainder_prompts = self.prompt_objects.prompts[(0 - remainder):]
        array_without_remainder = self.prompt_objects.prompts[0:(0 - remainder)]
        concurrent_prompts = []
        for prompt, i in zip(array_without_remainder, range(0, len(array_without_remainder))):
          concurrent_prompts.append(prompt)
          if i != 0 and self.targets.allowed_concurrency % i == 0:
            all_prompt_calls.append(concurrent_prompts)
            concurrent_prompts = []
        all_prompt_calls.append(remainder_prompts) # [[1,2],[3,4],[5]]
      else:
        array_without_remainder = self.prompt_objects.prompts
        concurrent_prompts = []
        if len(array_without_remainder) == 1:
          all_prompt_calls = [array_without_remainder]
        else:
          for prompt, i in zip(array_without_remainder, range(0, len(array_without_remainder))):
            concurrent_prompts.append(prompt)
            if i != 0 and self.targets.allowed_concurrency % i == 0:
              all_prompt_calls.append(concurrent_prompts)
              concurrent_prompts = []

      for concurrent_prompt_array in all_prompt_calls:
        self.responses = self.responses + asyncio.run(get_results(concurrent_prompt_array))

  def to_json(self):
    results = []
    index = 0
    for response in self.responses:
      if index in self.prompt_objects.invalid_lines_indexes:
        while index not in self.prompt_objects.invalid_lines_indexes:
          results.append({"error": "Maximum Token Size is reached for this prompt. This is skipped."})
          index = index + 1
      if 'error' in response:
        results.append({"error": response['error']})
      elif 'choices' in response:
        response = response['choices'][0]['text']
        lines = response.split("\n")
        lines = [line for line in lines if line != '']
        for line, line_index in zip(lines, range(0, len(lines))):
          result_dict = {}
          line = re.split(r" \| |\| | \|", line)
          line = [word for word in line if word != '']
          for i in range(len(line)):
            if "#$" in line[i]: # Array
              desired_array = []
              array = [word for word in line[i].split("#$") if word != '']
              for word in array:
                desired_line = self.prompt_objects.desired_lines[index + line_index]
                if word in desired_line:
                  desired_array.append(word.strip())
              if desired_array != []:
                result_dict[self.prompt_objects.labels[i]] = desired_array
            elif line[i] != "-" and self.prompt_objects.labels[i] != "Line": # String
              try:
                desired_line = self.prompt_objects.desired_lines[index + line_index]
                if line[i] in desired_line:
                  result_dict[self.prompt_objects.labels[i]] = line[i]
              except:
                result_dict = {"error": "The prompt is creating more results than expected. Try to restructure targets, and or examples."}
          results.append(result_dict)
        index = index + len(lines)
    
    if results == []:
      results = [{"error": "The model predicted a completion that begins with a stop sequence, resulting in no output. Consider adjusting your prompt or stop sequences."}]
    
    return results
