import random

# Define the list containing numbers and letters
lottery_tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Define your ticket
my_ticket = [3, 7, 'A', 9]

# Initialize a counter to keep track of the number of iterations
num_attempts = 0

# Continue pulling numbers until your ticket wins
while True:
    # Increment the counter for each iteration
    num_attempts += 1
    
    # Randomly select 4 numbers or letters
    winning_selection = random.sample(lottery_tickets, 4)
    
    # Check if the winning selection matches your ticket
    if winning_selection == my_ticket:
        print("Congratulations! You won the lottery!")
        print("It took", num_attempts, "attempts to win.")
        break
