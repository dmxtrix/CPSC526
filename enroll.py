import hashlib
import os
import hmac
username = input("Enter a username: ")
password = input("Enter a password: ")
#check if username is already in the file
if len(username) == 0:
    print("rejected")
    exit(-1)
with open('passwords.txt', 'r') as a:
    for line in a:
        temp = line
        temp = temp.split(':')
        if temp[0] == username:
            print("rejected")
            exit(-1) 
a.close()
#check if the password is simple
with open('words.txt', 'r') as b:
    for line in b:
        #check if password is a single number
        if password.isdigit() and len(password) == 1:
            print("rejected")
            exit(-1)
        #check if password is just a word
        elif password in line:
            print("rejected")
            exit(-1)
        #if first part of password is a word last element is a number
        elif (password[:-1] in line and password[-1:].isdigit()):
            print("rejected")
            exit(-1)
        #if the first part is a number and the rest is a word
        elif (password[1:] in line and password[0].isdigit()):
            print("rejected")
            exit(-1)
b.close()
print("accepted")
#encrypt the password, store the salt and then the hash
salt = os.urandom(8)
hashed = hmac.new(salt, password.encode(), hashlib.sha3_256)
#username:salt:hash
with open('passwords.txt', 'a') as c:
    c.write(username+':')
    c.write(salt.hex())
    c.write(':')
    c.write(hashed.hexdigest())
    c.write('\n')
c.close()
exit(0)
