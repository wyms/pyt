import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ALIEN_SIZE = 30
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sideways Shooter Part 2")

# Player
player = pygame.Rect(WIDTH // 2 - PLAYER_SIZE // 2, HEIGHT - 2 * PLAYER_SIZE, PLAYER_SIZE, PLAYER_SIZE)

# Bullets
bullets = []

# Aliens
aliens = []

def create_alien():
    x = WIDTH - ALIEN_SIZE
    y = random.randint(0, HEIGHT - ALIEN_SIZE)
    return pygame.Rect(x, y, ALIEN_SIZE, ALIEN_SIZE)

def draw_elements():
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)
    for alien in aliens:
        pygame.draw.rect(screen, RED, alien)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.centerx, player.top, 5, 10))

    # Move player
    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5

    # Move bullets
    bullets = [bullet.move(0, -10) for bullet in bullets]

    # Move aliens
    aliens = [alien.move(-5, 0) for alien in aliens]

    # Check for collisions
    for bullet in bullets[:]:
        if bullet.colliderect(player):
            bullets.remove(bullet)
        for alien in aliens[:]:
            if bullet.colliderect(alien):
                bullets.remove(bullet)
                aliens.remove(alien)

    # Create new aliens
    if random.randint(1, 100) < 5:
        aliens.append(create_alien())

    # Draw elements
    draw_elements()

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
