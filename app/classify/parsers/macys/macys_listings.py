from app.schemas import *

def commands():
  return json_to_pydantic({
    "main_prompt": "A table with NUMBER_OF_LABELS cells in each row summarizing the different parts of the text at each line:\n\n",
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
      "Add to Favourites",
      "Add to basket"
    ],
    "examples_for_prompt": [
      {
        "text": "Limited-Time Special +2 Alfani Women's Ultra-Soft Printed Packaged Pajama Set, Created for Macy's TRY 1,338.50 Sale TRY 577.60  (279)",
        "classifications": {
          "line": "1",
          "brand": "Alfani",
          "title": "Women's Ultra-Soft Printed Packaged Pajama Set, Created for Macy's",
          "shop": "RaffaelloDitty",
          "price": "TRY 577.60",
          "old_price": "TRY 1,338.50",
          "number_of_reviews": "279",
          "deal": "Limited-Time Special"
        }
      },
      {
        "text": "Deal of the Day +4 Alfani Women's Seam-Front Mock Neck Sweater, Created for Macy's TRY 1,146.00 Sale TRY 458.40 Flash Sale 60% Off  (39)",
        "classifications": {
          "line": "2",
          "brand": "Alfani",
          "title": "Women's Seam-Front Mock Neck Sweater, Created for Macy's",
          "shop": "RaffaelloDitty",
          "price": "TRY 458.40",
          "old_price": "TRY 1,146.00",
          "number_of_reviews": "39",
          "deal": "Deal of the Day"
        }
      },
      {
        "text": "Limited-Time Special Alfani Men's Classic-Fit Stretch Black Tuxedo Separates, Created for Macy's TRY 2,214.90 - 6,933.50 Sale TRY 885.90 - 2,773.40  (2)",
        "classifications": {
          "line": "3",
          "brand": "Alfani",
          "title": "Men's Classic-Fit Stretch Black Tuxedo Separates, Created for Macy's",
          "shop": "RaffaelloDitty",
          "price": "TRY 885.90 - 2,773.40",
          "old_price": "TRY 2,214.90 - 6,933.50",
          "number_of_reviews": "2",
          "deal": "Limited-Time Special"
        }
      }
    ]
  })
