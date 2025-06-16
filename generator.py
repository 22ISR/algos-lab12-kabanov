import tkinter as tk
import random
import string

def generate_pass ():
    length = int(spinbox.get())
    include_numbers = var1.get()
    include_special_symbols = var2.get()
    include_backspace = var3.get()

    symbol = string.ascii_letters

    if include_numbers :
        symbol += string.digits
    if include_special_symbols :
        symbol += string.punctuation
    if include_backspace :
        symbol += ' '

    password = ''.join(random.choice(symbol) for i in range(length))
    textbox.delete(0,tk.END)
    textbox.insert(0, password)

root = tk.Tk()
root.title("супер пупер генератор паролей 1000000")
root.geometry("500x300")
root.configure(bg="black")



spinbox_var = tk.StringVar(value=12)
spinbox = tk.Spinbox( from_=8.0, to=100.0 ,textvariable=spinbox_var, background="pink")
spinbox.pack(pady=10)

label = tk.Label(textvariable=spinbox_var)
label.pack()

var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()

checkbox1 = tk.Checkbutton(root, text="Включить цифры", variable=var1)
checkbox1.pack()
checkbox2 = tk.Checkbutton(root, text="Включить спецсимволы", variable=var2)
checkbox2.pack()
checkbox3 = tk.Checkbutton(root, text="Включить пробелы", variable=var3)
checkbox3.pack()

btn1=tk.Button(root,text="Сгенерировать пароль", command=generate_pass )
btn1.pack()

textbox = tk.Entry(root, font=("Arial", 14))
textbox.pack(pady=5)

root.mainloop()