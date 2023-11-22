# 4-4. One Million:
print("Exercise 4-4: One Million")

def prompt_for_confirmation():
    confirmation = input("Do you want to see 1 million numbers printed? (Y/N) ")
    return confirmation

confirmation = prompt_for_confirmation()

if confirmation.lower() == 'y':
    numbers = list(range(1, 1000001))
    for number in numbers:
        print(number)
    # Note: This might take a while to print a million numbers, and you can stop it manually.
    print()
