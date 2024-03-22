# Task 10-4: Guest
name = input("Please enter your name: ")
with open('guest.txt', 'w') as file:
    file.write(name)
