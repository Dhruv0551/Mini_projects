import pandas as pd
from tkinter import *
import random


BACKGROUND_COLOR = "#B1DDC6"
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/japanese_words.csv")
# ------------ OnClick Logic ------------------

toLearn = data.to_dict(orient="records")

wordList = list(data["Japanese"])
currentWord = ""

def next_word():
    global currentWord
    currentWord = random.choice(toLearn)
    canvas.itemconfig(currentImg,image=cardFront)
    canvas.itemconfig(text,text=currentWord["Japanese"],font=("Arial",40,"bold"),fill=BACKGROUND_COLOR)
    canvas.itemconfig(title,text="Japanese",font=("Arial",60,"bold"),fill=BACKGROUND_COLOR)
    window.after(3000,flip_card)


def flip_card():
    canvas.itemconfig(currentImg,image=cardBack)
    canvas.itemconfig(title,text="English",font=("Arial",40,"bold"),fill="white")
    canvas.itemconfig(text,text=currentWord["English"],font=("Arial",60,"bold"),fill="white")

def learnedWord():
    toLearn.remove(currentWord)
    data = pd.DataFrame(toLearn)
    data.to_csv("data/words_to_learn.csv")
    next_word()


# ------------ designing UI -------------------
window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.title("Flash Card")


canvas = Canvas()
canvas.config(width=800,height=530,highlightthickness=0,bg=BACKGROUND_COLOR)
cardFront = PhotoImage(file="images/card_front.png")
cardBack = PhotoImage(file="images/card_back.png")
currentImg = canvas.create_image(400,270,image=cardFront)
title = canvas.create_text(
    390, 130,
    text="",
    font=("Arial", 35),
    fill="black"
)

text = canvas.create_text(
    390, 263,
    text="",
    font=("Arial", 60,"bold"),
    fill="black"
)
canvas.grid(column=0,row=0,columnspan=2)

rightImg = PhotoImage(file="images/right.png")
right_button = Button(image=rightImg, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0,command=learnedWord)
right_button.grid(column=1, row=1)

wrongImg = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrongImg, highlightthickness=0, bg=BACKGROUND_COLOR, bd=0,command=next_word)
wrong_button.grid(column=0, row=1)
next_word()
# window.after(3000,flip_card)
window.mainloop()



