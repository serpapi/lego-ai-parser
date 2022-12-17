from app.schemas import *

def commands():
  return json_to_pydantic({
    "main_prompt": "A table with NUMBER_OF_LABELS cells in each row summarizing the different parts of the examples at each new line below here and above the table. Elements in cells containing multiple elements are separated by #$\n\n",
    "data": {
      "model": "text-davinci-003",
      "temperature": 0.01,
      "top_p": 0.8,
      "best_of": 1,
      "frequency_penalty": 0,
      "presence_penalty": 0
    },
    "model_specific_token_size": 3800,
    "openai_endpoint": "https://api.openai.com/v1/completions",
    "explicitly_excluded_strings": [
      "\n",
      "Opens in a new tab",
      "Quickview",
      "Save this item to your list"
    ],
    "examples_for_prompt": [
      {
        "text": "Wayfair's Choice Oliverson 661 lb. Capacity Stack Chair with Air-Vent Back and Powder Coated Sled Base by Inbox Zero $48.99$142.00 (168) Rated 4.5 out of 5 stars.168 total votes Free shipping Sponsored Grab the attention of visitors when they step into your meeting space and see these smart looking guest chairs. This modern beauty features a fully perforated back to provide airflow during conference hall meetings. Designed for versatility this chair is designed for reception areas, school functions, break rooms, cafeterias, event spaces and express emission testing locations where customers must get out their vehicle. Always be ready for guests by having several plastic guest chairs tucked away in your home. If you work in grungy environments and need a chair that is easy to clean plastic stack chairs are ideal. Store or transport up to 5 chairs on our compatible steel sled base stack chair dolly. When in need of a space-saving seating solution that is permanent or temporary, allow this stackable side chair to work for you. Overall: 31'' H x 17.75'' W x 20'' D Overall Product Weight: 8lb. These are currently the best value on Wayfair! An 8 pound chair that holds 661 pounds and requires no assembly. They stack easily and can be used at a desk, dining table, etc. I bought them in orange and in black.. Carrie. ellington, CT. 2022-06-26 18:28:36",
        "classifications": {
          "line": "1",
          "tags": "#$Free shipping#$Sponsored#$Wayfair's Choice#$",
          "title": "Oliverson 661 lb. Capacity Stack Chair with Air-Vent Back and Powder Coated Sled Base",
          "brand": "Inbox Zero",
          "price": "$48.99",
          "old_price": "$142.00",
          "number_of_votes": "168",
          "average_rating": "4.5",
          "details": "#$Overall: 31'' H x 17.75'' W x 20'' D#$Overall Product Weight: 8lb.#$"
        }
      },
      {
        "text": "+5 Sizes Available in 6 Sizes Sealy Cool 12\" Medium Memory Foam Mattress with CopperChill Technology by\xa0 Sealy From$365.99$1,099.00 Open Box Price:$504.00 (2284) Rated 4.5 out of 5 stars.2284 total votes Fast Delivery FREE Shipping Get it by Thu. Dec 22 Comfort Level Medium Mattress Type Memory Foam Mattress Thickness 12'' Sponsored",
        "classifications": {
          "line": "2",
          "tags": "#$6 Sizes#$Open Box Price:$504.00#$Fast Delivery#$FREE Shipping#$Get it by Thu. Dec 22#$Sponsored#$",
          "title": "Sealy Cool 12\" Medium Memory Foam Mattress with CopperChill Technology",
          "brand": "Sealy",
          "price": "$365.99",
          "old_price": "$1,099.00",
          "number_of_votes": "2284",
          "average_rating": "4.5",
          "details": "#$Comfort Level Medium#$Mattress Type Memory Foam#$Mattress Thickness 12''#$"
        }
      },
      {
        "text": "Sale +3 Sizes Available in 4 Sizes 6'' Mattress by Home Life From $91.99 $161.99 ( 164 ) Rated 4 out of 5 stars. 164 total votes Free shipping Mattress Type Innerspring Mattress Thickness 6''",
        "classifications": {
          "line": "3",
          "brand": "Home Life",
          "details": "#$Mattress Type Innerspring#$Mattress Thickness 6''#$",
          "number_of_votes": "164",
          "old_price": "$161.99",
          "price": "$91.99",
          "average_rating": "4",
          "tags": "#$4 Sizes#$Free shipping#$Sale#$",
          "title": "6'' Mattress"
        }
      }
    ]
  })