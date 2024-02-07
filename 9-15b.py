import random

# Create a list containing 10 numbers and 5 letters
lottery_items = [str(i) for i in range(1, 11)] + [chr(i) for i in range(65, 91)]

# Randomly select 4 items for the winning ticket
winning_items = random.sample(lottery_items, 4)

# Simulate lottery attempts until a winning ticket is drawn
attempts = 0
while True:
    # Create a random ticket
    my_ticket = random.sample(lottery_items, 4)

    # Check if the ticket matches the winning items
    if all(item in my_ticket for item in winning_items):
        break

    attempts += 1

# Print the results
print(f"Winning ticket: {winning_items}")
print(f"Number of attempts to win: {attempts}")
