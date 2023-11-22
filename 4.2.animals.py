# Step 1: Storing animal names in a list
animals = ['Dog', 'Cat', 'Rabbit']

# Step 2: Using a for loop to print the name of each animal
print("Animal Names:")
for animal in animals:
    print(animal)

# Step 3: Modifying the program to print a statement about each animal
print("\nStatements about Animals:")
for animal in animals:
    print(f"A {animal.lower()} would make a great pet.")

# Step 4: Adding a line stating what these animals have in common
print("\nCommon Characteristic:")
print("Any of these animals would make a great pet!")
