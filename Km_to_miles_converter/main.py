from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Km to mile converter")
window.minsize(width=200, height=200)
window.config(padx=20,pady=30)

def action():
    #Gets text in entry
    km = entry1.get()
    #Calculate
    miles = round(float(km) / 1.609, 1)
    if miles % 1 == 0:
        miles = int(miles)
    label3.config(text=miles)

#Variables
miles = 0

#Labels
label1 = Label(text="is equal to")
label1.grid(column=0,row=1)
label1.config(padx=10,pady=10)

label2 = Label(text="Km")
label2.grid(column=2,row=0)
label2.config(padx=10,pady=10)

label2 = Label(text="Miles")
label2.grid(column=2,row=1)
label2.config(padx=10,pady=10)

label3 = Label(text=miles)
label3.grid(column=1,row=1)

#Entries
entry1 = Entry(width=30)
#Add some text to begin with
entry1.insert(END, string="0")
entry1.grid(column=1,row=0)

#Button
button1 = Button(text="Calculate", command=action)
button1.grid(column=1, row=2)
button1.config(padx=10,pady=10)





window.mainloop()