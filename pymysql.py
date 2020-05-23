import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='db1'
    )
cursor=mydb.cursor()
#print("-"*60)
#print(mydb.connection_id )

sql_select_Query = "select * from cred "

cursor.execute(sql_select_Query)
records = cursor.fetchall()

print("-"*60)
print("1. Login")
print("-"*60)
print("2. Register")
print("-"*60)

ch=int(input("Enter The Choice :"))
print("-"*60)
def login() :
    if ch==1 :
        u=input("Enter Username :  ")
        p=input("Enter Password :   ")
        for row in records :
            print(" ")
        if u==row[0] and p==row[1] :
            print("Login Successful !!! ")
            print("-"*60)
            print(cursor.rowcount, "record inserted")
            print("-"*60)

            print('-------------------------')
            print('*************************')
            print('LOGIN SUCCESFUL, CONTINUE')
            print('*************************')
            print('-------------------------')
            print()
            print('--------------------------')
            print('**************************')
            print(str.capitalize(u), 'welcome to ATM')
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
                    print(str.capitalize(u), 'YOU HAVE ',row[2], 'RUPEES ON YOUR ACCOUNT.')
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
                        row[2] = row[2] - cash_out
                        print('-----------------------------------')
                        print('***********************************')
                        print('YOUR NEW BALANCE IS: ', row[2], 'RUPEES')
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
                        row[2] = row[2] + cash_in
                        print('----------------------------------------')
                        print('****************************************')
                        print('YOUR NEW BALANCE IS: ', row[2], 'RUPEES')
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
        else :
            print("-"*60)
            print("credential wrong ")
login()
def register() :
    if ch==2 :
        u=input("Enter Username :  ")
        p=input("Enter Password :   ")
        a=int(input("Enter Amount :  "))
        query = "INSERT INTO cred (username, password,amount) VALUES (%s, %s,%s)"
        for row in records :
            users = row[0]
            pins = row[1]
            amounts = row[2]
        values = (u,p,a)
        cursor.execute(query, values)
        mydb.commit()
        


register()

print("Mission Accomplished !!! ")
    
