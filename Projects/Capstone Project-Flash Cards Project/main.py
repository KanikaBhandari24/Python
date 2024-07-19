from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current={}
to_learn={}

try:
    data=pandas.read_csv("Capstone Project-Flash Cards/data/words_toLearn")
except:
    original=pandas.read_csv("Capstone Project-Flash Cards/data/words.csv")
    to_learn=original.to_dict(orient="records")
else:
    dict=data.to_dict(orient="records")

def card():
    global current, timer
    window.after_cancel(timer)
    current=random.choice(dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current["French"], fill="black")
    canvas.itemconfig(background, image=img) 
    timer=window.after(3000, func=flip)

def flip():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current["English"], fill="white") 
    canvas.itemconfig(background, image=img2)

def is_known():
        dict.remove(current)
        data=pandas.DataFrame(dict)
        data.to_csv("Capstone Project-Flash Cards/data/words_toLearn")
        card()

#*************************************************** UI SETUP ****************************************************
window=Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer=window.after(3000, func=flip)
#CANVAS SETUP
canvas=Canvas(width=800, height=526)
img=PhotoImage(file="/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Capstone Project-Flash Cards/images/front.png")
img2=PhotoImage(file="/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Capstone Project-Flash Cards/images/back.png")
background=canvas.create_image(400, 263, image=img)

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title=canvas.create_text(400, 150, text="Title", font=("Courier", 35, "bold"))
card_word=canvas.create_text(400, 263, text="Meaning", font=("Courier", 35, "bold")) 
canvas.grid(column=0, row=0, columnspan=2)
#BUTTONS SETUP
wrong=PhotoImage(file="/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Capstone Project-Flash Cards/images/wrong.png")
b1=Button(image=wrong, highlightthickness=0, command=card)
b1.grid(column=0, row=1)
right=PhotoImage(file="/Users/Kanika Bhandari/OneDrive/Desktop/PYTHON/Capstone Project-Flash Cards/images/right.png")
b2=Button(image=right, highlightthickness=0, command=is_known)
b2.grid(column=1, row=1)
card()

window.mainloop()