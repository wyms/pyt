def print_file_contents(filename):
    """Print the contents of a file."""
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")

files = ['cats.txt', 'dogs.txt']
for file in files:
    print_file_contents(file)
