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
    stock_data = {stock: f_price}
    current_price.append('stock_data')

def bull(name,ltp,inv):
    client = Client(SID, AUTH)
    message = client.messages.create(
        body=f'🚀 {name} ALERT 🟢📈 \n LTP:{ltp} \n CP: {inv}\nChange: { +((ltp-inv)/inv)*100}%',
        from_="FROMPHONE",
        to="TOPHONE"
    )
def bear(name,ltp,inv):
    client = Client(SID, AUTH)
    message = client.messages.create(
        body=f'😶‍🌫️ {name} ALERT 🔴📉 \n LTP:{ltp} \n CP: {inv}\nChange:-{((inv-ltp)/inv)*100}%',
        from_="FROMPHONE",
        to="TOPHONE"
    )

n=current_price[0]['NABIL']
ntc=current_price[1]['NTC']
ct=current_price[2]['CITY']
kbl=current_price[3]['KBL']
if n> 520:
    bull('NABIL',n,520)
else:
    bear('NABIL',n,520)

if ntc>820:
    bull('NTC',ntc,820)
else:
    bear('NTC',ntc,820)

if kbl>220:
    bull('KBL',kbl,220)
else:
    bear('KBL',kbl,220)
if ct>415:
    bull('CITY',ct,415)
else:
    bear('CITY',ct,415)
