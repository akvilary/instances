import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

password_status = 0

fields_data = None
website = None

def get_fields():
    global fields_data
    global website

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    fields_data = {website: {
        'e-mail' : email,
        'password' : password,
    }}

# ---------------------------- SEARCH MECHANISM ---------------------------- #
def search():
    try:
        get_fields()

        if len(website) > 0:
            with open("data.json", mode='r') as data_file:
                #Reading old data
                data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Ooops", message="There is no any record! Add a record at first, please.")

    else:
        if website in data.keys():
            pyperclip.copy(data[website]['password'])
            messagebox.showinfo(title=website,
                                message=f"E-mail: {data[website]['e-mail']}\n"
                                        f"Password: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Ooops", message=f"No details for {website} exists.")


# ---------------------------- SHOW PASSWORD ------------------------------- #
def show_hide_password():
    global password_status
    if password_status == 0:
        password_input.config(show="")
        password_status += 1
    elif password_status == 1:
        password_input.config(show="*")
        password_status -= 1
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def create_password():
    password_input.delete(0, tkinter.END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    get_fields()

    if len(website) == 0 or len(fields_data[website]['e-mail']) == 0 or len(fields_data[website]['password']) == 0:
        messagebox.showwarning(title="Ooops", message="Please, don't leave any fields empty!")
    else:
        try:
            with open("data.json", mode='r') as data_file:
                #Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode='w') as data_file:
                #Saving_data
                json.dump(fields_data, data_file, indent=4)

        else:
            #Updating old data with new data
            data.update(fields_data)

            with open("data.json", mode='w') as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, tkinter.END)
            password_input.delete(0, tkinter.END)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canva = tkinter.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tkinter.PhotoImage(file="logo.png")
canva.create_image(100, 100, image=lock_img)
canva.grid(column=1, row=0)

website_title = tkinter.Label(text="Website:")
website_title.config(padx=5, pady=5)
website_title.grid(column=0, row=1)

website_input = tkinter.Entry(width=30)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=1)

search_button = tkinter.Button(text="Search", width=17, command=search)
search_button.grid(column=2, row=1, columnspan=2)


email_title = tkinter.Label(text="E-mail/Username:")
email_title.config(padx=5, pady=5)
email_title.grid(column=0, row=2)

email_input = tkinter.Entry(width=50)
email_input.insert(0, "a.mathgame.s@gmail.com")
email_input.grid(column=1, row=2, columnspan=3)


password_title = tkinter.Label(text="Password:")
password_title.config(padx=5, pady=5)
password_title.grid(column=0, row=3)

password_input = tkinter.Entry(width=30, show="*")
password_input.grid(column=1, row=3)

show_password_button = tkinter.Button(text="👁️", command=show_hide_password)
show_password_button.grid(column=2, row=3)

new_password_button = tkinter.Button(text="New password", command=create_password)
new_password_button.grid(column=3, row=3)

add_password_button = tkinter.Button(text="Add", width=43, command=save_password)
add_password_button.grid(column=1, row=4, columnspan=3)

window.mainloop()
