# 6-4. Glossary 2
programming_glossary = {
    'variable': 'A name given to a storage location in memory.',
    'function': 'A block of code that performs a specific task.',
    'list': 'An ordered collection of items.',
    'dictionary': 'A collection of key-value pairs.',
    'loop': 'A control flow statement that allows code to be executed repeatedly.'
}

# Loop through the dictionary's keys and values and print each word and its meaning
for word, meaning in programming_glossary.items():
    print(f"{word.capitalize()}: {meaning}\n")

# Add five more Python terms to the glossary
programming_glossary['module'] = 'A file containing Python definitions and statements.'
programming_glossary['class'] = 'A blueprint for creating objects.'
programming_glossary['inheritance'] = 'A way to create a new class using properties of an existing class.'
programming_glossary['method'] = 'A function associated with an object.'
programming_glossary['exception'] = 'An event that occurs during the execution of a program that disrupts the normal flow.'

# Print the updated glossary
for word, meaning in programming_glossary.items():
    print(f"{word.capitalize()}: {meaning}\n")

# 6-5. Rivers
rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'yangtze': 'China'
}

# Loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country}.")

# Loop to print the name of each river
for river in rivers.keys():
    print(river.capitalize())

# Loop to print the name of each country
for country in rivers.values():
    print(country)

# 6-6. Polling
favorite_languages = {
    'alice': 'python',
    'bob': 'java',
    'charlie': 'c++'
}

people_to_poll = ['alice', 'bob', 'dave', 'emma']

# Loop through the list of people to poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.capitalize()}, for responding to the poll!")
    else:
        print(f"Hey, {person.capitalize()}, we invite you to take the poll.")
