import sys
secret = 'holycrapigotit'
pw=''
counter = 5

while pw != secret:
    pw = input('What is the secret password?')
    
    if pw == secret:
        print('You entered the correct password!')
        sys.exit()
    counter-=1
    print(f'Password is incorrect, you have {counter} attempts left')
    
    if counter == 0:
        print('You have exceeded your maximum attempts!')
        sys.exit()  
    

    
