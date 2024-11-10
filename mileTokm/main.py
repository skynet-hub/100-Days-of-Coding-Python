from tkinter import *

def calculate_km():
    input_distance = float(distance_miles.get())
    results = round(input_distance * 1.609, 2)
    label4.config(text=f"{results}")
    

screen = Tk()
screen.minsize(width=350, height=200)
screen.title("Miles to Km program")
screen.config(padx=50, pady=50)


distance_miles = Entry()
distance_miles.grid(column=1, row=0)
distance_miles.config(width=7)
distance_miles.focus()


label2 = Label(text="Miles")
label2.grid(column=2, row=0)
label2.config(padx=10)

label3 = Label(text="is equal to")
label3.grid(column=0, row=1)
label3.config(pady=10)

label4 = Label(text="0")
label4.grid(column=1, row=1)
label4.config(pady=10)

label5 = Label(text="Km")
label5.grid(column=2, row=1)

calculate_b = Button(text="Calculate", command=calculate_km)
calculate_b.grid(row=2, column=1)





















screen.mainloop()
