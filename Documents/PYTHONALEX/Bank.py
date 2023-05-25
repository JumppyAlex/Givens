
#Banking App
def buy_airtime():
    phone = str(input(" Enter phone no. "))
    amount =str (input("Enter amount"))
    pin =str(input("Enter 4 Digit PIN"))
    print("Thank you .Please wait for reply")
def withdraw () :
    '''This is withdrawal money function'''
    agent = str(input("Enter Agent no."))
    Amount = str (input("Enter amount"))
    pin = str(input("Enter 4 Digit PIN"))
    print("Thank you .Please wait for reply")


def send_money () :
    '''This is a send money function '''
    phone =str(input("Enter phone no."))
    amount =str (input("Enter Amount"))
    pin =str (input("Enter 4 Digit PIN"))
    print("Thank you .Please wait for reply")



def menu (name):
    print("Karibu ",name)
    items = "1.Send Money\n2. Withdraw\n3.Buy Airtime\n4.Loan and Savings\n5.Lipa na Mpesa\n6.My Account"
    print(items)
    
    choice = str(input('Reply :'))
    if choice ==" 1":
        send_money()
    elif choice== "2":
        withdraw()
    elif choice ==" 3" :
        buy_airtime()    
    
#Call
menu("Tom")
send_money()
withdraw()
buy_airtime()