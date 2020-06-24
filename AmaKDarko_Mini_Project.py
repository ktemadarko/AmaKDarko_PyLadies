def srch(x):
    pattern=r'[A-Z][a-z][a-z][a-z][a-z][a-z][a-z][0-9]'
    
    if re.search(pattern,x):
        print(f"Great, your password is {x}!")
        
    else:
        print("\nError!\n"
              "\nPassword should have 8 characters"
              "\nBegin with a uppercase or capital letter\n"
              '\nFollowed by 6 lowercase letters'
              '\nEnd with a number from 0 to 9.')
        passw=str(input("Enter a new password:"))
        srch(passw)
        
def checkpass():
    passw=str(input('What is your password?'))
    while len(passw)!=8:
        passw=str(input("Enter a password with 8 characters only:"))
        if len(passw)==8:
            print("Checking validity of password...")
            
    srch(passw)
checkpass()def srch(x):
    pattern=r'[A-Z][a-z][a-z][a-z][a-z][a-z][a-z][0-9]'
    
    if re.search(pattern,x):
        print(f"Great, your password is {x}!")
        
    else:
        print("\nError!\n"
              "\nPassword should have 8 characters"
              "\nBegin with a uppercase or capital letter\n"
              '\nFollowed by 6 lowercase letters'
              '\nEnd with a number from 0 to 9.')
        passw=str(input("Enter a new password:"))
        srch(passw)
        
def checkpass():
    passw=str(input('What is your password?'))
    while len(passw)!=8:
        passw=str(input("Enter a password with 8 characters only:"))
        if len(passw)==8:
            print("Checking validity of password...")
            
    srch(passw)
checkpass()
