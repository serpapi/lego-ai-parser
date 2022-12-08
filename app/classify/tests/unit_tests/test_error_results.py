import sys, os
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/../../../.."))

from fastapi.testclient import TestClient
from app.schemas import *
from app.main import *
import json

client = TestClient(app)

def test_limitation_error():
  targets = [
    "app/classify/tests/data/targets/electronic-shops-limitation-error.json",
    "app/classify/tests/data/targets/electronic-shops-api-key-error.json",
    "app/classify/tests/data/targets/electronic-shops-server-error.json",
  ]

  error_codes = [
    "insufficient_quota",
    "invalid_request_error",
    "server_error",
  ]

  for target_filename, error in zip(targets, error_codes):
    with open(target_filename) as json_file:
      target = json.load(json_file)
    r = client.post("/classify", json=target)

    result_filename = target['mock_name'].replace('.json','-result.json')
    result_filename = result_filename.replace('/targets/', '/results/')
    with open(result_filename) as json_file:
      result = json.load(json_file)

    assert r.status_code == 200
    assert r.json() == result
    assert ("message" in r.json()['results'][0]["error"])
    assert (r.json()['results'][0]["error"]["type"] == error)



