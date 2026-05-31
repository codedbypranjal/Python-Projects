from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- BROWSING PASSWORD ------------------------------- #
def search():
    web=input1.get()
    try:
        file=open("new_json.json",'r')
    except FileNotFoundError:
        messagebox.showinfo(title='Error',message='No Data Found')
    else:
        data=json.load(file)
        if web in data:
            email=data[web]['Userid']
            pasw=data[web]['Password']
            messagebox.showinfo(title='Your Password',message=f'{email}\n {pasw}')
        else:
            messagebox.showinfo(title="Error",message="No data found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import choice,randint,shuffle
def pass_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    pass_letters=[choice(letters) for _ in range(randint(8, 10))]
    pass_numbers=[choice(numbers) for _ in range(randint(2, 4))]
    pass_symbols=[choice(symbols) for _ in range(randint(2, 4))]

    password_list=pass_letters+pass_symbols+pass_numbers
    shuffle(password_list)

    password=''.join(password_list)
    input3.insert(0,password)
# ---------------------------- SAVE PASSWORD ----------\--------------------- #
def save_data():
    web=input1.get()
    id=input2.get()
    pp=input3.get()
    new_dict={
         web:{
                'Userid':id,
                'Password':pp
         }

    }
    if len(web)==0 or len(pp)==0:
        messagebox.showinfo(title="Error",message='Please dont leave empty fields')
    else:
        correct=messagebox.askokcancel(title=input1.get(),message=f"(Is it correct?\n Website:{web}\n Userid:{id}\n Password:{pp})")
        if correct:
            try:
                with open('new_json.json','r') as file:
                    content=json.load(file)
                    content.update(new_dict)
            except (FileNotFoundError, json.JSONDecodeError):
                with open('new_json.json','w') as file:
                    json.dump(new_dict,file,indent=4)
            else:
                with open('new_json.json','w') as file:
                    json.dump(content,file,indent=4)
            input1.delete(0,END)
            input3.delete(0,END)
            input1.focus()
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)



canvas=Canvas(width=200,height=200)
img=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

label1=Label(text='Website:',font=('arial',11))
label1.grid(column=0,row=1)
input1=Entry(width=22)
input1.grid(column=1,row=1)
input1.focus()

label2=Label(text='Email/Username:',font=('arial',11))
label2.grid(column=0,row=2)
input2=Entry(width=40)
input2.grid(column=1,row=2,columnspan=2)
input2.insert(0,'pranjalsapkota99@gmail.com')

label3=Label(text='Password:',font=('arial',11))
label3.grid(column=0,row=3)
input3=Entry(width=22)
input3.grid(column=1,row=3)


button1=Button(text='Generate Password',command=pass_gen)
button1.grid(column=2,row=3)

button2=Button(text='Add',width=36,command=save_data)
button2.grid(column=1,row=4,columnspan=2)

button3=Button(text='Search',command=search)
button3.grid(column=2,row=1)
window.mainloop()