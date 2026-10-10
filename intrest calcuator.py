import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        p, t, r = float(e_p.get()), float(e_t.get()), float(e_r.get())
        si = (p * t * r) / 100
        ci = p * ((1 + r / 100) ** t) - p
        lbl_res.config(text=f"SI: {si:.2f}\nCI: {ci:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

root = tk.Tk()
root.title("Interest Calc")
root.geometry("250x250")

tk.Label(root, text="Principal:").pack()
e_p = tk.Entry(root)
e_p.pack()

tk.Label(root, text="Time (Years):").pack()
e_t = tk.Entry(root)
e_t.pack()

tk.Label(root, text="Rate (%):").pack()
e_r = tk.Entry(root)
e_r.pack()

tk.Button(root, text="Calculate", command=calculate).pack(pady=10)
lbl_res = tk.Label(root, text="SI: 0.00\nCI: 0.00", font=("Arial", 10, "bold"))
lbl_res.pack()

root.mainloop()
