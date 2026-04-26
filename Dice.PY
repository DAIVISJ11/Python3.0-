import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dice Game (Pygame)")

# Load dice images
dice_images = {
    1: pygame.image.load("Dice 1.png"),
    2: pygame.image.load("Dice 2.png"),
    3: pygame.image.load("Dice 3.png"),
    4: pygame.image.load("Dice 4.png"),
    5: pygame.image.load("Dice 5.jpg"),
    6: pygame.image.load("Dice 6.png"),
}

# Resize images (optional)
for key in dice_images:
    dice_images[key] = pygame.transform.scale(dice_images[key], (150, 150))

# Starting dice values
player_roll = 1
computer_roll = 1

# Font
font = pygame.font.SysFont("Arial", 32)

def draw_screen():
    screen.fill((30, 30, 30))

    # Draw dice
    screen.blit(dice_images[player_roll], (100, 120))
    screen.blit(dice_images[computer_roll], (350, 120))

    # Text
    title = font.render("Press SPACE to Roll Dice", True, (255, 255, 255))
    screen.blit(title, (140, 30))

    result_text = f"You: {player_roll}   |   Computer: {computer_roll}"
    result = font.render(result_text, True, (255, 255, 0))
    screen.blit(result, (160, 300))

    pygame.display.update()

# Game loop
running = True
while running:
    draw_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Roll dice when SPACE is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player_roll = random.randint(1, 6)
                computer_roll = random.randint(1, 6)

pygame.quit()
sys.exit()

