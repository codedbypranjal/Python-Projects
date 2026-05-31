from tkinter import * # ---------------------------- CONSTANTS ------------------------------- #


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def pause():
    window.after_cancel(timer)
    label1.config(text="Timer")
    canvas.itemconfig(timer_text,text='00:00')
    check.config(text='')
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- #
import math
def start_timer():
    global reps
    reps += 1  # increment first

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        label1.config(text='Long Break', fg=RED)
        count_down(long_break_sec)
        # Short break on 2, 4, 6
    elif reps % 2 == 0:
        label1.config(text='Short Break', fg=GREEN)
        count_down(short_break_sec)
        # Work on 1, 3, 5, 7
    else:
        label1.config(text='Study', fg='red')
        count_down(work_sec)

def count_down(count):
    global reps
    min=math.floor(count/60)
    sec=count%60
    if sec <10:
        sec=f"0{sec}"
    if min<10:
        min=f'0{min}'

    canvas.itemconfig(timer_text,text=f'{min}:{sec}')
    if count>=0:
        global timer
        timer=window.after(1000,count_down,count-1) #after every sec, count_down fn gets called with count-1
    else:
        start_timer()
        if reps%2==0:
            work_sessions=math.floor(reps/2) #no. of work sessions
            marks='✔️'*work_sessions           #tick * no. of work sessions
            check.config(text=marks)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=80,bg=YELLOW)


label1=Label(text='Timer',fg=GREEN,font=(FONT_NAME,35,"bold"),bg=YELLOW)
label1.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
img=PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=img)

timer_text=canvas.create_text( 103,130, fill="white",font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)


button1=Button(text="Start",command=start_timer)
button1.grid(column=0,row=2)

button2=Button(text="Reset",command=pause)
button2.grid(column=2,row=2)

check = Label( fg="green", font=("Arial", 15),bg=YELLOW)
check.grid(column=1,row=2)

window.mainloop()