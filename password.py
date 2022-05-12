from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letter_pw = [password_list.append(random.choice(letters)) for char in range(nr_letters)]
    symbols_pw = [password_list.append(random.choice(symbols)) for char in range(nr_symbols)]
    numbers_pw = [password_list.append(random.choice(numbers)) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    p_entry.delete(0, END)
    p_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = w_entry.get().upper()
    email = e_entry.get()
    password = p_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        empty = messagebox.showinfo(title="oops", message="Please dont leave any fields empty!")
        
    else:
        try:
            with open("A:/fileali/Coding/Python Projects/Password Manager/password.json", "r") as password:
                data = json.load(password)
        except FileNotFoundError:
            with open("A:/fileali/Coding/Python Projects/Password Manager/password.json", "w") as password:
                json.dump(new_data, password, indent=4)
        else:
            data.update(new_data)
            with open("A:/fileali/Coding/Python Projects/Password Manager/password.json", "w") as password:
                json.dump(data, password, indent=4)
        finally:
            w_entry.delete(0, END)
            p_entry.delete(0, END)
            w_entry.focus()
# ---------------------------- SEARCH ------------------------------- #
def search():
    website = w_entry.get().upper()
    try:
        with open("A:/fileali/Coding/Python Projects/Password Manager/password.json", "r") as password:
            data = json.load(password)
            if website not in data:
                messagebox.showinfo(title="Oops", message=f"Details for {website} doesn't exist")
            else:
                for i in data:
                    key = data[i]
                    if website == i:
                        messagebox.showinfo(title=website, message=f'Email: {key["email"]}\nPassword: {key["password"]}')
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="You havent entered any info yet!")
    
    finally:
        w_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=80, pady=50, bg='white')
window.bind("<Return>", lambda event:save_password())

canvas = Canvas(width=240, height=240, bg='white', highlightthickness=0)

lock = PhotoImage(file="A:/fileali/Coding/Python Projects/Password Manager/logo.png")

#IMAGE
canvas.create_image(120, 120, image=lock)
canvas.grid(column=1, row=0)

#WEBSITE
website = Label(text='Website: ', bg='white')
website.grid(column=0, row=1)

#Website Entry
w_entry = Entry(width=35)
w_entry.grid(column=1, row=1)
w_entry.focus()

#Search
search = Button(text="Search", width=30, command=search)
search.grid(column=1, row=2, pady=5)

#Email
email = Label(text="Email/Username: ", bg="white")
email.grid(column=0, row=3)

#Email Entry
e_entry = Entry(width=35)
e_entry.grid(column=1, row=3)
e_entry.insert(0, "a.fikri2411@gmail.com")

#Password
password = Label(text="Password: ", bg='white')
password.grid(column=0, row=4)

#Password entry
p_entry = Entry(width=35)
p_entry.grid(column=1, row=4)

#Generate Password
gen_pass = Button(text="Generate Password", width=30, command=generate_password)
gen_pass.grid(column=1, row=5, pady=5)

#ADD
add = Button(text="Add", width=30, command=save_password)
add.grid(column=1, row=6)

window.mainloop()