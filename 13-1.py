import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
RAIN_DROP_SIZE = 5
RAIN_DROP_COLOR = (0, 0, 255)  # Blue color

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Raindrops")

# Create a list to store raindrops
raindrops = []

# Function to create a new raindrop
def create_raindrop():
    x = random.randint(0, WIDTH)
    y = 0
    return {'x': x, 'y': y}

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Add a new raindrop
    raindrops.append(create_raindrop())

    # Move existing raindrops
    for drop in raindrops:
        drop['y'] += 5  # Adjust the speed of the raindrops

    # Remove raindrops that have fallen off the screen
    raindrops = [drop for drop in raindrops if drop['y'] <= HEIGHT]

    # Fill the screen with a white background
    screen.fill((255, 255, 255))

    # Draw the raindrops
    for drop in raindrops:
        pygame.draw.circle(screen, RAIN_DROP_COLOR, (drop['x'], int(drop['y'])), RAIN_DROP_SIZE)

    # Update the display
    pygame.display.flip()

    # Add a delay to control the animation speed
    pygame.time.delay(30)  # Adjust the delay as needed
