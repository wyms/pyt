print("Enter 'q' at any time to quit.")

while True:
    try:
        first_number = input("\nEnter the first number: ")
        if first_number == 'q':
            break
        second_number = input("Enter the second number: ")
        if second_number == 'q':
            break
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter only numbers!")
    else:
        print(f"The sum is: {result}")
