#Password generator function
import random
from tkinter import *
from tkinter import messagebox

character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"

def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except:
        messagebox.showerror("Error", "Please enter valid numbers")
        return

    if repeat == 0:
        if length > len(character_string):
            messagebox.showerror("Error", "Length too long without repetition")
            return
        password = random.sample(character_string, length)
    else:
        password = random.choices(character_string, k=length)

    password = ''.join(password)
    password_v.set("Created password: " + password)

# Tkinter UI
root = Tk()
root.geometry("350x200")

repeat_entry = Entry(root)
repeat_entry.pack()

length_entry = Entry(root)
length_entry.pack()

password_v = StringVar()
password_label = Entry(root, textvariable=password_v, state="readonly", width=40)
password_label.pack()

Button(root, text="Generate", command=generate_password).pack()

root.mainloop()
