from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "lxml")

def find_prices():
    prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
    final_price = []
    to_remove = ["+", "bd", "/mo", " 1"]

    for price in prices:
        price_text = price.getText()
        for item in to_remove:
            price_text = price_text.replace(item, "")
        final_price.append(price_text.strip())

    return final_price


def find_hrefs():
    hrefs = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
    links = []
    for href in hrefs:
        links.append(href["href"])
    return links


def find_addrs():
    addresses = soup.find_all(name="address")
    address_list = []
    for address in addresses:
        address_list.append(address.getText().replace("|","").strip())
    return address_list
    

