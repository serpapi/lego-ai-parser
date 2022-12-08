from pydantic import BaseModel
from typing import Union
from app.credentials import *

class TextDaVinci2DefaultData(BaseModel):
	prompt: str = None
	model: str = "text-davinci-002"
	temperature: Union[float, int] = 0.7
	max_tokens: int = 256
	top_p: Union[float, int] = 1
	frequency_penalty: Union[float, int] = 0
	presence_penalty: Union[float, int] = 0


class ClassifierExampleForPrompt(BaseModel):
  text: str
  classifications: dict


class Classifier(BaseModel):
  main_prompt: str = "A table with NUMBER_OF_LABELS cells in each row summarizing the different parts of the text:\n\n"
  data: BaseModel = TextDaVinci2DefaultData()
  model_specific_token_size: int = 4000
  openai_endpoint: str = "https://api.openai.com/v1/completions"
  explicitly_excluded_strings: list = ["\n"]
  examples_for_prompt: list = []

class PromptObjects(BaseModel):
	desired_lines: list = None
	invalid_lines_indexes: list = None
	valid_calls_token_sizes: list = None
	labels: list = None
	prompts: list = None

class ParseOnly(BaseModel):
	responses: list = None
	prompt_objects: PromptObjects = None

class Targets(BaseModel):
	path: str = "google.google_local_results"
	targets: list = None
	openai_key: str = OPENAI_KEY
	allowed_concurrency: int = ALLOWED_CONCURRENCY
	classifier: Classifier = None
	prompts_only: bool = False
	mock_name: str = None
	parse_only: ParseOnly = None


def json_to_pydantic(classifier_json):
	if "examples_for_prompt" in classifier_json:
		examples_for_prompt = []
		for example in classifier_json['examples_for_prompt']:
			try:
				examples_for_prompt.append(ClassifierExampleForPrompt(**example))
			except:
				return {"error": "Unknown Example Structure"}
	else:
		return {"error": "No examples provided for prompt"}
	
	if "data" in classifier_json:
		try:
			data = TextDaVinci2DefaultData(**classifier_json['data'])
		except:
			return {"error": "Unkown or Unsupported Model Data"}
	
	try:
		classifier_json.pop('examples_for_prompt')
		classifier_json.pop('data')
		classifier = Classifier(**classifier_json)
		classifier.data = data
		classifier.examples_for_prompt = examples_for_prompt
		return classifier
	except:
		return {"error": "A problem occured when reading the classifier dictionary"}