import re

def srch(x):
    pattern=r'[A-Z][a-z][a-z][a-z][0-9]'
    
    if re.search(pattern,x):
        print(f"Great, your password is {x}!")
        
    else:
        print("\nError!\n"
              "\nPassword should have 5 characters"
              "\nBegin with a uppercase or capital letter\n"
              '\nFollowed by 3 lowercase letters'
              '\nEnd with a number from 0 to 9.')
              
        passw=str(input("Enter a new password:"))
        srch(passw)
        
def checkp():
    passw=str(input('What is your password?'))
    while len(passw)!=5:
        passw=str(input("Enter a password with 5 characters only:"))
        if len(passw)==5:
            print("Checking validity of password...")
            
    srch(passw)
checkp()
