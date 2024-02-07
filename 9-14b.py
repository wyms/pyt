import random

# Create a list containing 10 numbers and 5 letters
lottery_items = [str(i) for i in range(1, 11)] + [chr(i) for i in range(65, 91)]

# Randomly select 4 items without duplicates
winning_items = random.sample(lottery_items, 4)

# Print the winning message
print("Winning ticket:")
for item in winning_items:
    print(item, end=" ")

print("\nAny ticket matching these 4 numbers or letters wins a prize!")
