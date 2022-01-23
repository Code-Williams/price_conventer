import requests
from bs4 import BeautifulSoup

URL = "https://www.tgju.org/currency"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

toman_price = int(input("Enter toman price to convert : "))

tgju = {
    "dollar_price" : int(soup.find("tr", {"data-market-row":"price_dollar_rl"})['data-price'].replace(",", "")[:-1]),
    "euro_price" : int(soup.find("tr", {"data-market-row":"price_eur"})['data-price'].replace(",", "")[:-1]),"lir_price" : int(soup.find("tr", {"data-market-row":"price_try"})['data-price'].replace(",", "")[:-1]),"derham_price" : int(soup.find("tr", {"data-market-row":"price_aed"})['data-price'].replace(",", "")[:-1])
}

for price_name in tgju:
    price = tgju[price_name]
    convert_toman = toman_price / price
    print(f"{price_name} => {price} => {round(convert_toman, 2)}")