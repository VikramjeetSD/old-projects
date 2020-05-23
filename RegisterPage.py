from tkinter import *

window=Tk()
window.title("Register")

enter_3=StringVar()
enter_4=StringVar()
enter_5=StringVar()

def click() :
    username=enter_3.get()
    password=enter_4.get()
    phone=enter_5.get()
    for i in range(2):
        if username==" " or password==" " or username=="" or password=="" or phone==" " or phone=="" :
            print("Username , Password , Phone no.  Invalid ")
            break
    

Label(window,text="Username ",fg="black", bg = "white").grid(row=0,column=1)    # username

Entry(window,textvariable=enter_3,width=50).grid(row=0,column=2) #username

Label(window,text="Password",fg="black",bg="white").grid(row=1,column=1)

Entry(window,textvariable=enter_4,width=50).grid(row=1,column=2)

Label(window,text="PhoneNo. ",fg="black", bg = "white").grid(row=2,column=1)    # username

Entry(window,textvariable=enter_5,width=50).grid(row=2,column=2)

Button(window,text="Click",width=20,command=click).grid(row=3,column=2) # button

window.mainloop()
