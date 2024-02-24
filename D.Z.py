from tkinter import *
from tkinter import messagebox
import random
secret_number_global=None
attempts = 0
def generate_number():
    global secret_number_global
    global attempts
    attempts = 0
    min_val=min_entry.get()
    max_val = max_entry.get()
    if min_val.isdigit() and max_val.isdigit():
        min_val=int(min_val)
        max_val=int(max_val)
        secret_number=random.randint(min_val, max_val)
        result.config(text="", fg="black")  # Set text color to black
        secret_number_global = secret_number
        root.title("Вгадай число - Спроби: 0")
        min_entry.config(state="disabled")
        max_entry.config(state="disabled")
    else:
        result.config(text="Введіть коректні значення!", fg="red")  # Set text color to red

root = Tk()
root.title("Вгадай число - Спроби: 0")
root.configure(bg='green')  # Set background color to light grey
Label(root, text="Мінімальне значення:", fg="green",background='red',).grid(row=0, column=0)  # Set text color to black
Label(root, text="Максимальне значення:", fg="black",background='blue',).grid(row=1, column=0)  # Set text color to black
min_entry = Entry(root)
max_entry = Entry(root)
min_entry.grid(row=0, column=1)
max_entry.grid(row=1, column=1)
generate_button = Button(root, text="Генерувати", fg='blue', background='yellow', command=generate_number)
generate_button.grid(row=2, columnspan=2)
Label(root, text="Введіть число:", fg='black', background='red').grid(row=3, column=0,)
vgadatu_entry = Entry(root)
vgadatu_entry.grid(row=3, column=1)
vgadatu_button = Button(root, text="Вгадати",fg='blue', background='yellow', command=check_guess)
vgadatu_button.grid(row=4, columnspan=2)
result = Label(root, text="")
result.grid(row=5, columnspan=2)
root.mainloop()