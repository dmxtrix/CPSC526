import hashlib
import hmac
import sys
try:
    username = sys.argv[1]
    password = sys.argv[2]
except:
    print("access denied")
    exit(-1)
#check if username is already exists
with open('passwords.txt', 'r') as a:
    for line in a:
        temp = line
        temp = temp.split(':')
        if temp[0] == username:
            #if username matches, encrypt the password and see if it matches the password file
            salt = temp[1]
            real_hash = temp[2]
            salt = bytes.fromhex(salt)
            test_hash = hmac.new(salt, password.encode(), hashlib.sha3_256)
            if test_hash.hexdigest()+'\n' == real_hash:
                print("access granted")
                exit(0)
a.close()
print("access denied")
exit(-1)
