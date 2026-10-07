from tkinter import *
root=Tk()
root.title=('login app')
root.geometry("400x400")
frame=Frame(master=root, height=200, width=360, bg="#d0efff")

lb1=Label(frame, text="full name", bg="#3895d3", fg='white', width=12)
lb2=Label(frame, text="email ID", bg="#3895d3", fg='white', width=12)
lb3=Label(frame, text="enter password", bg="#3895d3", fg='white', width=12)

name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame, show="*")
def display():
    name=name_entry.get()
    greet="hey"+name
    message="\ncongratulations for your new account"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox=Text(bg="#bebebe", fg="black")
btn=Button(text="create account", command=display, bg="red")
frame.place(x=20, y=0)
lb1.place(x=20,y=20)
name_entry.place(x=150, y=20)
lb2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lb3.place(x=20,y=140)
pass_entry.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)
root.mainloop()

