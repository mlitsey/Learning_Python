secret = 'swordfish'
pw=''
count = 0
max_attempt=5
approved=False
while pw != secret:
    count +=1
    if count >  max_attempt: break
    pw = input(f'{count}: what is the secret password?')
else:  # while loop as long as pwd is not secret
    approved=True
        
print('correct password entered!' if approved else 'incorrect pwd')