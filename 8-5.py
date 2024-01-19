def describe_city(city, country="Default Country"):
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("New York")

# Test with a specified country
describe_city("Reykjavik", "Iceland")

# Test with a specified country
describe_city("Paris", "France")

# Test with the default country
describe_city("New York")
