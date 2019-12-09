import random
print("your account num is",random.randrange(5000000,6000000))
User=input("enter user name:")
def gmail_check(gmail):
    '''enter the gmail is right'''
    SpecialSym=['@','outlook','gmail']
    if not any(char in SpecialSym for char in gmail):
        print("invalid email")
        ge()
def ge():
    print(gmail_check.__doc__)
    gmail = input('enter the gmail: ')
    print(gmail_check(gmail))
    print("gmail is:",gmail)
ge()
def passwd_check(passwd):
    '''enter the password is right'''
    SpecialSym=['$','@','#']
    if len(passwd) < 6:
        pas()
    if len(passwd) > 10:
        pas()
    if not any(char.isdigit() for char in passwd):
        print("invalid password")
        paas()
    if not any(char.isupper() for char in passwd):
        print("invalid password")
        pas()
    if not any(char.islower() for char in passwd):
        print("invalid password")
        pas()
    if not any(char in SpecialSym for char in passwd):
        print("invalid password")
        pas()
def pas():
    print(passwd_check.__doc__)
    passwd = input('enter the password : ')
    print(passwd_check(passwd))
    print("password is:",passwd)
pas()
while true:
    mobilenum=input("enter pass:")
    if len(mobilenum)!=10 or mobilenum[0]!="9":
        print("invalid,enter regain number")
        continue
    else:
        break
balance=897.32
print("    ATM    ")
print("""
1)        Balance
2)        Withdraw
3)        Deposit
4)        Quit
""")
def opt():
    Option=int(input("Enter Option: "))
    if Option==1:
        print("Balance ",balance)
        opt()
    if Option==2:
        print("Balance ",balance)
        Withdraw=float(input("Enter Withdraw amount  "))
        if (Withdraw<balance):
            forewardbalance=(balance-Withdraw)
            print("remaining Balance   ",forewardbalance)
        else:
            print("No funs in account")
        opt()
    if Option==3:
        print("Balance ",balance)
        Deposit=float(input("Enter deposit amount"))
        if Deposit>0:
            forewardbalance=(balance+Deposit)
            print("remaining balance",forewardbalance)  
        else:
            print("None deposit made")
        opt()
    if Option==4:
        exit()
opt()













