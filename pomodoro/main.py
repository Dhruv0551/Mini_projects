from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():
    count_down(5*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    countMin = math.floor(count/60)
    countSec = count % 60
    canvas.itemconfig(timerText,text=f"{countMin}:{countSec}")
    if count > 0:
        window.after(1000,count_down,count-1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

timerLabel = Label(text="Timer",font=(FONT_NAME,40,"bold"),fg=GREEN,bg=YELLOW)
timerLabel.grid(column=1,row=0)

canvas = Canvas(width=200, height=224,bg=YELLOW,highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomatoImg)
timerText = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

stButton = Button(text="Start",bg=GREEN,fg=YELLOW,width=10,font=(FONT_NAME,13,"bold"),highlightthickness=0,command=timer_start)
stButton.grid(column=0,row=2)

CheckMarkLabel = Label(text="✔️",bg=YELLOW,fg=GREEN,font=(20))
CheckMarkLabel.grid(column=1,row=3)

rtButton = Button(text="Reset",bg=GREEN,fg=YELLOW,width=10,font=(FONT_NAME,13,"bold"),highlightthickness=0)
rtButton.grid(column=2,row=2)

window.mainloop()