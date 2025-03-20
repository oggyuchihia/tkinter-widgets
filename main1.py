from tkinter import *

window=Tk()
for i in range(3):
    for j in range(3):
        frame=Frame(master=window,relief=RAISED,borderwidth=3)
        frame.grid(row=i,column=j,padx=5,pady=5)
        label=Label(master=frame,text=f"row {i}\n colum {j}")
        label.pack()

window.mainloop()