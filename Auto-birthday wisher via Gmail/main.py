import pandas,smtplib,datetime,random
today=datetime.datetime.now()
today_tuple=(today.month,today.day)


my_email='achaulagain295@gmail.com'
pasw='jhio ocam qeje ttpv'
data=pandas.read_csv('birthdays.csv')
# print(data)
# dict=data.to_dict(orient='records')
bday_dict={(data_row.month,data_row.day):data_row for(index,data_row) in data.iterrows()}
if today_tuple in bday_dict:
    birthday_person=bday_dict[today_tuple]
    file_path=f'templates/letter_{random.randint(1,3)}.txt'
    with open(file_path)as file:
        contents=file.read()
        contents= contents.replace('[NAME]',birthday_person['name'])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email,password=pasw)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person['email'],msg=f'Subject: Happy Birthday! \n\n {contents}')








