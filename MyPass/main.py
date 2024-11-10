from  tkinter import *
from tkinter import messagebox 
from random import randint, choice, shuffle
#import pyperclip  will install the module when I have wifi
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list.extend([choice(symbols) for char in range(randint(2, 4))])
    password_list.extend([choice(numbers) for char in range(randint(2, 4))])

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)   
    #pyperclip.copy(password) 

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
        website = web_entry.get()
        email = user_entry.get()
        password = pass_entry.get()
        new_data = {
              website: {
                    "email": email,
                    "password": password
              }
        }

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oooops!", message="Make sure you have not left any fields empty")
        else:
            try:
                with open("./data.json", mode='r') as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("./data.json", mode='w') as data_file:
                    json.dump(new_data, data_file, indent=4)    
            else:
                data.update(new_data) 
                with open("./data.json", mode='w') as data_file:
                    json.dump(data, data_file, indent=4)

            finally:        
                web_entry.delete(0, END)
                pass_entry.delete(0, END)
                web_entry.focus()

#----------------------------- search data -----------------------------#

def find_password():
    website =  web_entry.get()

    try:
        with open("./data.json", mode='r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found.")        
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

        else:
            messagebox.showinfo(title="Error", message=f"No details of {website} exists")    
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas()
canvas.config(width=200, height=200)
image = PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

web_label = Label(text='Website:')
web_label.config(padx=60)
web_label.grid(column=0, row=1)

user_label = Label(text='Email/Username:')
user_label.grid(column=0, row=2)

user_entry = Entry(width=35)
user_entry.insert(0, "davidlesaomako@gmail.com")
user_entry.grid(column=1, row=2, columnspan=2, pady=10)

pass_Label = Label(text='Password:')
pass_Label.grid(column=0, row=3)

pass_entry = Entry(width=35)
pass_entry.grid(column=1, row=3, columnspan=2)


web_entry = Entry(width=28)
web_entry.focus()
web_entry.grid(column=1, row=1)

generate_btn = Button(text='Generate Password', command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=36, command=save_pass)
add_btn.grid(column=1, row=4, columnspan=2, pady=10)

search_button = Button(text="Search",  width=13,command=find_password)
search_button.grid(row=1, column=2)



window.mainloop()