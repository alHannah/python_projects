import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 200, 200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pixel Art Display")

# Define your pixel art
pixel_art = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0]
]

# Set the pixel size and colors
pixel_size = 40
pixel_color = (255, 255, 255)  # white

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill((0, 0, 0))  # black

    # Draw the pixel art
    for y, row in enumerate(pixel_art):
        for x, pixel in enumerate(row):
            if pixel == 1:
                pygame.draw.rect(screen, pixel_color, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))

    # Update the display
    pygame.display.flip()

    # Add a small delay to control the frame rate
    pygame.time.delay(100)  # in milliseconds
