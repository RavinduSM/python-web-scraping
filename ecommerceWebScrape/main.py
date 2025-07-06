from bs4 import BeautifulSoup
import requests

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')

product_cards = soup.select(".card.thumbnail")

for card in product_cards:
    name = card.select_one("a.title")["title"]
    price = card.select_one("span[itemprop='price']").text.strip()
    description = card.select_one("p[itemprop='description']").text.strip()
    more_info = card.select_one("a")['href']
    full_link = url + more_info

    print("Name:", name)
    print("Price:", price)
    print("Description:", description)
    print("more Information link:", full_link)
    print("-" * 40)

    detail_response = requests.get(full_link)
    detail_soup = BeautifulSoup(detail_response.text, "html")

 

    print("-" * 60)