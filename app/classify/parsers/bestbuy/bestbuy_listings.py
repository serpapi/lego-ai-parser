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
      "Add to Cart",
      "Compare Save",
      "Compare",
      "Learn more",
    ],
    "examples_for_prompt": [
      {
        "text": "Sony - PlayStation 5 - DualSense Wireless Controller - Cosmic Red SKU: 6464309 more Color:Cosmic Red Get previous slide selected Get next slide Rating 4.8 out of 5 stars with 2465 reviews (2,465) $49.99 Your price for this item is $49.99 Save $25Was $74.99 The previous price was $74.99 Open-Box: from $39.99 Get it today Pickup: Ready in 1 hour at Bangor See all pickup locations FREE Shipping: Get it by Wed, Dec 21 See all shipping options for 04785 Save",
        "classifications": {
          "line": "1",
          "title": "Sony - PlayStation 5 - DualSense Wireless Controller - Cosmic Red",
          "price": "$49.99",
          "old_price": "$74.99",
          "number_of_reviews": "2465",
          "rating": "4.8",
          "product_details": "#$Color:Cosmic Red#$SKU: 6464309#$",
          "tags": "#$Open-Box: from $39.99#$Save $25#$Was $74.99#$The previous price was $74.99#$Get it today#$",
          "shipping_information": "#$Pickup: Ready in 1 hour at Bangor#$FREE Shipping: Get it by Wed, Dec 21#$"
        }
      },
      {
        "text": "Microsoft - Xbox Series X 1TB Console - Black SKU: 6428324 more Rating 4.9 out of 5 stars with 22363 reviews (22,363) $499.99 Your price for this item is $499.99 High Demand Product This item is expected to sell out quickly. To improve your odds of getting one, we've updated our reservation process. Save",
        "classifications": {
          "line": "2",
          "title": "Microsoft - Xbox Series X 1TB Console - Black",
          "price": "$499.99",
          "number_of_reviews": "22363",
          "rating": "4.9",
          "product_details": "#$SKU: 6428324#$",
          "tags": "#$High Demand Product#$This item is expected to sell out quickly. To improve your odds of getting one, we've updated our reservation process.#$"
        }
      },
      {
        "text": "Sony - PlayStation 5 Digital Edition Console SKU: 6430161 more Rating 4.9 out of 5 stars with 6199 reviews (6,199) $399.99 Your price for this item is $399.99 Sold Out This item is currently sold out but we are working to get more inventory. Sold Out Save",
        "classifications": {
          "line": "3",
          "title": "Sony - PlayStation 5 Digital Edition Console",
          "price": "$399.99",
          "number_of_reviews": "6199",
          "rating": "4.9",
          "product_details": "#$SKU: 6430161#$",
          "tags": "#$This item is currently sold out but we are working to get more inventory.#$",
          "sold_out": "Sold Out"
        }
      },
      {
        "text": "Sponsored Pokémon Violet - Nintendo Switch, Nintendo Switch (OLED Model), Nintendo Switch Lite Publisher: Nintendo SKU: 6464088 Release Date: 11/18/2022 ESRB Rating: E (Everyone) Rating 4.2 out of 5 stars with 608 reviews (608) Get it today Pickup: Ready in 1 hour at Bangor See all pickup locations FREE Shipping: Get it by Wed, Dec 21 See all shipping options for 04785 Save $59.99 Your price for this item is $59.99",
        "classifications": {
          "line": "4",
          "number_of_reviews": "608",
          "price": "$59.99",
          "product_details": "#$Publisher: Nintendo#$SKU: 6464088#$Release Date: 11/18/2022#$ESRB Rating: E (Everyone)#$",
          "rating": "4.2",
          "shipping_information": "#$Pickup: Ready in 1 hour at Bangor#$FREE Shipping: Get it by Wed, Dec 21#$",
          "tags": "#$Sponsored#$Save $59.99#$Your price for this item is $59.99#$Get it today#$",
          "title": "Pokémon Violet - Nintendo Switch, Nintendo Switch (OLED Model), Nintendo Switch Lite"
        }
      }
    ]
  })
