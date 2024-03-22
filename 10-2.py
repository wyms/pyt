def replace_and_print_lines(filename, old_word, new_word):
    """Reads lines from a file, replaces a word with another, and prints the modified lines.

    Args:
        filename (str): The name of the text file.
        old_word (str): The word to be replaced.
        new_word (str): The word to replace with.
    """

    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read lines into a list
            lines = file.readlines()

            # Replace "old_word" with "new_word" in each line
            for line in lines:
                modified_line = line.replace(old_word, new_word)
                print(modified_line, end='')

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage: Replace 'learning_python.txt' with your actual filename
replace_and_print_lines('learning_python.txt', 'Python', 'C')
