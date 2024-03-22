# Exercise 10-6: Addition
def add_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print("The sum is:", result)
    except ValueError:
        print("Error: Please enter valid numbers.")

# Exercise 10-7: Addition Calculator
def addition_calculator():
    while True:
        add_numbers()
        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            break

# Exercise 10-8: Cats and Dogs
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Main function
def main():
    addition_calculator()

    print("\nReading cats.txt:")
    read_file("cats.txt")

    print("\nReading dogs.txt:")
    read_file("dogs.txt")

if __name__ == "__main__":
    main()
