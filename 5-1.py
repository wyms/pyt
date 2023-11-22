# Conditional Tests
car = 'subaru'

# Test 1
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

# Test 2
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Test 3
print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

# Test 4
print("\nIs car.upper() == 'SUBARU'? I predict True.")
print(car.upper() == 'SUBARU')

# Test 5
print("\nIs len(car) == 6? I predict True.")
print(len(car) == 6)

# Test 6
print("\nIs car != 'subaru'? I predict False.")
print(car != 'subaru')

# Test 7
print("\nIs car.startswith('s')? I predict True.")
print(car.startswith('s'))

# Test 8
print("\nIs car.endswith('u')? I predict True.")
print(car.endswith('u'))

# Test 9
print("\nIs 'u' in car? I predict True.")
print('u' in car)

# Test 10
print("\nIs 'z' not in car? I predict True.")
print('z' not in car)
