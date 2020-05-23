from tkinter import *

window = Tk()
window.title("Main")
window.geometry("200x80+0+0")

def contin() :
    print("Working !!!")

def quit():
    print("Quit Working !!!")
    exit()
        

Button(window,text="To Continue",command=contin,width=15).pack()

Button(window,text="Quit",command=quit,width=15).pack()


window.mainloop()
