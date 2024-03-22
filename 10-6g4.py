try:
    first_number = input("Enter the first number: ")
    second_number = input("Enter the second number: ")
    result = int(first_number) + int(second_number)
except ValueError:
    print("Please enter only numbers!")
else:
    print(f"The sum is: {result}")
