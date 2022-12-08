import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../../../.."))

from fastapi.testclient import TestClient
from app.schemas import *
from app.main import *
import json

client = TestClient(app)

def test_prompts_only():
  targets = [
    "app/classify/tests/data/targets/car-repair-parse-only.json"
  ]

  for target_filename in targets:
    with open(target_filename) as json_file:
      target = json.load(json_file)
    r = client.post("/classify", json=target)

    prompt_filename = target['mock_name'].replace('.json','-result.json')
    prompt_filename = prompt_filename.replace('/targets/', '/results/')
    with open(prompt_filename) as json_file:
      result = json.load(json_file)

    assert r.status_code == 200
    assert r.json() == result
    assert len(r.json()['results']) > 0
    assert ("message" not in r.json()['results'][0])