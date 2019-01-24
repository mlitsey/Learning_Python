import sys #for sys.exit

secret = "knockknock"

pw = ''
attempts = 0
max_attempts = 5 #for easy replacement

while pw != secret:
    if attempts == max_attempts:
        print("Access denied.")
        sys.exit()
    elif attempts > 0:
        print("Incorrect. {} attempts remaining.".format(max_attempts-attempts))
    pw = input("PASSWORD: ")
    
    attempts += 1
    
print("Success!")
    