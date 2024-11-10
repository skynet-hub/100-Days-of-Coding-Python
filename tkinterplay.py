from tkinter import *

window = Tk()
window.minsize(width=400, height=400)
window.title("First Gui program")
window.config(padx=20, pady=20)


def clicked_button():
    my_label.config(text=input.get())

my_label = Label(text="Hello World", font=('Arial', 12, 'bold'))
my_label.grid(column=0, row=0)    

input = Entry(width=10)
input.grid(column=3, row=2)

button = Button()
button.config(text="click me", command=clicked_button)
button.grid(column=1, row=1)

button = Button()
button.config(text="New button")
button.grid(column=2, row=0)




















window.mainloop()


