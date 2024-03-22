# First, let's create the file learning_python.txt with some example content about what has been learned in Python.
# This simulates writing a few lines in a blank file as described.

content = """
In Python you can create variables to store data.
In Python you can write functions to perform operations.
In Python you can use loops to repeat actions.
In Python you can use conditional statements for decision making.
"""

# Writing the content to learning_python.txt
with open('learning_pythong4.txt', 'w') as file:
    file.write(content)

# Now, we will write a program to read the file and print what was written two times as described.
# First, by reading in the entire file.
# Second, by storing the lines in a list and then looping over each line.
# Finally, we will read each line from the file, replace "Python" with "C", and print each modified line.

# Reading and printing the entire file content
with open('learning_pythong4.txt', 'r') as file:
    entire_file_content = file.read()
    print("Reading the entire file content:\n", entire_file_content)

# Reading, storing lines in a list, and looping over each line to print
print("\nReading lines from the file and printing each line:")
with open('learning_pythong4.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

# Replacing "Python" with "C" in each line and printing the modified line
print("\nReplacing 'Python' with 'C' and printing each modified line:")
for line in lines:
    modified_line = line.replace('Python', 'C')
    print(modified_line.strip())

# This Python code demonstrates file writing, reading, and string manipulation with replace() method.
