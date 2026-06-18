from bs4 import BeautifulSoup
import requests,smtplib,os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
SID=os.getenv('ACC_SID')
AUTH=os.getenv('AUTH_TOKEN')
FROMPHONE=os.getenv('PHONE_FR')
TOPHONE=os.getenv("PHONE_TO")


stocks=['NABIL','NTC','CITY','KBL']
current_price=[]
for stock in stocks:
    response=requests.get(url=f'https://merolagani.com/CompanyDetail.aspx?symbol={stock}')
    soup=BeautifulSoup(response.text,'html.parser')
    price=soup.find(name="span",id="ctl00_ContentPlaceHolder1_CompanyDetail1_lblMarketPrice")
    f_price=float(price.get_text(strip=True))
    dict = {stock: f_price}
    current_price.append(dict)
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


