from tkinter import *

window=Tk()
window.title("Drop Menu")
window.geometry("300x100+0+0")

clicked=StringVar(window)
clicked.set("Select")

drop=OptionMenu(window,clicked,"Select","Login","Register")
drop.pack()

def ok() :
    window.quit()
    if clicked.get() == "Select" :
        print("Enter a Valid Value ")
        window.quit()

button = Button(window, text="OK", command=ok)
button.pack()

window.mainloop()
