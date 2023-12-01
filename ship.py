import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
BULLET_SIZE = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sideways Shooter")

# Player
player = pygame.Rect(50, HEIGHT // 2 - PLAYER_SIZE // 2, PLAYER_SIZE, PLAYER_SIZE)
player_speed = 5

# Bullets
bullets = []

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player.right, player.centery - BULLET_SIZE // 2, BULLET_SIZE, BULLET_SIZE)
                bullets.append(bullet)

    # Move player
    keys = pygame.key.get_pressed()
    player.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed

    # Move bullets
    bullets = [bullet.move(10, 0) for bullet in bullets]

    # Remove bullets that go off-screen
    bullets = [bullet for bullet in bullets if bullet.x < WIDTH]

    # Fill the screen with a white background
    screen.fill(WHITE)

    # Draw player
    pygame.draw.rect(screen, RED, player)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
