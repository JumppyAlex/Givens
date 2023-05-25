import hashlib
password ="alex123"

encrypted =hashlib.md5(password.encode())

print("the hashed password is : " +encrypted.hexdigest())
