import tkinter as tk
from tkinter import messagebox

def convert():
    
    if not messagebox.askyesno("Confirm", "Proceed with conversion?"):
     
        messagebox.showwarning("Cancelled", "Operation halted.")
        return
    try:
     
        cm = float(entry.get()) * 2.54
        messagebox.showinfo("Result", f"Length: {cm:.2f} cm")
     
        if messagebox.askokcancel("Clear", "Clear input field?"):
            entry.delete(0, tk.END)
    except ValueError:
        
        messagebox.showerror("Error", "Please enter a valid number.")

root = tk.Tk()
root.title("Converter")
root.geometry("250x120")

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=15)

tk.Button(root, text="Convert", font=("Arial", 10, "bold"), command=convert).pack()

root.mainloop()