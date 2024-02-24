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
        result.config(text="", fg="black")
        secret_number_global = secret_number
        root.title("Вгадай число - Спроби: 0")
        min_entry.config(state="disabled")
        max_entry.config(state="disabled")
    else:
        result.config(text="Введіть коректні значення!", fg="red")
def check_guess():
    global attempts
    global secret_number_global
    if secret_number_global is None:
        messagebox.showerror("Помилка", "Спочатку згенеруйте число!")
        return
    guess = vgadatu_entry.get()
    if guess.isdigit():
        guess = int(guess)
        attempts += 1
        root.title(f"Вгадай число - Спроби: {attempts}")
        if guess < secret_number_global:
            result.config(text="Загадане число більше", fg="blue",background='red',)
        elif guess > secret_number_global:
            result.config(text="Загадане число менше", fg="red",background='blue',)
        else:
            result.config(text="Вітаю! Ви вгадали число!", fg="green")
            messagebox.showinfo("Вітаю!", f"Ви вгадали число за {attempts} спроб")
            vgadatu_entry.config(state="disabled")
    else:
        result.config(text="Введіть коректне число!", fg="red")
    if attempts == 5:
        vgadatu_entry.config(state="disabled")
    if attempts >= 5:
        result.config(text="Ви використали всі спроби. Спробуйте ще раз.", fg="red")
        answer = messagebox.askyesno("Вгадай число", "Бажаєте розпочати нову гру?")
        if answer:
            generate_number()
root = Tk()
root.title("Вгадай число - Спроби: 0")
root.configure(bg='green')  # Set background color to light grey
Label(root, text="Мінімальне значення:", fg="green",background='red',).grid(row=0, column=0)
Label(root, text="Максимальне значення:", fg="black",background='blue',).grid(row=1, column=0)
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