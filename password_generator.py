import random
import string
import sys
# print("=== Password Generator ===")
# length=int(input("Enter your desired password size: "))
# if length < 8:
#     print("Password lenght should be >= 8 .")
#     exit
# else:
#     charachters=string.ascii_letters + string.digits + "@#?!£$&*^"
#     password=""
#     for i in range(length):
#         password+=random.choice(charachters)
#     print("Your password is : ",password)



def password_generator(length,type):
    letters=string.ascii_letters
    numbers=string.digits
    mixed=letters+numbers+"#!234678?><"
    
    if type== 1:
        charachters=letters
    elif type== 2:
        charachters=numbers
    elif type == 3:
        charachters=mixed
    else:
        print ("Invalid response")
        sys.exit()
    
    
    password=""
    for i in range(length):
        password+=random.choice(charachters)
    
    return password

print("=== Password Generator ===")
print("1- Only letters.")
print("2- Only digits.")
print("3- All charachetrs (Strong Password).")

type=int(input("your type choice: "))
length=int(input("Enter your desired password length: "))

if length < 8 :
    print( "length should be >= 8." )
else:
    password=password_generator(length,type)
    print("your password is: ",password)       
    
    
