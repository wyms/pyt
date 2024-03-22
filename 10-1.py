def read_and_print_file(filename):
    """Reads the contents of a file and prints them twice:
    - Once by reading the entire file
    - Once by storing lines in a list and iterating

    Args:
        filename (str): The name of the text file.
    """

    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Method 1: Read the entire file and print
            contents = file.read()
            print(contents)

            # Method 2: Read lines into a list and print each line
            lines = file.readlines()
            for line in lines:
                print(line, end='')

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage: Replace 'learning_python.txt' with your actual filename
read_and_print_file('learning_python.txt')
