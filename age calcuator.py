import tkinter as tk
from datetime import date

def calc():
    try:
        born = date(int(e_y.get()), int(e_m.get()), int(e_d.get()))
        today = date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        lbl.config(text=f"Age: {age}")
    except:
        lbl.config(text="Invalid Input")

root = tk.Tk()
root.title("Age Calc")

e_d = tk.Entry(root)
e_m = tk.Entry(root)
e_y = tk.Entry(root)
lbl = tk.Label(root, text="Age: ")

e_d.pack()
e_m.pack()
e_y.pack()
tk.Button(root, text="Calculate", command=calc).pack()
lbl.pack()

root.mainloop()