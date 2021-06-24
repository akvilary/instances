import tkinter
import pandas
import random


#Variabels
BACKGROUND_COLOR = "#B1DDC6"
learning_language = "French"
native_language = "English"
FONT_of_language = ("Arial", 30,"italic")
FONT_of_learning_word = ("Arial", 40,"bold")

frenchword = None
englishword = None
flip_timer = None

#------------------------------FUNCTIONS--------------------------------------#
def flip_back():
    canva.itemconfig(canva_image, image=card_back_img)
    canva.itemconfig(word_title, text=current_card[native_language], fill="white")
    canva.itemconfig(language_title, text=native_language, fill="white")

def flip_front():
    canva.itemconfig(canva_image, image=card_front_img)
    canva.itemconfig(word_title, text=current_card[learning_language], fill="black")
    canva.itemconfig(language_title, text=learning_language, fill="black")

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    if len(learnsheet) == 0:
        current_card = {
            'French': '0 words to learn',
            'English': '0 words to learn'
        }
        canva.itemconfig(language_title, text="Congratulations!", fill="black")
        canva.itemconfig(word_title, text="0 words to learn", fill="black")
    else:
        current_card = random.choice(learndict)
        flip_front()
        flip_timer = window.after(3000, func=flip_back)



def remove_card():
    learndict.remove(current_card)
    words_to_learn = pandas.DataFrame(learndict)
    words_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

#------------------------------READ DATA--------------------------------------#
try:
    learnsheet = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    learnsheet = pandas.read_csv("./data/french_words.csv")

learndict = learnsheet.to_dict(orient="records")

#------------------------------SET UP-----------------------------------------#
#Установка окна
window = tkinter.Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, width=900, height=600, bg=BACKGROUND_COLOR)

#Card set up
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
card_back_img = tkinter.PhotoImage(file="./images/card_back.png")

canva = tkinter.Canvas(width=600, height=396, highlightthickness=0, bg=BACKGROUND_COLOR)
canva_image = canva.create_image(300, 198, image=card_front_img)
canva.grid(column=0, row=0, columnspan=2, rowspan=2)

#Text set up
language_title = canva.create_text(300,100, text=learning_language, fill="black", font=FONT_of_language)
word_title = canva.create_text(300,210, text=frenchword, fill="black", font=FONT_of_learning_word)
flip_timer = window.after(3000, func=flip_back)

#Buttons set up
wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=2, pady=30)

right_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_image, highlightthickness=0, command=remove_card)
right_button.grid(column=1, row=2, pady=30)

front_image = tkinter.PhotoImage(file="./images/fr.png")
front_button = tkinter.Button(image=front_image, highlightthickness=0, command=flip_front)
front_button.grid(column=2, row=0, padx=30, pady=10)

back_image = tkinter.PhotoImage(file="./images/uk.png")
back_button = tkinter.Button(image=back_image, highlightthickness=0, command=flip_back)
back_button.grid(column=2, row=1, padx=30, pady=10)

next_card()

window.mainloop()