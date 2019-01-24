pw=''
secret='password'
counter = 0
max_attempts = 5
auth=False
while pw != secret:
    counter+=1
    if counter>max_attempts: break
    if counter==3: continue
    pw = input(f'{counter}: password is ')
else:
    auth=True
    
print('works' if auth else 'not working')