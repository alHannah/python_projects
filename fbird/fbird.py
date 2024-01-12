import pygame
import sys
import random
import os

# Set the working directory to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Initialize Pygame
pygame.init()

# Set up game constants
WIDTH, HEIGHT = 300, 600
FPS = 60

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Set up screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Initialize clock
clock = pygame.time.Clock()

# Load images
bird_image = pygame.image.load("bird.png")
pipe_image = pygame.image.load("pipe.png")
background_image = pygame.image.load("background.png")
ground_image = pygame.image.load("ground.png")

# Resize images
bird_image = pygame.transform.scale(bird_image, (50, 50))
pipe_image = pygame.transform.scale(pipe_image, (100, 100))
ground_image = pygame.transform.scale(ground_image, (WIDTH, 100))

# Define game variables
bird_y = HEIGHT // 2
bird_speed = 5
bird_gravity = 1

pipes = []

score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -12  # Jump

    # Move bird
    bird_speed += bird_gravity
    bird_y += bird_speed

    # Spawn pipes
    if random.randint(1, 100) < 5:
        pipe_height = random.randint(100, 400)
        pipes.append({"x": WIDTH, "height": pipe_height})

    # Move pipes
    for pipe in pipes:
        pipe["x"] -= 5

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe["x"] > -100]

    # Check for collisions
    bird_rect = pygame.Rect(50, bird_y, 50, 50)
    for pipe in pipes:
        pipe_rect_upper = pygame.Rect(pipe["x"], 0, 100, pipe["height"])
        pipe_rect_lower = pygame.Rect(pipe["x"], pipe["height"] + 150, 100, HEIGHT - pipe["height"] - 150)

        if bird_rect.colliderect(pipe_rect_upper) or bird_rect.colliderect(pipe_rect_lower) or bird_y > HEIGHT - 100:
            # If collision, reset the game
            bird_y = HEIGHT // 2
            bird_speed = 5
            pipes = []
            score = 0

    # Check for scoring
    for pipe in pipes:
        if pipe["x"] == 50:
            score += 1

    # Draw everything on the screen
    screen.blit(background_image, (0, 0))
    screen.blit(bird_image, (50, bird_y))
    for pipe in pipes:
        screen.blit(pipe_image, (pipe["x"], 0))
        screen.blit(pygame.transform.flip(pipe_image, False, True), (pipe["x"], pipe["height"] + 150))
    screen.blit(ground_image, (0, HEIGHT - 100))

    # Draw the score on the screen
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
