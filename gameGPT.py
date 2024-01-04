import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Clock for controlling the frame rate
clock = pygame.time.Clock()

# Player
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - 2 * PLAYER_SIZE
player_speed = 10

# Enemies
enemies = []
for _ in range(10):
    enemy = {
        "x": random.randint(0, WIDTH - ENEMY_SIZE),
        "y": random.randint(50, 200),
        "speed": random.randint(2, 4)
    }
    enemies.append(enemy)

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += player_speed

    # Update enemy positions
    for enemy in enemies:
        enemy["y"] += enemy["speed"]
        if enemy["y"] > HEIGHT:
            enemy["y"] = 0
            enemy["x"] = random.randint(0, WIDTH - ENEMY_SIZE)
            score += 1

    # Check for collisions
    for enemy in enemies:
        if (
            player_x < enemy["x"] + ENEMY_SIZE and
            player_x + PLAYER_SIZE > enemy["x"] and
            player_y < enemy["y"] + ENEMY_SIZE and
            player_y + PLAYER_SIZE > enemy["y"]
        ):
            running = False

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, [player_x, player_y, PLAYER_SIZE, PLAYER_SIZE])

    for enemy in enemies:
        pygame.draw.rect(screen, WHITE, [enemy["x"], enemy["y"], ENEMY_SIZE, ENEMY_SIZE])

    # Draw score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
