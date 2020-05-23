from tkinter import *

'''
login - username & password
register - userame & password & phone




'''
window = Tk()
window.title("Main")
window.geometry("200x80+0+0")

def contin() :
    window=Tk()
    window.title("Drop Menu")
    window.geometry("300x100+0+0")

    clicked=StringVar(window)
    clicked.set("Select")

    drop=OptionMenu(window,clicked,"Select","Login","Register")
    drop.pack()

    def ok() :
        if clicked.get() == "Select" :
            print("Enter a Valid Value ")
            
        if clicked.get() =="Login" :
            window = Tk()
            window.title("Login Page ")

            window.geometry("300x80+0+0")

            enter_1=StringVar()
            enter_2=StringVar()

            def click() :
                username=enter_1.get()
                password=enter_2.get()

                Label(window,text="Username ",fg="black", bg = "white").grid(row=0,column=1)    # username

                Entry(window,textvariable=enter_1,width=50).grid(row=0,column=2) #username

                Label(window,text="Password",fg="black",bg="white").grid(row=1,column=1)

                Entry(window,textvariable=enter_2,width=50).grid(row=1,column=2)

                Button(window,text="Click",width=20,command=click).place(relx=0.75, rely=0.75, anchor=CENTER) # button

                window.mainloop()
                for i in range(2):
                        if username==" " or password==" " or username=="" or password=="" :
                            print("Username OR Password invalid ")
                            break
                if username==row[0] and password==row[1] :
                    print("login Successfull")
                else :
                    print("-"*60)
                    print("credential wrong ")   
            click()
        if clicked.get()=="Register" :
            window=Tk()
            window.title("Register")

            enter_3=StringVar()
            enter_4=StringVar()
            enter_5=StringVar()

            def click() :
                username=enter_3.get()
                password=enter_4.get()
                phone=enter_5.get()
                print(username,password)
                print(enter_3.get())
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
                
            
                            
                    
    button = Button(window, text="OK", command=ok)
    button.pack()

def quit():
    print("Quit Working !!!")
    exit()
        

Button(window,text="To Continue",command=contin,width=15).pack()

Button(window,text="Quit",command=quit,width=15).pack()

window.mainloop()
