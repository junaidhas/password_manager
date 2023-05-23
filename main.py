from tkinter import *
from tkinter import messagebox
import random

# --------------------------------Constants ------------------------------------#

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#95cd41"
YELLOW = "#f7f5dd"
DARKBLUE = "#16697a"
GOLD = "#ffd95a"
BROWN = "#C07F00"
FONT_NAME = "Cambria"

# -------------------------------saving pwd data in a txt file ------------------#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title="error", message="Don't leave any field empty")

    else:
        is_ok = messagebox.askokcancel(title=f"{website}",message=f"username/email: {email} \n password: {password}" )

        if is_ok:
            with open("data.txt","a") as f:
                f.write(f"{website}--{email}--{password}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)

#--------------------------------Generate password------------------------------#
def generate_password():
    pass
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= random.randint(6,8)
    nr_symbols = 1
    nr_numbers = random.randint(2,3)

    print(f"nr_numbers:{nr_numbers},nr_symbols:{nr_symbols},nr_letters:{nr_letters}")


    randomletter=random.choices(letters ,k=nr_letters)
    randomSymbol=random.choices(symbols, k=nr_symbols)
    randomNumber=random.choices(numbers,k=nr_numbers)
    password_list=[]
    password_list =randomletter + randomSymbol + randomNumber
    print(f"{password_list}")
    #Don't use random.shuffle (getting some error), use random.sample
    shuffledPassword=random.sample(password_list, len(password_list))
    print(f"{shuffledPassword}")

    password ="".join(shuffledPassword)
    password_entry.insert(0,string=password)





# ------------------------------- UI setup -------------------------------------#
#TODO create window
window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40,bg=YELLOW)

#TODO create labels, entries and buttons

website_label = Label(text="Website",bg=YELLOW)
website_label.grid(row=1,column=0)

website_entry = Entry(width=35)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username",bg=YELLOW)
email_label.grid(row=2,column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(index=0,string="junaidhb@gmail.com")

password_label = Label(text="Password",bg=YELLOW)
password_label.grid(row=3,column=0)

password_entry = Entry(width=24)
password_entry.grid(row=3,column=1)

generate_pwd = Button(text="Generate Password",command=generate_password)
generate_pwd.grid(row=3,column=2)

add_button = Button(text="ADD",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)




#TODO Create canvas and place the image on canvas
canvas = Canvas(width= 256, height= 256)
lock_img =PhotoImage(file= "password-lock.png")
canvas.create_image(0,0,image = lock_img, anchor ='nw')
canvas.grid(row=0,column=1)



window.mainloop()
