from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
word_dict = {}
try:
    pd = pandas.read_csv("data/known_words.csv")
except FileNotFoundError:
    orignal_data = pandas.read_csv("data/Hindi to English.csv")
    word_dict = orignal_data.to_dict(orient="records")
else:
    word_dict = pd.to_dict(orient="records")



def next_card():
    global current_card,flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas.itemconfig(title_text,text="Hindi")
    canvas.itemconfig(word_text,text = current_card["Hindi"])
    screen.after(3000, flip_card)
def flip_card():
    canvas.itemconfig(title_text,text="English",fill= "white")
    canvas.itemconfig(word_text,text = current_card["English"],fill = "white")
    canvas.itemconfig(canvas_image,image = back_image)

def known_word():
    word_dict.remove(current_card)
    print(len(word_dict ))
    data = pandas.DataFrame(word_dict)
    data.to_csv("data/known_words.csv",index=False)

    next_card()



screen = Tk()
screen.title("Language Card")
screen.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = screen.after(3000, flip_card)


#----------------------canvas-------------------------
canvas = Canvas(width=800,height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400,263,image= front_image)
canvas.config(background=BACKGROUND_COLOR,highlightthickness=0)
title_text = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"),fill="black")
word_text = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"),fill="black")
canvas.grid(row = 0,column = 1,columnspan = 2)
next_card()
#-------------------------------button--------------------
cross_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

cross_button = Button(image=cross_image,highlightthickness=0,background=BACKGROUND_COLOR,command=next_card)
cross_button.grid(row=1,column = 1)

right_button = Button(image=right_image,background=BACKGROUND_COLOR,highlightthickness=0,command=known_word)
right_button.grid(row=1,column = 2)
screen.mainloop()

