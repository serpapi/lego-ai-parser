from app.schemas import *

def commands():
  return json_to_pydantic({
    "main_prompt": "A table with NUMBER_OF_LABELS cells in each row summarizing the different parts of the text where elements in cells that might contain multiple elements are separated by #$:\n\n",
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
      "\n",
    ],
    "examples_for_prompt": [
      {
        "text": "Featured from our brands Allegro Coffee, Coffee Decaf Colombia El Premio De Timana Ground, 12 Ounce 12 Ounce (Pack of 1) 4.6 4.6 out of 5 stars (353) Amazon brand",
        "classifications": {
          "line": "1",
          "title": "Allegro Coffee, Coffee Decaf Colombia El Premio De Timana Ground, 12 Ounce",
          "brand_information": "Featured from our brands",
          "scale": "12 Ounce (Pack of 1)",
          "rating": "4.6",
          "reviews": "353"
        }
      },
      {
        "text": "Krispy Kreme Original Glazed Doughnut, Ground Coffee, Flavored Medium Roast, Bagged 12 oz 12 Ounce (Pack of 1) 4.5 4.5 out of 5 stars (1,489) Options: 3 flavors 3 flavors",
        "classifications": {
          "line": "2",
          "title": "Krispy Kreme Original Glazed Doughnut, Ground Coffee, Flavored Medium Roast, Bagged 12 oz",
          "scale": "12 Ounce (Pack of 1)",
          "rating": "4.5",
          "reviews": "1,489",
          "product_options": "3 flavors#$"
        }
      },
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
      {
        "text": "Best Seller Sponsored Ad - Nifty Coffee Pod Carousel – Compatible with K-Cups, 35 Pod Pack Storage, Spins 360-Degrees, Lazy Susan Plat... Sponsored Nifty Coffee Pod Carousel – Compatible with K-Cups, 35 Pod Pack Storage, Spins 360-Degrees, Lazy Susan Platform, Modern Black Design, Home or Office Kitchen Counter Organizer 4.9 4.9 out of 5 stars (84,749) $19.99 $29.99 Ships to Turkey Small Business Shop products from small business brands sold in Amazon’s store. Discover more about the small businesses partnering with Amazon and Amazon’s commitment to empowering them. Learn more",
        "classifications": {
          "line": "4",
          "title": "Nifty Coffee Pod Carousel – Compatible with K-Cups, 35 Pod Pack Storage, Spins 360-Degrees, Lazy Susan Platform, Modern Black Design, Home or Office Kitchen Counter Organizer",
          "rating": "4.9",
          "reviews": "84,749",
          "tags": "Best Seller#$Sponsored Ad#$Small Business#$",
          "old_price": "$29.99",
          "price": "$19.99",
          "shipment_information": "Ships to Turkey"
        }
      },
      {
        "text": "Apple MacBook Pro 13.3\" with Retina Display, M1 Chip with 8-Core CPU and 8-Core GPU, 16GB Memory, 512GB SSD, Space Gray, Late 2020 4.6 4.6 out of 5 stars (45) $1,799.99 Only 2 left in stock - order soon. More Buying Choices $1,399.55(2 used & new offers)",
        "classifications": {
          "line": "5",
          "title": "Apple MacBook Pro 13.3\" with Retina Display, M1 Chip with 8-Core CPU and 8-Core GPU, 16GB Memory, 512GB SSD, Space Gray, Late 2020",
          "rating": "4.6",
          "reviews": "45",
          "price": "$1,799.99",
          "stock_information": "Only 2 left in stock - order soon",
          "more_buying_options": "$1,399.55#$2 used & new offers#$"
        }
      },
      {
        "text": "Hoerrye for iPhone 14 Pro Max & iPhone 14 Pro Camera Lens Protector, Case-Friendly, Military-Grade Shockproof Camera Protection for iPhone Accessories - Colorful 3.8 3.8 out of 5 stars (307) $12.99 Save 20% with coupon Ships to Turkey More Buying Choices $11.49(2 used & new offers) +8 colors/patterns",
        "classifications": {
          "line": "6",
          "title": "Hoerrye for iPhone 14 Pro Max & iPhone 14 Pro Camera Lens Protector, Case-Friendly, Military-Grade Shockproof Camera Protection for iPhone Accessories - Colorful",
          "rating": "3.8",
          "reviews": "307",
          "price": "$12.99",
          "tags": "Save 20% with coupon",
          "shipment_information": "Ships to Turkey",
          "more_buying_options": "$11.49#$2 used & new offers#$",
          "product_options": "+8 colors/patterns#$"
        }
      },
    ]
  })