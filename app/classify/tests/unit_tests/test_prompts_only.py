import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../../../.."))

from fastapi.testclient import TestClient
from app.schemas import *
from app.main import *
import json

client = TestClient(app)

def test_prompts_only():
  targets = [
    "app/classify/tests/data/targets/electronic-shops-successful-prompts-only.json"
  ]

  for target_filename in targets:
    with open(target_filename) as json_file:
      target = json.load(json_file)
    r = client.post("/classify", json=target)

    prompt_filename = target['mock_name'].replace('.json','-prompt.json')
    prompt_filename = prompt_filename.replace('/targets/', '/prompts/')
    with open(prompt_filename) as json_file:
      prompt = json.load(json_file)

    assert r.status_code == 200
    assert "prompts" in r.json()
    assert "prompt_objects" in r.json()
    assert r.json() == prompt