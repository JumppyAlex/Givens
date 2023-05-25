password = "12345678"

import re
if len(password) < 8:
    print('Password Must be 8 xters')

elif not re.search ("[a-z]" , password) :
    print("Small Letters Required !")

elif not re.search("[A-Z" , password) :
    print("Capital Letters Required !")

elif not re.search("0-9" , password) :
    print("A Number is Required !")  


elif not re.search("[@#$%^&" , password) :
    print("A Symbol is Required !")


elif not re.match("[abc" , password) :
    print("You cannot use abc,123 In a password ")

else :
    print("Valid Password")

