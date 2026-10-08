import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        
        result = num1 * num2
        
       
        label_result.config(text=f"Product: {result}")
    except ValueError:

        messagebox.showerror("Invalid Input", "Please enter valid numbers in both fields.")

root = tk.Tk()
root.title("Product Calculator")
root.geometry("350x250")


label1 = tk.Label(root, text="Enter First Number:")
label1.pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter Second Number:")
label2.pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)


button_calculate = tk.Button(root, text="Calculate Product", command=calculate_product)
button_calculate.pack(pady=15)

label_result = tk.Label(root, text="Product: ", font=("Arial", 12, "bold"))
label_result.pack(pady=5)


root.mainloop()