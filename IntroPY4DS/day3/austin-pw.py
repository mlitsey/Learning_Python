# Password entering exercise
# 01. Allow the user to enter a password that matches a secret password
# 02. Allow them to make 5 attempts
# 03. Let them know how many they have made
# 04. Display if password is correct or if max attempts has been reaced.

SECRET_PW = 'katana'
pw_in = ''
cur_attempts = 0
MAX_ATTEMPTS = 5

while cur_attempts <= MAX_ATTEMPTS:
    # Ask for pass
    pw_in = input("Password: ")
    # Increment current attempts
    cur_attempts += 1
    if pw_in != SECRET_PW:
        # Login failure
        if cur_attempts == MAX_ATTEMPTS:
            print("Maximum attempts reached.")
            break
        else:
            print("Incorrect password. ({} out of {} tries left.)".format((MAX_ATTEMPTS - cur_attempts), MAX_ATTEMPTS))
            continue
    else:
        # Successful login
        print("Successful login!")
        print("Present pretty shell here.")
        break