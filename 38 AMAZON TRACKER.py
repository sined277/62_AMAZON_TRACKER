import requests
from bs4 import BeautifulSoup
import smtplib

# Amazon product URL
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Headers to send with the request
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "Accept-Language": "ru-UA,ru;q=0.9,en-US;q=0.8,en;q=0.7,ru-RU;q=0.6,uk;q=0.5"
}

# Send the request and get the response
response = requests.get(url, headers=header)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

# Get the price of the product
price = soup.find(class_="a-offscreen").text
price_without_currency = price.split('$')[1]
price_as_float = float(price_without_currency)

# Set the price we want to buy at
BUY_PRICE = 70

# If the current price is less than the buy price, send an email notification
if price_as_float < BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Establish a secure connection to the SMTP server
        connection.starttls()
        # Login to your email account
        connection.login(MY_EMAIL, MY_PASSWORD)
        # Send the email notification with the Amazon product URL
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n\n{url}".encode("utf-8")
        )

