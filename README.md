<h1 align="center">Daath AI Parser</h1>


[![Build status][Build-shield]][Build-url] 
[![Contributors][contributors-shield]][contributors-url] 
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![Issues][issuesclosed-shield]][issuesclosed-url]
[![MIT License][license-shield]][license-url]
[![Server Status][server-shield]][server-url]
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)


<p align="center">
  <img src="https://user-images.githubusercontent.com/73674035/205769347-bc9327b4-e35d-4f42-9716-9de21b54e889.jpg" alt="The Fool of Daath"/>
</p>

<p align="center">
  Daath AI Parser is an open-source application that uses OpenAI to parse visible text of HTML elements. It is built on top of FastAPI. It is ready to set up as a server, and make calls from any language. It is currently hosted in <a href="https://ai.kagermanov.com">ai.kagermanov.com</a>.
<br>
<br>
<a href="https://replit.com/@EmirhanAkdeniz1/Example-with-one-element#main.py">Interactive Example on Replit</a>
<br>
</p>

|Currently Supported Preset Parsers||||
|-|-|-|-|
|Google Local Results Parser|Amazon Listings Parser|Etsy Listings Parser|Wayfair Listings Parser|
|BestBuy Listings Parser|Costco Listings Parser|Macy's Listings Parser|Nordstrom Listings Parser|

---

<h2 align="center">Table of Contents</h2>

