import tkinter
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers+ password_letters+ password_symbols
    shuffle(password_list)
    password = "".join(password_list)
    entry3.insert(0,password)
    pyperclip.copy(password) #COPIES PASSWORD TO CLIPBOARD!!

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Make sure your fields are not empty")
    else:
        is_ok = messagebox.askokcancel(title= website ,message=f"These are the details entered: \nEmail: {email} \n Password: {password} \n Is it ok to save?" )
        if is_ok:
            try:
                with open("data.json", "r") as f:
                    # Reading old data
                    data = json.load(f)

            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data,f,indent=4 )
            else:
                # Updating old data with mew data
                data.update(new_data)
                with open("data.json", "w") as f:
                    #Saving updated data
                    json.dump(data,f, indent=4)
            finally:
                entry1.delete(0,END)
                entry2.delete(0,END)
                entry3.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = entry1.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
            if website in data:
                email = data[website]["email"]
                password= data[website]["password"]
                messagebox.showinfo(title= website, message= f"email: {email}\nPassword:{password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_png)
canvas.grid(row=0,column=1)

weblab = tkinter.Label(text="Website")
weblab.grid(row=1,column=0)

email_lab = tkinter.Label(text="Email/Username: ")
email_lab.grid(row=2, column = 0)

pass_lab = tkinter.Label(text="Password: ")
pass_lab.grid(row =3, column=0)

entry1 = Entry(width=21)
entry1.focus()
entry1.grid(row=1, column=1, columnspan=1, sticky=EW)

entry2 = Entry(width=35)
entry2.grid(row=2, column=1, columnspan=2, sticky=EW)

entry3 = Entry(width=21)
entry3.grid(row=3, column=1, sticky=EW)

button1 = Button(text="Generate Password",command=generate_password, bg='LIGHT GREEN')
button1.grid(row=3, column=2, sticky=EW)

button2 = Button(text="Add",width=36, command=save,bg='orange')
button2.grid(row=4, column = 1, columnspan=2, sticky=EW)

search_button = Button(text="Search",bg='sky BLUE', command=find_password)
search_button.grid(row=1, column=2, columnspan=1,sticky=EW, padx= 2, pady=0)

window.mainloop()
