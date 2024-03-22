# Define the file name
file_name = 'learning_python.txt'

# Open the file and read its contents
with open(file_name) as file_object:
    contents = file_object.read()

# Loop directly over the lines returned by splitlines() and print each one
for line in contents.splitlines():
    print(line)
