from app.schemas import *

def commands():
  return json_to_pydantic({
    "main_prompt": "A table with NUMBER_OF_LABELS cells in each row summarizing the different parts of the examples at each new line below here and above the table. Elements in cells containing multiple elements are separated by #$\n\n",
    "data": {
      "model": "text-davinci-003",
      "temperature": 0.01,
      "top_p": 0.9,
      "best_of": 1,
      "frequency_penalty": 0,
      "presence_penalty": 0
    },
    "model_specific_token_size": 3800,
    "openai_endpoint": "https://api.openai.com/v1/completions",
    "explicitly_excluded_strings": [
      "\n",
      "Compare Product"
    ],
    "examples_for_prompt": [
      {
        "text": "Quick Ship $1,099.99 Price valid through 12/25/22 Samsung 65\" Class - Q80BD Series - 4K UHD QLED LCD TV - Allstate 3-Year Protection Plan Bundle Included for 5 years of total coverage* Rated 4.6 out of 5 stars based on 441 reviews. (441) Select Options",
        "classifications": {
          "line": "1",
          "tags": "#$Quick Ship#$",
          "price_info": "Price valid through 12/25/22",
          "title": "Samsung 65\" Class - Q80BD Series - 4K UHD QLED LCD TV - Allstate 3-Year Protection Plan Bundle Included for 5 years of total coverage*",
          "rating": "4.6",
          "number_of_reviews": "441",
          "price": "$1,099.99",
          "options_available": "Options"
        }
      },
      {
        "text": "Sponsored $18.99 $6 OFF Starbucks French Roast, Whole Bean Coffee, 2.5 lbs May be available In-Warehouse at a lower non-delivered price  Add sponsored",
        "classifications": {
          "line": "2",
          "pice_info": "$6 OFF",
          "product_info": "May be available In-Warehouse at a lower non-delivered price",
          "title": "Starbucks French Roast, Whole Bean Coffee, 2.5 lbs",
          "price": "$18.99",
          "sponsored": "Sponsored"
        }
      },
      {
        "text": "$14.99 After $8 OFF Starbucks Organic Winter Blend Whole Bean Coffee, Medium, 2.5 lbs Out of Stock",
        "classifications": {
          "line": "3",
          "price_info": "$8 OFF",
          "title": "Starbucks Organic Winter Blend Whole Bean Coffee, Medium, 2.5 lbs",
          "price": "$14.99",
          "out_of_stock": "Out of Stock"
        }
      }
    ]
  })
