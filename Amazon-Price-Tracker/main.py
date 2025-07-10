import smtplib
from bs4 import BeautifulSoup
import lxml
import requests

# Replace with your actual email and app password
MY_EMAIL = "your_email@example.com"
MY_PASSWORD = "your_app_password"
TO_EMAIL = "recipient_email@example.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.6"
}

url = "https://www.amazon.in/OnePlus-13R-Smarter-Lifetime-Warranty/dp/B0DPS62DYH"
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

price_tag = soup.select_one("#corePriceDisplay_desktop_feature_div .a-section .a-price-whole")

if price_tag:
    price = int(price_tag.getText().replace(",", ""))
    if price < 50000:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject:Price Alert!\n\nThe price is now ₹{price}! Check it out here: {url}"
            )
else:
    print("Price tag not found.")
