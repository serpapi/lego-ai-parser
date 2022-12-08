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
      {
        "text": "Starbucks 4.4(471) · $$ · Coffee shop 301 W 3rd St Opens soon ⋅ 5:30AM Iconic Seattle-based coffeehouse chain",
        "classifications": {
          "line": "2",
          "title": "Starbucks",
          "rating": "4.1",
          "number_of_reviews": "471",
          "expensiveness": "$$",
          "type": "Coffee Shop",
          "address": "301 W 3rd St",
          "open_hours": "Opens soon ⋅ 5:30AM",
          "description_or_review": "Iconic Seattle-based coffeehouse chain"
        }
      },
      {
        "text": "Progress Coffee Bank of America Building 5.0(1) · Cafe 515 Congress Ave. Closed ⋅ Opens 7AM Dine-in·Takeout·No delivery",
        "classifications": {
          "line": "3",
          "title": "Progress Coffee Bank of America Building",
          "rating": "5.0",
          "number_of_reviews": "1",
          "type": "Cafe",
          "address": "515 Congress Ave.",
          "open_hours": "Closed ⋅ Opens 7AM",
          "delivery_options": "Dine-in·Takeout·No delivery"
        }
      },
      {
        "text": "Coffee Cantata Nicosia 5.0(3) · Tea store Nicosia Closed ⋅ Opens 10AM Mon In-store shopping",
        "classifications": {
          "line": "4",
          "title": "Coffee Cantata Nicosia",
          "rating": "5.0",
          "number_of_reviews": "3",
          "type": "Tea store",
          "address": "Nicosia",
          "open_hours": "Closed ⋅ Opens 10AM Mon",
          "delivery_options": "In-store shopping"
        }
      },
      {
        "text": "La Bella Bakery - Gloria Jean's Coffees K. Kaymaklı 4.4(251) · €€ · Coffee shop Şehit mustafa Ruso Caddesi no:148 - Küçük Kaymaklı - Lefkoşa - KKTC Mersin 10 Turkey Lefkoşa · In Aydın Oto Camları & Döşeme Ltd. On the menu: tea",
        "classifications": {
          "line": "5",
          "title": "La Bella Bakery - Gloria Jean's Coffees K. Kaymaklı",
          "rating": "4.4",
          "number_of_reviews": "251",
          "expensiveness": "€€",
          "type": "Coffee shop",
          "address": "Şehit mustafa Ruso Caddesi no:148 - Küçük Kaymaklı - Lefkoşa - KKTC Mersin 10 Turkey Lefkoşa · In Aydın Oto Camları & Döşeme Ltd.",
          "description_or_review": "On the menu: tea"
        }
      },
      {
        "text": "A.D.A. Auto Repair Center 4.8(26) · Auto repair shop 30+ years in business · Nicosia · 99 639471 Closes soon ⋅ 3PM \"I strongly recommend this repair shop.\"",
        "classifications": {
          "line": "6",
          "title": "A.D.A. Auto Repair Center",
          "rating": "4.8",
          "number_of_reviews": "26",
          "type": "Auto repair shop",
          "address": "Nicosia",
          "open_hours": "Closes soon ⋅ 3PM",
          "years_of_business": "30+ years in business",
          "description_or_review": "\"I strongly recommend this repair shop.\"",
          "phone": "99 008200"
        }
      },
      {
        "text": "Evolution GYM No reviews · Gym Nicosia · +90 533 821 10 02 Open ⋅ Closes 6PM",
        "classifications": {
          "line": "7",
          "title": "Evolution GYM",
          "type": "Gym",
          "address": "Nicosia",
          "open_hours": "Closes 6PM",
          "phone": "+90 000 827 11 00"
        }
      },
      {
        "text": "A McDonald's 420 Fulton St · (929) 431-6994 Open ⋅ Closes 1AM Dine-in · Curbside pickup · No-contact delivery",
        "classifications": {
          "line": "8",
          "title": "McDonald's",
          "rating": "A",
          "address": "420 Fulton St",
          "open_hours": "Open ⋅ Closes 1AM",
          "delivery_options": "Dine-in · Curbside pickup · No-contact delivery",
          "phone": "(900) 451-6800"
        }
      }
    ]
  })