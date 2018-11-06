print('What is your name?')
name = input()
print('How old are you?')
age = input()
if name == 'Alice':
    print('Hi, Alice.')
elif int(age) < 12:
    print('You are not Alice, kiddo.')
elif int(age) > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif int(age) > 100:
    print('You are not Alice, grannie.')
else:
    print("I don't know you.")
# added lines 1-4, changed elif age to elif int(age), added lines 13-14 --> michael.litsey@gmail.com