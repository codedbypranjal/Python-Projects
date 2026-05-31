import datetime,random,smtplib
from calendar import weekday
from dotenv import load_dotenv
import os

now=datetime.datetime.now()
today=now.weekday()
load_dotenv(verbose=True)
if now.weekday()==6:
    my_email=os.getenv("GMAIL_EMAIL")
    passw=os.getenv("GMAIL_PASS")
    file=open('quotes.txt','r')
    data=file.readlines()  #reads and stores in a list where each line in file=each element of list
    chosen=[quote for quote in data]
    selected=random.choice(data)
    file.close()
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=passw)
        connection.sendmail(from_addr=my_email,to_addrs='pranjalsapkota66@gmail.com',msg=f'(Subject:Monday Motivation\n\n{selected})')
