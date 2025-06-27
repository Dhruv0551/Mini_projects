from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

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
    if len(webName) == 0 or len(userName) == 0 or len(passName) == 0 :
        messagebox.showwarning(title="Warning",message="Please fill out Empty Fields!!")
    else:
        isok = messagebox.askokcancel(title=webName, message=f"These are the Details You entered: \nEmail: {userName}\nPassword: {passName}\n Do you want to Save?")
        if isok:
            messagebox.showinfo(title="Success",message="Data Added Successfully")
            with open("data.txt","a") as saveFile:
                saveFile.write(f"{webName} | {userName} | {passName}\n")
                websiteInput.delete(0,END) 
                passwordInput.delete(0,END) 

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


websiteInput = Entry(width=35)
websiteInput.focus()
websiteInput.grid(column=1,row=1,columnspan=2)

userNameInput = Entry(width=35)
userNameInput.grid(column=1,row=2,columnspan=2)

passwordInput = Entry(width=21)
passwordInput.grid(column=1,row=3)


genPassButton = Button(text="Generate Password",command=generate_password)
genPassButton.grid(column=2,row=3)

addButton = Button(text="Add",width=35,command=saveData)
addButton.grid(column=1,row=4,columnspan=2)



window.mainloop()