# String equality and inequality tests
fruit = 'apple'
print("\nIs fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit == 'orange'? I predict False.")
print(fruit == 'orange')

# String tests using the lower() method
print("\nIs fruit.lower() == 'APPLE'? I predict True.")
print(fruit.lower() == 'apple')

# Numerical tests
number = 42
print("\nIs number == 42? I predict True.")
print(number == 42)

print("\nIs number != 10? I predict True.")
print(number != 10)

print("\nIs number > 50? I predict False.")
print(number > 50)

print("\nIs number < 100? I predict True.")
print(number < 100)

print("\nIs number >= 42? I predict True.")
print(number >= 42)

print("\nIs number <= 30? I predict False.")
print(number <= 30)

# Tests using the and and or keywords
x = 5
y = 10
print("\nIs x > 0 and y > 0? I predict True.")
print(x > 0 and y > 0)

print("\nIs x > 0 or y < 0? I predict True.")
print(x > 0 or y < 0)

# Test whether an item is in a list
fruits_list = ['apple', 'orange', 'banana']
print("\nIs 'apple' in fruits_list? I predict True.")
print('apple' in fruits_list)

# Test whether an item is not in a list
print("\nIs 'grape' not in fruits_list? I predict True.")
print('grape' not in fruits_list)
