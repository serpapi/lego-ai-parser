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
      "Add to Favourites",
      "Add to basket"
    ],
    "examples_for_prompt": [
      {
        "text": f"1 Ct Diamond Tennis Bracelet, 14K Solid Yellow Gold, Natural Real Stones, Elegant Gift For Woman, Fine Jewelry, 7.5\" (401) Star Seller Sale Price EUR 756.96 EUR 756.96 EUR 1,081.38 Original Price EUR 1,081.38 (30% off) Sale ends in 30 hours Ad vertisement by Etsy seller Ad from Etsy seller RaffaelloDitty From shop RaffaelloDitty FREE delivery",
        "classifications": {
          "line": "1",
          "tags": f"#$Star Seller#$30% off#$Sale ends in 30 hours#$#$Ad from Etsy seller#$FREE delivery#$",
          "title": "1 Ct Diamond Tennis Bracelet, 14K Solid Yellow Gold, Natural Real Stones, Elegant Gift For Woman, Fine Jewelry, 7.5\"",
          "shop": "RaffaelloDitty",
          "price": "EUR 756.96",
          "old_price": "EUR 1,081.38",
          "number_of_reviews": "401"
        }
      },
      {
        "text": "european bracelet big hole bead, artisan glass bead silver tube, Halloween, Large Hole, Silver Core, European Bracelet Beads, Christmas gift (70) EUR 16.00 ad vertisement by Etsy seller Ad from Etsy seller DewLampworkGlass From shop DewLampworkGlass Only 1 left — order soon",
        "classifications": {
          "line": "2",
          "tags": "#$Only 1 left — order soon#$Ad from Etsy seller#$",
          "title": "european bracelet big hole bead, artisan glass bead silver tube, Halloween, Large Hole, Silver Core, European Bracelet Beads, Christmas gift",
          "shop": "DewLampworkGlass",
          "price": "EUR 16.00"
        }
      },
      {
        "text": f"Taurus Crystal Bracelet, Taurus Bracelet Birthstone, Black Onyx Jewelry, Tigers Eye Bracelet Natural Stone, Gift for Taurus, Taurus Crystals (711) Sale Price EUR 27.00 EUR 27.00 EUR 30.00 Original Price EUR 30.00 (10% off)  ad vertisement by Etsy seller Ad from Etsy seller MelyannaCrystals From shop MelyannaCrystals FREE delivery",
        "classifications": {
          "line": "3",
          "tags": f"#$10% off#$Ad from Etsy seller#$FREE delivery#$",
          "title": "Taurus Crystal Bracelet, Taurus Bracelet Birthstone, Black Onyx Jewelry, Tigers Eye Bracelet Natural Stone, Gift for Taurus, Taurus Crystals",
          "shop": "MelyannaCrystals",
          "price": "EUR 27.00",
          "old_price": "EUR 30.00"
        }
      }
    ]
  })
