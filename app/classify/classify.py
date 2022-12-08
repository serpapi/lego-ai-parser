from app.classify.functions.parser import Parser
from app.classify.functions.prompt_creator import PromptCreator
from app.classify.functions.results import Results
from app.schemas import *
import importlib
import json
import os

class Classify:
	def classify(self, targets = Targets):
		if targets.mock_name != None and "PYTEST_CURRENT_TEST" not in os.environ:
			return {"error": "Mock name is only allowed in unit tests."}

		if targets.parse_only == None:
			# Create a new mock dictionary for target if given		
			if targets.mock_name != None and os.environ["PYTEST_CURRENT_TEST"] != None:
				try:
					with open(targets.mock_name) as json_file:
						targets_dict = json.load(json_file)
				except:
					targets_dict = targets.dict()
					if "openai_key" in targets_dict:
						targets_dict.pop('openai_key')
					if "save_locally" in targets_dict:
						targets_dict.pop('save_locally')
					if "save_name" in targets_dict:
						targets_dict.pop('save_name')
					with open(targets.mock_name, "w") as pretty_json:
						json.dump(targets_dict, pretty_json, indent=2, sort_keys=False)
				targets = Targets(**targets_dict)

			# Call the parser command dictionary or return an error
			if targets.classifier != None and targets.parse_only == False:
				classifier = json_to_pydantic(targets.classifier.dict())
			else:
				try:
					parser = targets.path
					path = "app.classify.parsers.{}".format(parser.lower())
					classifier = importlib.import_module(path)
					classifier = classifier.commands()
					if type(classifier) == dict:
						return classifier
				except:
					return {"error": "Could not find parser classifier commands"}
			
			# Parse the incoming body whether it is html, text, or a mixbag of them
			parser = Parser(classifier = classifier)
			desired_lines = parser.parse(targets.targets)

			# Create a prompt, get maximum response token size, get estimated maximum token size
			prompt_objects = PromptObjects(desired_lines = desired_lines)
			prompt_creator = PromptCreator(classifier = classifier, prompt_objects = prompt_objects)
			classifier, prompt_objects = prompt_creator.get_prompts()

			# Return an error if all bodies are illegal
			if prompt_objects.prompts == []:
				return {"error": "None of the items are below maximum token threshold for this prompt."}
			
			# Return mock prompt results, or create a new one, or return prompt results
			if targets.prompts_only == True and targets.mock_name != None and os.environ["PYTEST_CURRENT_TEST"] != None:
				mock_prompt_name = targets.mock_name.replace(".json", "-prompt.json")
				mock_prompt_name = mock_prompt_name.replace("/targets/", "/prompts/")
				try:
					with open(mock_prompt_name) as json_file:
						prompt = json.load(json_file)
					return prompt
				except:
					prompts_only_dict = {
										"prompts": prompt_objects.prompts,
										"prompt_objects": {
											"invalid_lines_indexes": prompt_objects.invalid_lines_indexes,
											"desired_lines": prompt_objects.desired_lines,
											"labels": prompt_objects.labels
										}
									}
					with open(mock_prompt_name, "w") as pretty_json:
						json.dump(prompts_only_dict, pretty_json, indent=2, sort_keys=False)
					return prompts_only_dict
			elif targets.prompts_only == True:
				return {
									"prompts": prompt_objects.prompts,
									"prompt_objects": {
										"invalid_lines_indexes": prompt_objects.invalid_lines_indexes,
										"desired_lines": prompt_objects.desired_lines,
										"labels": prompt_objects.labels
									}
								}

		# Return mock classified results, or create a new one
		if targets.mock_name != None and os.environ["PYTEST_CURRENT_TEST"] != None:
			mock_result_name = targets.mock_name.replace(".json", "-result.json")
			mock_result_name = mock_result_name.replace("/targets/", "/results/")
			try:
				with open(mock_result_name) as json_file:
					result = json.load(json_file)
				return result
			except:
				if targets.parse_only != None:
					results = Results(targets = targets, classifier = None, prompt_objects = targets.parse_only.prompt_objects)
					results_to_write = results.to_json()
				else:
					results = Results(targets = targets, classifier = classifier, prompt_objects = prompt_objects)
					results.get_results_from_openai()
					results_to_write = results.to_json()
				with open(mock_result_name, "w") as pretty_json:
					json.dump({"results": results_to_write}, pretty_json, indent=2, sort_keys=False)
				return {"results": results_to_write}
		
		# Return classified results
		if targets.parse_only != None:
			results = Results(targets = targets, classifier = None, prompt_objects = targets.parse_only.prompt_objects)
			results_from_parsing = results.to_json()
			return {"results": results_from_parsing}
		else:
			results = Results(targets = targets, classifier = classifier, prompt_objects = prompt_objects)
			results.get_results_from_openai()
			results_from_openai = results.to_json()
			return {"results": results_from_openai}