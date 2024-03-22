# Task 10-5: Guest Book
names = []

print("Enter 'quit' when you are finished.")
while True:
    name = input("Please enter your name: ")
    if name == 'quit':
        break
    else:
        print(f"Hello, {name}! You've been added to the guest book.")
        names.append(name)

with open('guest_book.txt', 'w') as file:
    for name in names:
        file.write(name + "\n")
