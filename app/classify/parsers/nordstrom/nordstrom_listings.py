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
        "text": "Previous Next Sustainable Style Nordstrom Recycled Cashmere Blend Beanie $44.00 Current Price $44.00 (21) Free Delivery",
        "classifications": {
          "line": "1",
          "brand": "Nordstrom",
          "title": "Recycled Cashmere Blend Beanie",
          "price": "$44.00",
          "number_of_reviews": "21"
        }
      },
      {
        "text": f"Zella Pyrite Slim Fit Pocket Joggers $17.99 Current Price $17.99 (69% off) 69% off. $59.00 Previous Price $59.00 (133) Free Delivery",
        "classifications": {
          "line": "2",
          "brand": "Zella",
          "title": "Pyrite Slim Fit Pocket Joggers",
          "price": "$17.99",
          "old_price": "$59.00",
          "number_of_reviews": "133"
        }
      },
      {
        "text": f"Limited-Time Sale Nike Everyday Plus 6-Pack Cushioned Low Socks $16.50 Current Price $16.50 (25% off) 25% off. $22.00 Previous Price $22.00 (10) Free Delivery",
        "classifications": {
          "line": "3",
          "brand": "Nike",
          "title": "Everyday Plus 6-Pack Cushioned Low Socks",
          "price": "$16.50",
          "old_price": "$22.00",
          "number_of_reviews": "10",
          "deal": "Limited-Time Special"
        }
      },
      {
        "text": f"Previous Next Limited-Time Sale Nike Sportswear Club Hoodie $48.00 – $55.00 Current Price $48.00 to $55.00 (Up to 12% off select items) Up to 12% off select items. $55.00 Previous Price $55.00 (136) Free Delivery",
        "classifications": {
          "line": "3",
          "brand": "Nike",
          "title": "Sportswear Club Hoodie",
          "price": "$48.00 to $55.00",
          "old_price": "$55.00",
          "number_of_reviews": "136",
          "deal": "Limited-Time Special"
        }
      }
    ]
  })
