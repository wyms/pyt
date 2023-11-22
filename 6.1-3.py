# 6-1. Person
person_info = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

# Print each piece of information stored in the dictionary
for key, value in person_info.items():
    print(f"{key.capitalize()}: {value}")

# 6-2. Favorite Numbers
favorite_numbers = {
    'Alice': 7,
    'Bob': 15,
    'Charlie': 42,
    'David': 3,
    'Eve': 11
}

# Print each person’s name and their favorite number
for name, number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

# 6-3. Glossary
programming_glossary = {
    'variable': 'A name given to a storage location in memory.',
    'function': 'A block of code that performs a specific task.',
    'list': 'An ordered collection of items.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'A control flow statement that allows code to be executed repeatedly.'
}

# Print each word and its meaning with newline between each pair
for word, meaning in programming_glossary.items():
    print(f"{word.capitalize()}: {meaning}\n")
