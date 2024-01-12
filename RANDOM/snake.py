import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up game constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
FPS = 10

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize clock
clock = pygame.time.Clock()

# Initialize snake
snake = [(100, 100), (90, 100), (80, 100)]
snake_dir = (GRID_SIZE, 0)

# Initialize food
food = (random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
        random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE)

# Initialize score
score = 0

# Load high score from file
try:
    with open("highscore.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Save high score to file before quitting
            with open("highscore.txt", "w") as file:
                file.write(str(high_score))
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake.insert(0, new_head)

    # Check for collisions with the food
    if snake[0] == food:
        score += 1
        food = (random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
                random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE)
    else:
        # If no collision with food, remove the last segment of the snake
        snake.pop()

    # Check for collisions with the walls or itself
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            snake[0] in snake[1:]):
        # If collision, reset the game
        if score > high_score:
            high_score = score
        score = 0
        snake = [(100, 100), (90, 100), (80, 100)]
        snake_dir = (GRID_SIZE, 0)

    # Draw everything on the screen
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    for segment in snake:
        pygame.draw.rect(screen, WHITE, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Draw the score on the screen
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}   High Score: {high_score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
