# 6-7. People
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York'
}

person2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles'
}

person3 = {
    'first_name': 'Bob',
    'last_name': 'Johnson',
    'age': 35,
    'city': 'Chicago'
}

people = [person1, person2, person3]

# Loop through the list of people and print information about each person
for person in people:
    for key, value in person.items():
        print(f"{key.capitalize()}: {value}")
    print()

# 6-8. Pets
pet1 = {'kind': 'dog', 'owner': 'Alice'}
pet2 = {'kind': 'cat', 'owner': 'Bob'}
pet3 = {'kind': 'parrot', 'owner': 'Charlie'}

pets = [pet1, pet2, pet3]

# Loop through the list of pets and print information about each pet
for pet in pets:
    for key, value in pet.items():
        print(f"{key.capitalize()}: {value}")
    print()

# 6-9. Favorite Places
favorite_places = {
    'John': ['Paris', 'Tokyo'],
    'Jane': ['New York', 'London'],
    'Bob': ['Sydney', 'Rome']
}

# Loop through the dictionary and print each person’s name and their favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are: {', '.join(places)}")
print()

# 6-10. Favorite Numbers
favorite_numbers = {
    'Alice': [7, 14, 21],
    'Bob': [3, 6, 9],
    'Charlie': [10, 20, 30]
}

# Loop through the dictionary and print each person’s name along with their favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: {', '.join(map(str, numbers))}")
print()

# 6-11. Cities
cities = {
    'New York': {'country': 'USA', 'population': 8398748, 'fact': 'The city that never sleeps'},
    'Tokyo': {'country': 'Japan', 'population': 37435191, 'fact': 'Hosted the 2020 Summer Olympics'},
    'Paris': {'country': 'France', 'population': 2140526, 'fact': 'Known as the City of Love'}
}

# Loop through the dictionary and print the name of each city and all the information about it
for city, info in cities.items():
    print(f"{city}:")
    for key, value in info.items():
        print(f"  {key.capitalize()}: {value}")
    print()

# 6-12. Extensions
# You can extend any of the previous examples by adding new keys and values, changing the context, or improving formatting.
# Let me know if you have a specific example in mind for this extension.
