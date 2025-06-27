from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    global passwordInput
    passwordInput.delete(0,END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for _  in range(nr_letters)]

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    passwordInput.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def saveData():
    webName = websiteInput.get()
    userName = userNameInput.get()
    passName = passwordInput.get()
    new_data = {webName:{"email":userName,"password":passName}}
    if len(webName) == 0 or len(userName) == 0 or len(passName) == 0 :
        messagebox.showwarning(title="Warning",message="Please fill out Empty Fields!!")
    else:  
        messagebox.showinfo(title="Success",message="Data Added Successfully")

        try:
            with open("data.json","r") as dataFile:
                data = json.load(dataFile)
                data.update(new_data)


        except FileNotFoundError:
            with open("data.json","w") as dataFile:
                json.dump(new_data,dataFile,indent=4)


        else:
            with open("data.json","w") as dataFile:
                json.dump(data,dataFile,indent=4)
                 
        finally:
            websiteInput.delete(0,END) 
            passwordInput.delete(0,END)


# ---------------------------- Searching Logic ------------------------ #

def Search():
    try:
        with open("data.json","r") as dataFile:
            data = json.load(dataFile)
    except FileNotFoundError:
        messagebox.showwarning(title="Error",message="Data file doesn't Exist")
    else:
        searchedElement = websiteInput.get()
        if searchedElement in data:
            messagebox.showinfo(title="Your Info",message=f"{data[searchedElement]}")
        else:
            messagebox.showwarning(title="Not Found",message="No information Exists for Inserted Website")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30,pady=30)


canvas = Canvas(height=200,width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)


websiteLabel = Label(text="Website:")
websiteLabel.grid(column=0,row=1)
userNameLabel = Label(text="Username/Email:")
userNameLabel.grid(column=0,row=2)
passwordLabel = Label(text="Password:")
passwordLabel.grid(column=0,row=3)


websiteInput = Entry(width=21)
websiteInput.focus()
websiteInput.grid(column=1,row=1)


searchButton = Button(text="Search",width=10,command=Search)
searchButton.grid(column=2,row=1)

userNameInput = Entry(width=35)
userNameInput.grid(column=1,row=2,columnspan=2)

passwordInput = Entry(width=21)
passwordInput.grid(column=1,row=3)


genPassButton = Button(text="Generate Password",command=generate_password)
genPassButton.grid(column=2,row=3)

addButton = Button(text="Add",width=35,command=saveData)
addButton.grid(column=1,row=4,columnspan=2)


window.mainloop()