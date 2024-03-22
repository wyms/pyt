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