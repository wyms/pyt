# Define a tuple with five basic foods
foods = ('Pizza', 'Burger', 'Salad', 'Pasta', 'Soup')

# Use a for loop to print each food the restaurant offers
print("Original Menu:")
for food in foods:
    print(food)

# Try to modify one of the items (This will raise an error)
# Uncomment the next line to see the error
#foods[0] = 'Sushi'

# The restaurant changes its menu, replacing two items with different foods
# Create a new tuple with the revised menu

foods = ('Sushi', 'Burger', 'Salad', 'Pasta', 'Soup')
#revised_menu = ('Sushi', 'Sandwich', 'Salad', 'Pasta', 'Steak')

# Print each item on the revised menu using a for loop
print("\nRevised Menu:")
for food in foods:
    print(food)
