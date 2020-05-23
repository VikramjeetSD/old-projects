from tkinter import *

window = Tk()
window.title("Login Page ")
window.configure(background="grey")
window.geometry("300x80+0+0")

enter_1=StringVar()
enter_2=StringVar()

def click() :
    username=enter_1.get()
    password=enter_2.get()
    print(username,password)
    for i in range(2):
        if username==" " or password==" " or username=="" or password=="" :
            print("Username OR Password invalid ")
            break
    

Label(window,text="Username ",fg="black", bg = "white").grid(row=0,column=1)    # username

Entry(window,textvariable=enter_1,width=50).grid(row=0,column=2) #username

Label(window,text="Password",fg="black",bg="white").grid(row=1,column=1)

Entry(window,textvariable=enter_2,width=50).grid(row=1,column=2)

Button(window,text="Click",width=20,command=click).place(relx=0.75, rely=0.75, anchor=CENTER) # button

window.mainloop()
 
