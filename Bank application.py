import random
print("your account num is",random.randrange(5000000,6000000))
User=input("enter user name:")
def ge():
  gmail=input("enter the gmail:")
  if "@"in gmail:
    if "outlook" in gmail or "gmail" in gmail:
      print("")
    else:
      print("invalid gmail")
      ge() 
  else:
    print("check the  gmail")
    ge()
ge()
def passwd_check(passwd):
    '''enter the correct password'''
    SpecialSym=['$','@','#']
    if len(passwd) < 6:
      print("enter the correct password")
      pas()
    if len(passwd) > 10:
      pas()
    if not any(char.isdigit() for char in passwd):
      print("invalid password")
      pas()
    if not any(char.isupper() for char in passwd):
      print("invalid password")
      pas()
    if not any(char.islower() for char in passwd):
      print("invalid password")
      pas()
    if not any(char in SpecialSym for char in passwd):
      print("invalid password")
      pas()
    return("")
def pas():
    print(passwd_check.__doc__)
    passwd = input('enter the password : ')
    print(passwd_check(passwd))
    print("password is:",passwd)
    return
pas()
while True:
    mobilenum=input("enter mobile num:")
    if len(mobilenum)!=10:
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

















