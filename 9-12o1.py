import random

class Die:
    def __init__(self, num_sides=6):
        """
        Initializes a Die object with the specified number of sides.

        Args:
            num_sides (int, optional): The number of sides on the die. Defaults to 6.
        """

        if num_sides < 1:
            raise ValueError("Number of sides must be at least 1.")

        self.num_sides = num_sides

    def roll_die(self):
        """
        Rolls the die and returns a random number between 1 and the number of sides.
        """

        return random.randint(1, self.num_sides)

# Create a 6-sided die and roll it 10 times
six_sided_die = Die()
for _ in range(10):
    roll = six_sided_die.roll_die()
    print(f"6-sided die roll: {roll}")

# Create a 10-sided die and a 20-sided die. Roll each die 10 times
ten_sided_die = Die(10)
for _ in range(10):
    roll = ten_sided_die.roll_die()
    print(f"10-sided die roll: {roll}")

twenty_sided_die = Die(20)
for _ in range(10):
    roll = twenty_sided_die.roll_die()
    print(f"20-sided die roll: {roll}")
