import getpass
import string
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db1'
    )
cursor=mydb.cursor()
#print("-"*60)
print(mydb.connection_id )

sql_select_Query = "select * from cred "

cursor.execute(sql_select_Query)
records = cursor.fetchall()


# creating lists of users, their PINs and bank statements
count = 0
#
print("1. If New User ")
print("2. If Registered User ")
cho: int = int(input("Enter Your Choice :  "))
if cho == 1:
    def register() :
        u=input("Enter Username :  ")
        p=input("Enter Password :   ")
        a=int(input("Enter amount :  "))
        query = "INSERT INTO cred (username, password,amount) VALUES (%s, %s,%s)"
        values = (u,p,a)
        cursor.execute(query, values)
        mydb.commit()
        print("-"*60)
        print(cursor.rowcount, "record inserted")
        print("-"*60)
        
    register()

if cho == 2:
    while True:  # while loop checks existance of the enterd username
        def login() :
            u=input("Enter Username :  ")
            p=input("Enter Password :   ")
            for row in records :
                if row[0] ==u and row[1] == p :
                    print("Login Successful !!! ")
        
                else:
                    print('----------------')
                    print('****************')
                    print('INVALID USERNAME')
                    print('****************')
                    print('----------------')
        login()
    # comparing pin
    while count < 3:
        print('------------------')
        print('******************')
        pin = str(input('PLEASE ENTER PIN: '))
        print('******************')
        print('------------------')
        if pin.isdigit():
            if user == users[0]:
                if pin == pins[0]:
                    break
        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()

        if user == users[1]:
            if pin == pins[1]:
                break
        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()

        if user == users[2]:
            if pin == pins[2]:
                break
        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------')
            print()
    else:
        print('------------------------')
        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        print('------------------------')
        count += 1

    # in case of a valid pin- continuing, or exiting
    if count == 3:
        print('-----------------------------------')
        print('***********************************')
        print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
        print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
        print('***********************************')
        print('-----------------------------------')
        exit()

    print('-------------------------')
    print('*************************')
    print('LOGIN SUCCESFUL, CONTINUE')
    print('*************************')
    print('-------------------------')
    print()
    print('--------------------------')
    print('**************************')
    print(str.capitalize(users[n]), 'welcome to ATM')
    print('**************************')
    print('----------ATM SYSTEM-----------')
    # Main menu
    while True:
        
        print('-------------------------------')
        print('*******************************')
        response = input(
            'SELECT FROM FOLLOWING OPTIONS: \n Statement__(S) \nWithdraw___(W) \nLodgement__(L)  \nChange PIN_(P)  \nQuit_______(Q) \n: ').lower()
        print('*******************************')
        print('-------------------------------')
        valid_responses = ['s', 'w', 'l', 'p', 'q']
        response = response.lower()
        if response == 's':
            print('---------------------------------------------')
            print('*********************************************')
            print(str.capitalize(users[n]), 'YOU HAVE ', amounts[n], 'RUPEES ON YOUR ACCOUNT.')
            print('*********************************************')
            print('---------------------------------------------')

        elif response == 'w':
            print('---------------------------------------------')
            print('*********************************************')
            cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
            print('*********************************************')
            print('---------------------------------------------')
            if cash_out % 10 != 0:
                print('------------------------------------------------------')
                print('******************************************************')
                print('AMOUNT YOU WANT TO WITHDRAW MUST TO MATCH 10 RUPEES NOTES')
                print('******************************************************')
                print('------------------------------------------------------')
            elif cash_out > amounts[n]:
                print('-----------------------------')
                print('*****************************')
                print('YOU HAVE INSUFFICIENT BALANCE')
                print('*****************************')
                print('-----------------------------')
            else:
                amounts[n] = amounts[n] - cash_out
                print('-----------------------------------')
                print('***********************************')
                print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
                print('***********************************')
                print('-----------------------------------')

        elif response == 'l':
            print()
            print('---------------------------------------------')
            print('*********************************************')
            cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
            print('*********************************************')
            print('---------------------------------------------')
            print()
            if cash_in % 10 != 0:
                print('----------------------------------------------------')
                print('****************************************************')
                print('AMOUNT YOU WANT TO LODGE MUST TO MATCH 10 RUPEES NOTES')
                print('****************************************************')
                print('----------------------------------------------------')
            else:
                amounts[n] = amounts[n] + cash_in
                print('----------------------------------------')
                print('****************************************')
                print('YOUR NEW BALANCE IS: ', amounts[n], 'RUPEES')
                print('****************************************')
                print('----------------------------------------')
        elif response == 'p':
            print('-----------------------------')
            print('*****************************')
            new_pin = str(input('ENTER A NEW PIN: '))
            print('*****************************')
            print('-----------------------------')
            if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
                print('------------------')
                print('******************')
                new_ppin = str(input('CONFIRM NEW PIN: '))
                print('*******************')
                print('-------------------')
                if new_ppin != new_pin:
                    print('------------')
                    print('************')
                    print('PIN MISMATCH')
                    print('************')
                    print('------------')
                else:
                    pins[n] = new_pin
                    print('NEW PIN SAVED')
            else:
                print('-------------------------------------')
                print('*************************************')
                print('   NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
                print('*************************************')
                print('-------------------------------------')
        elif response == 'q':
            exit()
        else:
            print('------------------')
            print('******************')
            print('RESPONSE NOT VALID')
            print('******************')
            print('------------------')
