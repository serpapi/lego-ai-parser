<h2 align="center">Contributions Guide</h2>

If you want to contribute to this project, you can open a pull request. You can also create an issue if you have any questions or suggestions.

- ### Reporting Issues or Feature Requests

All kinds of bug reports, suggestions, and feature requests are welcomed. Head to [Issues](https://github.com/kagermanov27/daath-ai-parser/issues) to keep track of the progress, or contribute to it.

- ### Adding a New Preset Parser

You can design a prompt in OpenAI Playground that creates a table such as this:
<img width="1467" alt="image" src="https://user-images.githubusercontent.com/73674035/205761436-9b8b8fa2-a284-4486-967c-e2609c119023.png">

And then you can turn it into a dictinary form as following example:

```py
# app/classify/parsers/google/google_local_results.py

from app.schemas import *

def commands():
  return json_to_pydantic({
    "main_prompt": "A table with NUMBER_OF_LABELS cells in each row summarizing the different parts of the text at each line:\n\n",
    "data": {
      "model": "text-davinci-003",
      "temperature": 0.001,
      "top_p": 0.9,
      "best_of": 2,
      "frequency_penalty": 0,
      "presence_penalty": 0
    },
    "model_specific_token_size": 3800,
    "openai_endpoint": "https://api.openai.com/v1/completions",
    "explicitly_excluded_strings": [
      "Order",
      "Website",
      "Directions",
      "\n"
    ],
    "examples_for_prompt": [
      {
        "text": "Houndstooth Coffee 4.6(824) · $$ · Coffee shop 401 Congress Ave. #100c · In Frost Bank Tower Closed ⋅ Opens 7AM Cozy hangout for carefully sourced brews",
        "classifications": {
          "line": "1",
          "title": "Houndstooth Coffee",
          "rating": "4.1",
          "number_of_reviews": "824",
          "expensiveness": "$$",
          "type": "Coffee Shop",
          "address": "401 Congress Ave. #100c · In Frost Bank Tower",
          "open_hours": "Opens 7AM",
          "description_or_review": "Cozy hangout for carefully sourced brews"
        }
      },
      # More examples ...
    ]
  })
```


- ### Unit Testing

You can add unit tests to your contribution easily with `mock_name`.

#### Write a unit test pointing to a mock name:

Point the results to `app/classify/tests/data/results` folder, or prompts to `app/classify/tests/data/prompts` folder, depending on whatever end result you are getting inside the unit test.

```py
# app/classify/tests/unit_tests/test_google_local_results.py
# ...
def test_google_local_results_successful_response():
  targets = [
    "app/classify/tests/data/targets/electronic-shops-successful.json"
  ]

  for target_filename in targets:
    with open(target_filename) as json_file:
      target = json.load(json_file)
    r = client.post("/classify", json=target)

    result_filename = target['mock_name'].replace('.json','-result.json')
    result_filename = result_filename.replace('/targets/', '/results/')

    with open(result_filename) as json_file:
      result = json.load(json_file)

    assert r.status_code == 200
    assert r.json() == result
    assert len(r.json()['results']) > 0
    assert ("message" not in r.json()['results'][0])
# ...
```


#### Create a json that contains the `mock_name` to call the localhost server:

`mock_name` should contain the path of the file itself.

```json
# app/classify/tests/data/targets/coffee-shops-successful.json
{
  "path": "google.google_local_results",
  "targets": [
    "<div jscontroller=\"AtSb\" class=\"w7Dbne\" data-record-click-time=\"false\" id=\"tsuid_25\" jsdata=\"zt2wNd;_;BvbRxs V6f1Id;_;BvbRxw\" jsaction=\"rcuQ6b:npT2md;e3EWke:kN9HDb\" data-hveid=\"CBUQAA\"><div jsname=\"jXK9ad\" class=\"uMdZh tIxNaf\" jsaction=\"mouseover:UI3Kjd\"><div class=\"VkpGBb\"><div class=\"cXedhc\"><a class=\"vwVdIc wzN8Ac rllt__link a-no-hover-decoration\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" tabindex=\"0\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEAE\"><div><div class=\"rllt__details\"><div class=\"dbg0pd\" aria-level=\"3\" role=\"heading\"><span class=\"OSrXXb\">Y Coffee</span></div><div><span class=\"Y0A0hc\"><span class=\"yi40Hd YrbPuc\" aria-hidden=\"true\">4.0</span><span class=\"z3HNkc\" aria-label=\"Rated 4.0 out of 5,\" role=\"img\"><span style=\"width:56px\"></span></span><span class=\"RDApEe YrbPuc\">(418)</span></span> · <span aria-label=\"Moderately expensive\" role=\"img\">€€</span> · Coffee shop</div><div>Nicosia</div><div class=\"pJ3Ci\"><span>Iconic Seattle-based coffeehouse chain</span></div></div></div></a><a class=\"uQ4NLd b9tNq wzN8Ac rllt__link a-no-hover-decoration\" aria-hidden=\"true\" tabindex=\"-1\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEA4\"><g-img class=\"gTrj3e\"><img id=\"pimg_3\" src=\"https://lh5.googleusercontent.com/p/AF1QipPaihclGQYWEJpMpBnBY8Nl8QWQVqZ6tF--MlwD=w184-h184-n-k-no\" class=\"YQ4gaf zr758c wA1Bge\" alt=\"\" data-atf=\"4\" data-frt=\"0\" width=\"92\" height=\"92\"></g-img></a></div></div></div></div>"
  ],
  "mock_name": "app/classify/tests/data/results/coffee-shops-successful.json"
}
```

#### Run the unit test using `pytest` once to generate json.

They will only be created in the initial call not to exhaust credits in testing. Here is an example result:

```json
# app/classify/tests/data/results/coffee-shops-successful-result.json
{
  "results": [
    {
        "Address": "Nicosia",
        "Description Or Review": "Iconic Seattle-based coffeehouse chain",
        "Expensiveness": "€€",
        "Number Of Reviews": "418",
        "Rating": "4.0",
        "Title": "Y Coffee",
        "Type": "Coffee shop"
    }
  ]
}
```
