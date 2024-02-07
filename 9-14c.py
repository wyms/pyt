import random

# Define a list containing numbers and letters
lottery_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 numbers or letters
winning_selection = random.sample(lottery_tickets, 4)

# Print the winning selection
print("The winning selection is:", winning_selection)

# Print a message saying that any ticket matching these 4 numbers or letters wins a prize
print("Any ticket matching these 4 numbers or letters wins a prize!")
