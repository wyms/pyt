dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Define a tuple with five basic foods
foods = ('Pizza', 'Burger', 'Salad', 'Pasta', 'Soup')

# Use a for loop to print each food the restaurant offers
print("Original Menu:")
for food in foods:
    print(food)

# Try to modify one of the items (This will raise an error)
# Uncomment the next line to see the error
# foods[0] = 'Sushi'

# The restaurant changes its menu, replacing two items with different foods
# Create a new tuple with the revised menu
revised_menu = ('Sushi', 'Sandwich', 'Salad', 'Pasta', 'Steak')

# Print each item on the revised menu using a for loop
print("\nRevised Menu:")
for food in revised_menu:
    print(food)
