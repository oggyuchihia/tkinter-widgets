from tkinter import *

window=Tk()
window.title("Tintker window")
window.geometry("300x300")
label=Label(text="hlo", fg="blue" , bg="black",width=10,height=10)

button=Button(text="hi", fg="orange" ,bg="red",width=10,height=10)

entry=Entry(fg="red",bg="yellow",width=50)

label.pack()
button.pack()
entry.pack()

frame=Frame(master=window,relief=RAISED,borderwidth=5)

frame.pack()

label1=Label(master=frame,text="hello")

label1.pack()

textbox=Text(fg="green",bg="white")

textbox.pack()

window.mainloop()