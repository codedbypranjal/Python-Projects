from bs4 import BeautifulSoup
import requests,smtplib,os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
SID=os.getenv('ACC_SID')
AUTH=os.getenv('AUTH_TOKEN')
FROMPHONE=os.getenv('PHONE_FR')
TOPHONE=os.getenv("PHONE_TO")


response=requests.get(url='https://www.sharesansar.com/company/unhpl')
soup=BeautifulSoup(response.text,'html.parser')
price=soup.find(name="span",class_="text-comp-red comp-price padding-second")
current_price=float(price.get_text(strip=True))
print(current_price)
if current_price>528:
    client = Client(SID, AUTH)
    message = client.messages \
        .create(
        body=f'Price Increased 🔼📈!! \n\n The price of the share increased by Rs.{current_price-528 }🔥',
        from_="FROMPHONE",
        to="TOPHONE"
    )
if current_price<534:
    client = Client(SID, AUTH)
    message = client.messages \
        .create(
        body=f'Price Decreased🔻📉!! \n\n The price of the share decreased by Rs.{534-current_price }😵 )',
        from_="FROMPHONE",
        to='TOPHONE'
    )