- [Daath AI Parser](#daath-ai-parser)
  * [Basic Usage](#basic-usage)
  * [Parsing Multiple Elements](#parsing-multiple-elements)
  * [Designing Custom Parsers](#designing-custom-parsers)
  * [Making Server-Side Calls without exposing API Key](#making-server-side-calls-without-exposing-api-key)
    + [Prompts Only Call](#prompts-only-call)
    + [Making Server-Side Calls to OpenAI](#making-server-side-calls-to-openai)
    + [Parse Only Call](#parse-only-call)
  * [Expected Error Responses](#expected-error-responses)
  * [Customizing Default Allowed Concurrency and API Key of Cliend-Side Calls](#customizing-default-allowed-concurrency-and-api-key-of-cliend-side-calls)
  * [Contributions Guide](#contributions-guide)
    + [Adding a New Preset Parser](#adding-a-new-preset-parser)
    + [Unit Testing](#unit-testing)

---

<h2 align="center">Basic Usage</h2>

- ### Copy the Outer HTML of the element you want to parse

<img width="1463" alt="image" src="https://i.imgur.com/8Ql6M4i.gif">

- ### Use the path for the preset parser

You can find the supported preset parsers and their fields at [Daath Preset Parsers Page](https://www.kagermanov.com/daath-preset-parsers)

- ### Use your OpenAI API Key

You need to [register a free account](https://beta.openai.com/signup) first. You may find your API Key [here](https://beta.openai.com/account/api-keys).
<img width="667" alt="image" src="https://user-images.githubusercontent.com/73674035/205708634-cd524db9-50ac-44a6-8b38-a7186857648f.png">

- ### Make a POST request to the endpoint

```py
import requests

uri = "https://ai.kagermanov.com/classify"

headers = {"Content-Type": "application/json"}

data = {
  "path": "google.google_local_results",
  "targets": [
    "<div jscontroller=\"AtSb\" class=\"w7Dbne\" data-record-click-time=\"false\" id=\"tsuid_25\" jsdata=\"zt2wNd;_;BvbRxs V6f1Id;_;BvbRxw\" jsaction=\"rcuQ6b:npT2md;e3EWke:kN9HDb\" data-hveid=\"CBUQAA\"><div jsname=\"jXK9ad\" class=\"uMdZh tIxNaf\" jsaction=\"mouseover:UI3Kjd\"><div class=\"VkpGBb\"><div class=\"cXedhc\"><a class=\"vwVdIc wzN8Ac rllt__link a-no-hover-decoration\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" tabindex=\"0\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEAE\"><div><div class=\"rllt__details\"><div class=\"dbg0pd\" aria-level=\"3\" role=\"heading\"><span class=\"OSrXXb\">Y Coffee</span></div><div><span class=\"Y0A0hc\"><span class=\"yi40Hd YrbPuc\" aria-hidden=\"true\">4.0</span><span class=\"z3HNkc\" aria-label=\"Rated 4.0 out of 5,\" role=\"img\"><span style=\"width:56px\"></span></span><span class=\"RDApEe YrbPuc\">(418)</span></span> · <span aria-label=\"Moderately expensive\" role=\"img\">€€</span> · Coffee shop</div><div>Nicosia</div><div class=\"pJ3Ci\"><span>Iconic Seattle-based coffeehouse chain</span></div></div></div></a><a class=\"uQ4NLd b9tNq wzN8Ac rllt__link a-no-hover-decoration\" aria-hidden=\"true\" tabindex=\"-1\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEA4\"><g-img class=\"gTrj3e\"><img id=\"pimg_3\" src=\"https://lh5.googleusercontent.com/p/AF1QipPaihclGQYWEJpMpBnBY8Nl8QWQVqZ6tF--MlwD=w184-h184-n-k-no\" class=\"YQ4gaf zr758c wA1Bge\" alt=\"\" data-atf=\"4\" data-frt=\"0\" width=\"92\" height=\"92\"></g-img></a></div></div></div></div>"
  ],
  "openai_key": "<OPENAI KEY>"
}

r = requests.post(url=uri, headers=headers, json=data)

print(r.json()["results"])
```

- ### Result:

<img width="851" alt="image" src="https://user-images.githubusercontent.com/73674035/205724193-917feb92-3054-436d-93e9-552f8ec7ca9b.png">


```json
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

These instructions are for basic usage. Sharing API Keys with third-party applications is not recommended. It is recommended that you set up your own server, or use a throwaway API key to check out this fuctionality. Making the calls on server-side without sharing credentials are explained in the next sections.

---

<h2 align="center">Parsing Multiple Elements</h2>

In addition to using HTML of the element, using text you copy from the element is also accepted. You can pass a mixbag of HTML and Text in the same list. If all the elements exceed the token size of the model, `Daath AI Parser` will separate the prompts for you and return the results in the same order. Please note that duplicate items will result in bad parsing.

```py
import requests

uri = "https://ai.kagermanov.com/classify"

headers = {"Content-Type": "application/json"}

data = {
  "path": "google.google_local_results",
  "targets": [
    "X Coffee 4.1(23) · €€ · Coffee shop Nicosia Counter-serve chain for coffee & snacks",
    "<div jscontroller=\"AtSb\" class=\"w7Dbne\" data-record-click-time=\"false\" id=\"tsuid_25\" jsdata=\"zt2wNd;_;BvbRxs V6f1Id;_;BvbRxw\" jsaction=\"rcuQ6b:npT2md;e3EWke:kN9HDb\" data-hveid=\"CBUQAA\"><div jsname=\"jXK9ad\" class=\"uMdZh tIxNaf\" jsaction=\"mouseover:UI3Kjd\"><div class=\"VkpGBb\"><div class=\"cXedhc\"><a class=\"vwVdIc wzN8Ac rllt__link a-no-hover-decoration\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" tabindex=\"0\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEAE\"><div><div class=\"rllt__details\"><div class=\"dbg0pd\" aria-level=\"3\" role=\"heading\"><span class=\"OSrXXb\">Y Coffee</span></div><div><span class=\"Y0A0hc\"><span class=\"yi40Hd YrbPuc\" aria-hidden=\"true\">4.0</span><span class=\"z3HNkc\" aria-label=\"Rated 4.0 out of 5,\" role=\"img\"><span style=\"width:56px\"></span></span><span class=\"RDApEe YrbPuc\">(418)</span></span> · <span aria-label=\"Moderately expensive\" role=\"img\">€€</span> · Coffee shop</div><div>Nicosia</div><div class=\"pJ3Ci\"><span>Iconic Seattle-based coffeehouse chain</span></div></div></div></a><a class=\"uQ4NLd b9tNq wzN8Ac rllt__link a-no-hover-decoration\" aria-hidden=\"true\" tabindex=\"-1\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEA4\"><g-img class=\"gTrj3e\"><img id=\"pimg_3\" src=\"https://lh5.googleusercontent.com/p/AF1QipPaihclGQYWEJpMpBnBY8Nl8QWQVqZ6tF--MlwD=w184-h184-n-k-no\" class=\"YQ4gaf zr758c wA1Bge\" alt=\"\" data-atf=\"4\" data-frt=\"0\" width=\"92\" height=\"92\"></g-img></a></div></div></div></div>",
    # Some other elements in between ...
    "Z Coffee 4.6(13) · € · Cafe Nicosia Takeaway"
  ],
  "openai_key": "<OPENAI KEY>"
}

r = requests.post(url=uri, headers=headers, json=data)

print(r.json()["results"])
```

- ### Multiple Results

```json
{
    "results": [
      {
          "Address": "Nicosia",
          "Description Or Review": "Counter-serve chain for coffee & snacks",
          "Expensiveness": "€€",
          "Number Of Reviews": "23",
          "Rating": "4.1",
          "Title": "X Coffee",
          "Type": "Coffee shop"
      },
      {
          "Address": "Nicosia",
          "Description Or Review": "Iconic Seattle-based coffeehouse chain",
          "Expensiveness": "€€",
          "Number Of Reviews": "418",
          "Rating": "4.0",
          "Title": "Y Coffee",
          "Type": "Coffee shop"
      },
      # Some Other Results in between ...
      {
          "Address": "Nicosia",
          "Description Or Review": "Takeaway",
          "Expensiveness": "€",
          "Number Of Reviews": "13",
          "Rating": "4.6",
          "Title": "Z Coffee",
          "Type": "Cafe"
      }
    ]
}
```

---

<h2 align="center">Designing Custom Parsers</h2>

In addition to preset parsers, designing your own parsers are also allowed in `Daath AI Parser`. All that is needed is to provide a `prompt`, `examples`, and `details about the OpenAI model` under `classifier` key. Here is a breakdown of such custom parser:

```json
{
  "classifier": {
    "main_prompt": "String, A prompt commanding the model to classify each item you desire. `NUMBER_OF_LABELS` is used to automatically determine the size of all unique labels in each example by `Daath AI Parser`."
    "data": "Dictionary, Details of the model you want to employ. Same data field you would use in a normal OpenAI API call, excluding `max_tokens`",
    "model_specific_token_size": "Integer, The maximum number of tokens allowed for the model. This is used to determine where to split multiple prompt calls in a given command. It is wise to set it just below the maximum number of tokens allowed by the model. For example, if the model allows 4000 tokens, you can set it to 3800. This is because the token count made by `Daath AI Parser` is determined by GPT-2 standards, and it might be higher than the actual token count of the model.",
    "openai_endpoint": "String, Endpoint you want to call the model from. For example: `https://api.openai.com/v1/completions`",
    "explicitly_excluded_strings": "List, A list of strings that you want to exclude from the results. For example, if you want to exclude new lines, you may add \"\n\" to the list.",
    "examples_for_prompt": [
      {
        "text": "String, The text you want to classify.",
        "classifications": {
          "label_1": "String, The value of the label_1 for the given text.",
          "label_2": "String, The value of the label_2 for the given text.",
          # More Labels
        }
      },
      # More examples
    ]
  }
}
```

Here is an example script with a Custom Parser:

```py
import requests

uri = "https://ai.kagermanov.com/classify"

headers = {"Content-Type": "application/json"}

data = {
  "targets": [
    "<div jscontroller=\"AtSb\" class=\"w7Dbne\" data-record-click-time=\"false\" id=\"tsuid_25\" jsdata=\"zt2wNd;_;BvbRxs V6f1Id;_;BvbRxw\" jsaction=\"rcuQ6b:npT2md;e3EWke:kN9HDb\" data-hveid=\"CBUQAA\"><div jsname=\"jXK9ad\" class=\"uMdZh tIxNaf\" jsaction=\"mouseover:UI3Kjd\"><div class=\"VkpGBb\"><div class=\"cXedhc\"><a class=\"vwVdIc wzN8Ac rllt__link a-no-hover-decoration\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" tabindex=\"0\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEAE\"><div><div class=\"rllt__details\"><div class=\"dbg0pd\" aria-level=\"3\" role=\"heading\"><span class=\"OSrXXb\">Y Coffee</span></div><div><span class=\"Y0A0hc\"><span class=\"yi40Hd YrbPuc\" aria-hidden=\"true\">4.0</span><span class=\"z3HNkc\" aria-label=\"Rated 4.0 out of 5,\" role=\"img\"><span style=\"width:56px\"></span></span><span class=\"RDApEe YrbPuc\">(418)</span></span> · <span aria-label=\"Moderately expensive\" role=\"img\">€€</span> · Coffee shop</div><div>Nicosia</div><div class=\"pJ3Ci\"><span>Iconic Seattle-based coffeehouse chain</span></div></div></div></a><a class=\"uQ4NLd b9tNq wzN8Ac rllt__link a-no-hover-decoration\" aria-hidden=\"true\" tabindex=\"-1\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEA4\"><g-img class=\"gTrj3e\"><img id=\"pimg_3\" src=\"https://lh5.googleusercontent.com/p/AF1QipPaihclGQYWEJpMpBnBY8Nl8QWQVqZ6tF--MlwD=w184-h184-n-k-no\" class=\"YQ4gaf zr758c wA1Bge\" alt=\"\" data-atf=\"4\" data-frt=\"0\" width=\"92\" height=\"92\"></g-img></a></div></div></div></div>"
  ],
  "openai_key": "<OPENAI KEY>",
  "classifier": {
    "main_prompt": "A table with NUMBER_OF_LABELS cells in each row summarizing the different parts of the text at each line even if they are not unique:\n\n",
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
  }
}

r = requests.post(url=uri, headers=headers, json=data)

print(r.json()["results"])
```

Custom Parser Result will be the same as the preset one:

```json
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

You may also get arrays from your prompts by separating your results with a special double character, `#$`. Here is an representation of such utility in `product_options` key proivded in the example below:

```json
{
  # ...
  "examples_for_prompt": [
    {
      "text": "Stumptown Coffee Roasters, Medium Roast Organic Whole Bean Coffee Gifts - Holler Mountain 12 Ounce Bag with Flavor Notes of Citrus Zest, Caramel and Hazelnut 12 Ounce 4.3 4.3 out of 5 stars (8,311) Options: 2 sizes, 6 flavors 2 sizes, 6 flavors Climate Pledge Friendly uses sustainability certifications to highlight products that support our commitment to help preserve the natural world. Time is fleeting. Learn more Product Certification (1) USDA Organic",
      "classifications": {
        "line": "3",
        "title": "Stumptown Coffee Roasters, Medium Roast Organic Whole Bean Coffee Gifts - Holler Mountain 12 Ounce Bag with Flavor Notes of Citrus Zest, Caramel and Hazelnut",
        "scale": "12 Ounce",
        "rating": "4.3",
        "reviews": "8,311",
        "product_options": "2 sizes#$6 flavors#$",
        "tags": "Climate Pledge Friendly#$USDA Organic#$"
      }
    },
    #...
  ]
  #...
}
```

Constructing a custom parser with such example will result in the following structure:

```json
{
  "results": [
    {
      "Line": "X",
      "Product Options": [
        "X",
        "X"
      ],
      "Rating": "X",
      "Reviews": "X",
      "Scale": "X",
      "Tags": [
        "X",
        "X"
      ],
      "Title": "X"
    }
  ]
}
```

---

<h2 align="center">Making Server-Side Calls without exposing API Key</h2>


- ### Prompts Only Call
You can get only the prompts you need to call the OpenAI endpoint with `prompts_only` key.

```py
import requests

uri = "https://ai.kagermanov.com/classify"

headers = {"Content-Type": "application/json"}

data = {
  "prompts_only": True,
  "path": "google.google_local_results",
  "targets": [
    "<div jscontroller=\"AtSb\" class=\"w7Dbne\" data-record-click-time=\"false\" id=\"tsuid_25\" jsdata=\"zt2wNd;_;BvbRxs V6f1Id;_;BvbRxw\" jsaction=\"rcuQ6b:npT2md;e3EWke:kN9HDb\" data-hveid=\"CBUQAA\"><div jsname=\"jXK9ad\" class=\"uMdZh tIxNaf\" jsaction=\"mouseover:UI3Kjd\"><div class=\"VkpGBb\"><div class=\"cXedhc\"><a class=\"vwVdIc wzN8Ac rllt__link a-no-hover-decoration\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" tabindex=\"0\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEAE\"><div><div class=\"rllt__details\"><div class=\"dbg0pd\" aria-level=\"3\" role=\"heading\"><span class=\"OSrXXb\">Y Coffee</span></div><div><span class=\"Y0A0hc\"><span class=\"yi40Hd YrbPuc\" aria-hidden=\"true\">4.0</span><span class=\"z3HNkc\" aria-label=\"Rated 4.0 out of 5,\" role=\"img\"><span style=\"width:56px\"></span></span><span class=\"RDApEe YrbPuc\">(418)</span></span> · <span aria-label=\"Moderately expensive\" role=\"img\">€€</span> · Coffee shop</div><div>Nicosia</div><div class=\"pJ3Ci\"><span>Iconic Seattle-based coffeehouse chain</span></div></div></div></a><a class=\"uQ4NLd b9tNq wzN8Ac rllt__link a-no-hover-decoration\" aria-hidden=\"true\" tabindex=\"-1\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEA4\"><g-img class=\"gTrj3e\"><img id=\"pimg_3\" src=\"https://lh5.googleusercontent.com/p/AF1QipPaihclGQYWEJpMpBnBY8Nl8QWQVqZ6tF--MlwD=w184-h184-n-k-no\" class=\"YQ4gaf zr758c wA1Bge\" alt=\"\" data-atf=\"4\" data-frt=\"0\" width=\"92\" height=\"92\"></g-img></a></div></div></div></div>"
  ]
}

r = requests.post(url=uri, headers=headers, json=data)

print(r.json())

```

Here is the breakdown of the response of such a call:

```json
{
  "prompts": [
    "String, Individual Prompts You need to call OpenAI endpoint with. Separated into multiple calls if the calls exceed the maximum number of tokens allowed by the endpoint."
  ],
  "prompt_objects": {
    "invalid_lines_indexes": "List, An array of elements that their texts are already exceeding the allowed threshold. These results will be skipped and will be returned with an error in the final response.",
    "desired_lines": "List, An array of text contents of HTML elements.",
    "labels": "List, An array of labels the user wants to classify from."
  }
}
```

Here is an example response:

```json
{
  "prompts": [
    "A table with 12 cells in each row summarizing the different parts of the text at each line:\n\nHoundstooth Coffee 4.6(824) · $$ · Coffee shop 401 Congress Ave. #100c · In Frost Bank Tower Closed ⋅ Opens 7AM Cozy hangout for carefully sourced brews\nStarbucks 4.4(471) · $$ · Coffee shop 301 W 3rd St Opens soon ⋅ 5:30AM Iconic Seattle-based coffeehouse chain\nProgress Coffee Bank of America Building 5.0(1) · Cafe 515 Congress Ave. Closed ⋅ Opens 7AM Dine-in·Takeout·No delivery\nCoffee Cantata Nicosia 5.0(3) · Tea store Nicosia Closed ⋅ Opens 10AM Mon In-store shopping\nLa Bella Bakery - Gloria Jean's Coffees K. Kaymaklı 4.4(251) · €€ · Coffee shop Şehit mustafa Ruso Caddesi no:148 - Küçük Kaymaklı - Lefkoşa - KKTC Mersin 10 Turkey Lefkoşa · In Aydın Oto Camları & Döşeme Ltd. On the menu: tea\nA.D.A. Auto Repair Center 4.8(26) · Auto repair shop 30+ years in business · Nicosia · 99 639471 Closes soon ⋅ 3PM \"I strongly recommend this repair shop.\"\nEvolution GYM No reviews · Gym Nicosia · +90 533 821 10 02 Open ⋅ Closes 6PM\nA McDonald's 420 Fulton St · (929) 431-6994 Open ⋅ Closes 1AM Dine-in · Curbside pickup · No-contact delivery\nY Coffee 4.0 (418) · €€ · Coffee shop Nicosia Iconic Seattle-based coffeehouse chain\n| Address | Description Or Review | Expensiveness | Line | Number Of Reviews | Open Hours | Rating | Title | Type | Delivery Options | Phone | Years Of Business |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n| 401 Congress Ave. #100c · In Frost Bank Tower | Cozy hangout for carefully sourced brews | $$ | 1 | 824 | Opens 7AM | 4.1 | Houndstooth Coffee | Coffee Shop | - | - | - |\n| 301 W 3rd St | Iconic Seattle-based coffeehouse chain | $$ | 2 | 471 | Opens soon ⋅ 5:30AM | 4.1 | Starbucks | Coffee Shop | - | - | - |\n| 515 Congress Ave. | - | - | 3 | 1 | Closed ⋅ Opens 7AM | 5.0 | Progress Coffee Bank of America Building | Cafe | Dine-in·Takeout·No delivery | - | - |\n| Nicosia | - | - | 4 | 3 | Closed ⋅ Opens 10AM Mon | 5.0 | Coffee Cantata Nicosia | Tea store | In-store shopping | - | - |\n| Şehit mustafa Ruso Caddesi no:148 - Küçük Kaymaklı - Lefkoşa - KKTC Mersin 10 Turkey Lefkoşa · In Aydın Oto Camları & Döşeme Ltd. | On the menu: tea | €€ | 5 | 251 | - | 4.4 | La Bella Bakery - Gloria Jean's Coffees K. Kaymaklı | Coffee shop | - | - | - |\n| Nicosia | \"I strongly recommend this repair shop.\" | - | 6 | 26 | Closes soon ⋅ 3PM | 4.8 | A.D.A. Auto Repair Center | Auto repair shop | - | 99 648261 | 30+ years in business |\n| Nicosia | - | - | 7 | - | Closes 6PM | - | Evolution GYM | Gym | - | +90 555 827 11 12 | - |\n| 420 Fulton St | - | - | 8 | - | Open ⋅ Closes 1AM | A | McDonald's | - | Dine-in · Curbside pickup · No-contact delivery | (959) 451-6894 | - |"
  ],
  "prompt_objects": {
    "invalid_lines_indexes": [],
    "desired_lines": [
      "Y Coffee 4.0 (418) · €€ · Coffee shop Nicosia Iconic Seattle-based coffeehouse chain"
    ],
    "labels": [
      "Address",
      "Description Or Review",
      "Expensiveness",
      "Line",
      "Number Of Reviews",
      "Open Hours",
      "Rating",
      "Title",
      "Type",
      "Delivery Options",
      "Phone",
      "Years Of Business"
    ]
  },
}
```

- ### Making Server-Side Calls to OpenAI

You can make the calls to OpenAI from your server-side code. The adjustment of parameters to a model should be taken as the same with preset parser you use, or the custom parser you have provided. The `max_tokens` needs to be calculated on server-side per each-call. Here is an example on making a server-side call:

```py
import os
import openai
import requests

uri = "https://ai.kagermanov.com/classify"

headers = {"Content-Type": "application/json"}

data = {
  "prompts_only": True,
  "path": "google.google_local_results",
  "targets": [
    "<div jscontroller=\"AtSb\" class=\"w7Dbne\" data-record-click-time=\"false\" id=\"tsuid_25\" jsdata=\"zt2wNd;_;BvbRxs V6f1Id;_;BvbRxw\" jsaction=\"rcuQ6b:npT2md;e3EWke:kN9HDb\" data-hveid=\"CBUQAA\"><div jsname=\"jXK9ad\" class=\"uMdZh tIxNaf\" jsaction=\"mouseover:UI3Kjd\"><div class=\"VkpGBb\"><div class=\"cXedhc\"><a class=\"vwVdIc wzN8Ac rllt__link a-no-hover-decoration\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" tabindex=\"0\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEAE\"><div><div class=\"rllt__details\"><div class=\"dbg0pd\" aria-level=\"3\" role=\"heading\"><span class=\"OSrXXb\">Y Coffee</span></div><div><span class=\"Y0A0hc\"><span class=\"yi40Hd YrbPuc\" aria-hidden=\"true\">4.0</span><span class=\"z3HNkc\" aria-label=\"Rated 4.0 out of 5,\" role=\"img\"><span style=\"width:56px\"></span></span><span class=\"RDApEe YrbPuc\">(418)</span></span> · <span aria-label=\"Moderately expensive\" role=\"img\">€€</span> · Coffee shop</div><div>Nicosia</div><div class=\"pJ3Ci\"><span>Iconic Seattle-based coffeehouse chain</span></div></div></div></a><a class=\"uQ4NLd b9tNq wzN8Ac rllt__link a-no-hover-decoration\" aria-hidden=\"true\" tabindex=\"-1\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEA4\"><g-img class=\"gTrj3e\"><img id=\"pimg_3\" src=\"https://lh5.googleusercontent.com/p/AF1QipPaihclGQYWEJpMpBnBY8Nl8QWQVqZ6tF--MlwD=w184-h184-n-k-no\" class=\"YQ4gaf zr758c wA1Bge\" alt=\"\" data-atf=\"4\" data-frt=\"0\" width=\"92\" height=\"92\"></g-img></a></div></div></div></div>"
  ]
}

response_from_daath_ai_parser = requests.post(url=uri, headers=headers, json=data)

openai.api_key = os.getenv("OPENAI_API_KEY")

prompts = response_from_daath_ai_parser["prompts"]

responses = []

for prompt in prompts:
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.001,
    max_tokens=400,
    top_p=0.9,
    best_of=2,
    frequency_penalty=0,
    presence_penalty=0
  )
  responses.append(response)

print(responses)
```

- ### Parse Only Call

You can gather the responses on the server-side and then make a call with `parse_only` to get the parsed results. Here is an example on making a `parse_only` call:

```py
import os
import openai
import requests


# Prompts Only Call
uri = "https://ai.kagermanov.com/classify"

headers = {"Content-Type": "application/json"}

data = {
  "prompts_only": True,
  "path": "google.google_local_results",
  "targets": [
    "<div jscontroller=\"AtSb\" class=\"w7Dbne\" data-record-click-time=\"false\" id=\"tsuid_25\" jsdata=\"zt2wNd;_;BvbRxs V6f1Id;_;BvbRxw\" jsaction=\"rcuQ6b:npT2md;e3EWke:kN9HDb\" data-hveid=\"CBUQAA\"><div jsname=\"jXK9ad\" class=\"uMdZh tIxNaf\" jsaction=\"mouseover:UI3Kjd\"><div class=\"VkpGBb\"><div class=\"cXedhc\"><a class=\"vwVdIc wzN8Ac rllt__link a-no-hover-decoration\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" tabindex=\"0\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEAE\"><div><div class=\"rllt__details\"><div class=\"dbg0pd\" aria-level=\"3\" role=\"heading\"><span class=\"OSrXXb\">Y Coffee</span></div><div><span class=\"Y0A0hc\"><span class=\"yi40Hd YrbPuc\" aria-hidden=\"true\">4.0</span><span class=\"z3HNkc\" aria-label=\"Rated 4.0 out of 5,\" role=\"img\"><span style=\"width:56px\"></span></span><span class=\"RDApEe YrbPuc\">(418)</span></span> · <span aria-label=\"Moderately expensive\" role=\"img\">€€</span> · Coffee shop</div><div>Nicosia</div><div class=\"pJ3Ci\"><span>Iconic Seattle-based coffeehouse chain</span></div></div></div></a><a class=\"uQ4NLd b9tNq wzN8Ac rllt__link a-no-hover-decoration\" aria-hidden=\"true\" tabindex=\"-1\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEA4\"><g-img class=\"gTrj3e\"><img id=\"pimg_3\" src=\"https://lh5.googleusercontent.com/p/AF1QipPaihclGQYWEJpMpBnBY8Nl8QWQVqZ6tF--MlwD=w184-h184-n-k-no\" class=\"YQ4gaf zr758c wA1Bge\" alt=\"\" data-atf=\"4\" data-frt=\"0\" width=\"92\" height=\"92\"></g-img></a></div></div></div></div>"
  ]
}

response_from_daath_ai_parser = requests.post(url=uri, headers=headers, json=data)

openai.api_key = os.getenv("OPENAI_API_KEY")

prompts = response_from_daath_ai_parser["prompts"]

responses = []

# Server-Side Call to OpenAI
for prompt in prompts:
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.001,
    max_tokens=400,
    top_p=0.9,
    best_of=2,
    frequency_penalty=0,
    presence_penalty=0
  )
  responses.append(response)

# Parse Only Call

data = {
  "path": "google.google_local_results",
  "parse_only": {
    "responses": responses
    "prompt_objects": response_from_daath_ai_parser["prompt_objects"]
  }
}

response_from_daath_ai_parser = requests.post(url=uri, headers=headers, json=data)

print(response_from_daath_ai_parser.json())
```

Here is an example response with parse only:

```json
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

---

<h2 align="center">Expected Error Responses</h2>

Different OpenAI Errors are served in the response to save the user trouble of looking back and forth:

```json
{
  "results": [
    {
      "message": "Incorrect API key provided: <Your Op*****Key>. You can find your API key at https://beta.openai.com.",
      "type": "invalid_request_error",
      "param": null,
      "code": "invalid_api_key"
    }
  ]
}
```

```json
{
  "results": [
    {
      "message": "You exceeded your current quota, please check your plan and billing details.",
      "type": "insufficient_quota",
      "param": null,
      "code": null
    }
  ]
}
```

If there is a communication error in hosted endpoint for one or more of the concurrent requests, it will results in the following form:

```json
{
  "results": [
    {"error": "Error from Local Machine"}
  ]
}
```

If the element you have passed already exceeds the maximum token size, the error will be in the following form:

```json
{
  "results": [
    {"error": "Maximum Token Size is reached for this prompt. This is skipped."}
  ]
}
```

If there are any other errors you encounter, feel free to create an issue about them.

---

<h2 align="center">Customizing Default Allowed Concurrency and API Key of Cliend-Side Calls</h2>

You can adjust the number of allowed concurrency for the client-side calls with `allowed_concurrency` key. The maximum number of calls you can make per minute is still need to be configured by you. You may put sleep time between calls to `Daath AI Parser` to avoid exceeding the limit imposed by OpenAI. Here is an example script where allowed concurrency is 2:

```python
import requests

uri = "https://ai.kagermanov.com/classify"

headers = {"Content-Type": "application/json"}

data = {
  "allowed_concurrency": 2,
  "path": "google.google_local_results",
  "targets": [
    "<div jscontroller=\"AtSb\" class=\"w7Dbne\" data-record-click-time=\"false\" id=\"tsuid_25\" jsdata=\"zt2wNd;_;BvbRxs V6f1Id;_;BvbRxw\" jsaction=\"rcuQ6b:npT2md;e3EWke:kN9HDb\" data-hveid=\"CBUQAA\"><div jsname=\"jXK9ad\" class=\"uMdZh tIxNaf\" jsaction=\"mouseover:UI3Kjd\"><div class=\"VkpGBb\"><div class=\"cXedhc\"><a class=\"vwVdIc wzN8Ac rllt__link a-no-hover-decoration\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" tabindex=\"0\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEAE\"><div><div class=\"rllt__details\"><div class=\"dbg0pd\" aria-level=\"3\" role=\"heading\"><span class=\"OSrXXb\">Y Coffee</span></div><div><span class=\"Y0A0hc\"><span class=\"yi40Hd YrbPuc\" aria-hidden=\"true\">4.0</span><span class=\"z3HNkc\" aria-label=\"Rated 4.0 out of 5,\" role=\"img\"><span style=\"width:56px\"></span></span><span class=\"RDApEe YrbPuc\">(418)</span></span> · <span aria-label=\"Moderately expensive\" role=\"img\">€€</span> · Coffee shop</div><div>Nicosia</div><div class=\"pJ3Ci\"><span>Iconic Seattle-based coffeehouse chain</span></div></div></div></a><a class=\"uQ4NLd b9tNq wzN8Ac rllt__link a-no-hover-decoration\" aria-hidden=\"true\" tabindex=\"-1\" jsname=\"kj0dLd\" data-cid=\"12176489206865957637\" jsaction=\"click:h5M12e;\" role=\"link\" data-ved=\"2ahUKEwiS1P3_j-P7AhXnVPEDHa0oAiAQvS56BAgVEA4\"><g-img class=\"gTrj3e\"><img id=\"pimg_3\" src=\"https://lh5.googleusercontent.com/p/AF1QipPaihclGQYWEJpMpBnBY8Nl8QWQVqZ6tF--MlwD=w184-h184-n-k-no\" class=\"YQ4gaf zr758c wA1Bge\" alt=\"\" data-atf=\"4\" data-frt=\"0\" width=\"92\" height=\"92\"></g-img></a></div></div></div></div>"
  ],
  "openai_key": "<OPENAI KEY>"
}

r = requests.post(url=uri, headers=headers, json=data)

print(r.json()["results"])
```

By default, allowed concurrency is `1`. You can change the default `allowed_concurrency` and default `openai_key` from `credentials.py` when you set your own server.

---

<h2 align="center">Contributions Guide</h2>

For recent updates, head to [Contributions Guide Page](https://github.com/kagermanov27/daath-ai-parser/blob/master/CONTRIBUTING.md)

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
[Build-shield]: https://github.com/kagermanov27/daath-ai-parser/actions/workflows/python-app.yml/badge.svg
[Build-url]: https://github.com/kagermanov27/daath-ai-parser/actions/workflows/python-app.yml
[contributors-shield]: https://img.shields.io/github/contributors/kagermanov27/daath-ai-parser.svg
[contributors-url]: https://github.com/kagermanov27/daath-ai-parser/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kagermanov27/daath-ai-parser.svg
[forks-url]: https://github.com/kagermanov27/daath-ai-parser/network/members
[stars-shield]: https://img.shields.io/github/stars/kagermanov27/daath-ai-parser.svg
[stars-url]: https://github.com/kagermanov27/daath-ai-parser/stargazers
[issues-shield]: https://img.shields.io/github/issues/kagermanov27/daath-ai-parser.svg
[issues-url]: https://github.com/kagermanov27/daath-ai-parser/issues
[issuesclosed-shield]: https://img.shields.io/github/issues-closed/kagermanov27/daath-ai-parser.svg
[issuesclosed-url]: https://github.com/kagermanov27/daath-ai-parser/issues?q=is%3Aissue+is%3Aclosed
[board-shield]: https://img.shields.io/badge/Kanban-Board-grey?logo=data:image/svg%2bxml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEzLjM1MiAxNC41ODVsLTQuNTA5IDQuNjE0LjcyLTQuMDYyTDMuNDI4IDcuNTcgMCA3Ljc1MyA3LjU4IDB2Mi45NTNsNy4yMTQgNi42NDYgNC41MTMtMS4xMDUtNC42ODkgNC45ODJMMjQgMjRsLTEwLjY0OC05LjQxNXoiLz48L3N2Zz4=
[board-url]: https://github.com/kagermanov27/daath-ai-parser/projects/1
[license-shield]: https://img.shields.io/github/license/kagermanov27/daath-ai-parser.svg
[license-url]: https://github.com/kagermanov27/daath-ai-parser/blob/master/LICENSE
[server-shield]: https://img.shields.io/website?down_color=Red&down_message=Down&label=Server&up_color=Green&up_message=Up&url=https%3A%2F%2Fai.kagermanov.com
[server-url]: https://ai.kagermanov.com