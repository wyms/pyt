import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
CELL_SIZE = 40
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Game variables
maze = [
    "####################",
    "#P.................#",
    "#.################.#",
    "#.#...............#.#",
    "#.#.#############.###",
    "#.#.#.............#.#",
    "#.#.#.#############.#",
    "#...#...............#",
    "#####################"
]

pacman_position = [1, 1]
ghost_position = [8, 18]
score = 0

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

def draw_maze():
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "#":
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif cell == "P":
                pygame.draw.circle(screen, YELLOW, (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2)

def move_pacman(direction):
    global pacman_position, score
    x, y = pacman_position

    if direction == "UP" and maze[x - 1][y] != "#":
        x -= 1
    elif direction == "DOWN" and maze[x + 1][y] != "#":
        x += 1
    elif direction == "LEFT" and maze[x][y - 1] != "#":
        y -= 1
    elif direction == "RIGHT" and maze[x][y + 1] != "#":
        y += 1

    if maze[x][y] == ".":
        score += 1
        maze[x] = maze[x][:y] + " " + maze[x][y + 1:]

    pacman_position = [x, y]

def move_ghost():
    global ghost_position
    x, y = ghost_position

    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dx, dy = random.choice(moves)

    if maze[x + dx][y + dy] != "#":
        x += dx
        y += dy

    ghost_position = [x, y]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_pacman("UP")
            elif event.key == pygame.K_DOWN:
                move_pacman("DOWN")
            elif event.key == pygame.K_LEFT:
                move_pacman("LEFT")
            elif event.key == pygame.K_RIGHT:
                move_pacman("RIGHT")

    move_ghost()

    screen.fill(BLACK)
    draw_maze()

    pygame.display.flip()
    clock.tick(FPS)
