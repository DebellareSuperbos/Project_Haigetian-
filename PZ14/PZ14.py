#Вариант 31(32)
#https://i2.wp.com/ps.w.org/ultimate-form-builder-lite/assets/screenshot-1.png


import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("ALL FIELDS FORM")
root.geometry("500x750")
root.configure(bg="white")

title = tk.Label(root, text="ALL FIELDS FORM", font=("Arial", 18, "bold"), bg="white", fg="#333")
title.pack(pady=(20, 10))

l1 = tk.Label(root, text="Textfield", bg="white", font=("Arial", 10), anchor="w")
l1.pack(fill="x", padx=20)
e1 = tk.Entry(root, bg="white", relief="solid", borderwidth=1)
e1.pack(fill="x", padx=20, pady=(0, 10))

l2 = tk.Label(root, text="Textarea", bg="white", font=("Arial", 10), anchor="w")
l2.pack(fill="x", padx=20)
t2 = tk.Text(root, height=5, bg="white", relief="solid", borderwidth=1)
t2.pack(fill="x", padx=20, pady=(0, 10))

l3 = tk.Label(root, text="Email Address", bg="white", font=("Arial", 10), anchor="w")
l3.pack(fill="x", padx=20)
e3 = tk.Entry(root, bg="white", relief="solid", borderwidth=1)
e3.pack(fill="x", padx=20, pady=(0, 10))

l4 = tk.Label(root, text="Dropdown", bg="white", font=("Arial", 10), anchor="w")
l4.pack(fill="x", padx=20)

var_drop = tk.StringVar()
var_drop.set("Option 1")
dropdown = tk.OptionMenu(root, var_drop, "Option 1", "Option 2", "Option 3")
dropdown.config(bg="white", relief="solid", borderwidth=1)
dropdown.pack(fill="x", padx=20, pady=(0, 10))

l5 = tk.Label(root, text="Radio Button", bg="white", font=("Arial", 10), anchor="w")
l5.pack(fill="x", padx=20)

var_radio = tk.StringVar()
var_radio.set("Option 1")

radio_frame = tk.Frame(root, bg="white")
radio_frame.pack(fill="x", padx=20, pady=(0, 10))

r1 = tk.Radiobutton(radio_frame, text="Option 1", variable=var_radio, value="Option 1", bg="white")
r1.pack(side="left", padx=(0, 20))
r2 = tk.Radiobutton(radio_frame, text="Option 2", variable=var_radio, value="Option 2", bg="white")
r2.pack(side="left")

l6 = tk.Label(root, text="Checkbox", bg="white", font=("Arial", 10), anchor="w")
l6.pack(fill="x", padx=20)

var_check1 = tk.IntVar()
var_check2 = tk.IntVar()
var_check3 = tk.IntVar()

check_frame = tk.Frame(root, bg="white")
check_frame.pack(fill="x", padx=20, pady=(0, 10))

c1 = tk.Checkbutton(check_frame, text="Option 1", variable=var_check1, bg="white")
c1.pack(anchor="w")
c2 = tk.Checkbutton(check_frame, text="Option 2", variable=var_check2, bg="white")
c2.pack(anchor="w")
c3 = tk.Checkbutton(check_frame, text="Option 3", variable=var_check3, bg="white")
c3.pack(anchor="w")

l7 = tk.Label(root, text="Password", bg="white", font=("Arial", 10), anchor="w")
l7.pack(fill="x", padx=20)
e7 = tk.Entry(root, show="*", bg="white", relief="solid", borderwidth=1)
e7.pack(fill="x", padx=20, pady=(0, 10))

l8 = tk.Label(root, text="Number Field", bg="white", font=("Arial", 10), anchor="w")
l8.pack(fill="x", padx=20)
e8 = tk.Entry(root, bg="white", relief="solid", borderwidth=1)
e8.pack(fill="x", padx=20, pady=(0, 10))

l9 = tk.Label(root, text="Mathematical", bg="white", font=("Arial", 10), anchor="w")
l9.pack(fill="x", padx=20)

math_frame = tk.Frame(root, bg="white")
math_frame.pack(fill="x", padx=20, pady=(0, 10))

math_label = tk.Label(math_frame, text="6 + 8 =", bg="white", font=("Arial", 11))
math_label.pack(side="left", padx=(0, 10))
math_entry = tk.Entry(math_frame, width=10, bg="white", relief="solid", borderwidth=1)
math_entry.pack(side="left")
math_result = tk.Label(math_frame, text="", bg="white", fg="red", font=("Arial", 9))
math_result.pack(side="left", padx=(10, 0))

l10 = tk.Label(root, text="Capcha", bg="white", font=("Arial", 10), anchor="w")
l10.pack(fill="x", padx=20)

captcha_frame = tk.Frame(root, bg="#f0f0f0", relief="solid", borderwidth=1)
captcha_frame.pack(fill="x", padx=20, pady=(0, 10), ipady=10)

captcha_label = tk.Label(captcha_frame, text="Google Captcha", bg="#f0f0f0", font=("Arial", 10, "bold"))
captcha_label.pack(side="left", padx=(20, 0))

robot_var = tk.IntVar()
robot_check = tk.Checkbutton(captcha_frame, text="I'm not a robot", variable=robot_var, bg="#f0f0f0")
robot_check.pack(side="right", padx=(0, 20))

def submit_form():
    result = f"Textfield: {e1.get()}\n"
    result += f"Email: {e3.get()}\n"
    result += f"Dropdown: {var_drop.get()}\n"
    result += f"Radio: {var_radio.get()}\n"
    result += f"Password: {e7.get()}\n"
    result += f"Number: {e8.get()}\n"
    result += f"Math: {math_entry.get()}\n"
    result += f"Robot: {'Да' if robot_var.get() else 'Нет'}"
    messagebox.showinfo("Результат", result)

btn = tk.Button(root, text="Submit", command=submit_form, bg="#4CAF50", fg="white",
                font=("Arial", 12, "bold"), relief="flat", height=2)
btn.pack(fill="x", padx=20, pady=(10, 20))

root.mainloop()
