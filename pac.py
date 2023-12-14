import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
PACMAN_SIZE = 40
PACMAN_SPEED = 5

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman-like Game")

# Pacman properties
pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_direction = 0  # 0: right, 1: up, 2: left, 3: down

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        pacman_direction = 0
    elif keys[pygame.K_UP]:
        pacman_direction = 1
    elif keys[pygame.K_LEFT]:
        pacman_direction = 2
    elif keys[pygame.K_DOWN]:
        pacman_direction = 3

    # Update Pacman position
    if pacman_direction == 0:
        pacman_x += PACMAN_SPEED
    elif pacman_direction == 1:
        pacman_y -= PACMAN_SPEED
    elif pacman_direction == 2:
        pacman_x -= PACMAN_SPEED
    elif pacman_direction == 3:
        pacman_y += PACMAN_SPEED

    # Boundary checking
    pacman_x = max(0, min(WIDTH - PACMAN_SIZE, pacman_x))
    pacman_y = max(0, min(HEIGHT - PACMAN_SIZE, pacman_y))

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, YELLOW, (pacman_x + PACMAN_SIZE // 2, pacman_y + PACMAN_SIZE // 2), PACMAN_SIZE // 2)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
