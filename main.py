from tkinter import *
from tkinter import messagebox
import random






# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_letters=[random.choice(letters) for _ in range(0,nr_letters-1)]
    password_symbols=[random.choice(symbols) for _ in range(0,nr_symbols-1)]
    password_numbers=[random.choice(numbers) for _ in range(0,nr_numbers-1)]

    password_list = password_numbers+password_symbols+password_letters

    random.shuffle(password_list)




    generated_password="".join(password_list)
    password_enter.insert(0, f"{generated_password}")


    # print(f"Your password is: {generated_password}")





# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    websites=website_enter.get()
    emails=email_enter.get()
    passwords=password_enter.get()
    if websites=="" or passwords=="" or email=="":
        opps=messagebox.showinfo(title="oops", message="Please don't leave any field empty")

    else:
        is_ok= messagebox.askokcancel(title=websites, message=f"These are the details received\n Email:{emails}\n Password: {passwords}\n Is it okay to save this?")
        if is_ok:
            with open("Data.txt", mode="a") as file:
                file.write(f"{website_enter.get()} | {email_enter.get()} | {password_enter.get()}")
                file.write("\n")
            website_enter.delete(0, 'end')
            password_enter.delete(0, 'end')

        else:
            password_enter.delete(0, 'end')
            password.focus()











# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.config(padx=50, pady=50)
window.title("Password Generator")
canvas=Canvas(width=200, height=200)
canvas.grid(row=0, column=1)

image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)

website=Label(text="Website:", font=("Arial", 10, "normal"))
website.grid(row=1, column=0)
email=Label(text="Email/Username:", font=("Arial", 10, "normal"))
email.grid(row=2, column=0)
password=Label(text="Password:", font=("Arial", 10, "normal"))
password.grid(row=3, column=0)


website_enter=Entry(width=35 )
website_enter.grid(row=1, column=1, columnspan=2, sticky="w")
website_enter.focus()

email_enter=Entry(width=35 )
email_enter.grid(row=2, column=1, columnspan=2, sticky="w")
email_enter.insert(0, "j.b@gmail.com")

password_enter=Entry(width=35 )
password_enter.grid(row=3, column=1, sticky="w")

generate_password=Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)






add=Button(text="Add", width=36, command=save)
add.grid(row=4, column=1, columnspan=2)






window.mainloop()