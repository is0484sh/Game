import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 640
window_height = 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("RPG Game")

# Define game colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the player character
player_x = 300
player_y = 400
player_width = 50
player_height = 50
player_speed = 5

player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the enemy characters
enemy_x = 100
enemy_y = 100
enemy_width = 50
enemy_height = 50
enemy_speed = 3

enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

# Define game loop variables
game_over = False
clock = pygame.time.Clock()

# Game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Update the player rectangle
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # Handle enemy movement
    if enemy_x < player_x:
        enemy_x += enemy_speed
    elif enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    elif enemy_y > player_y:
        enemy_y -= enemy_speed

    # Update the enemy rectangle
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    # Handle collisions
    if player_rect.colliderect(enemy_rect):
        game_over = True

    # Draw the game world
    window.fill(white)
    pygame.draw.rect(window, black, player_rect)
    pygame.draw.rect(window, black, enemy_rect)
    pygame.display.update()

    # Update the clock
    clock.tick(60)

# Clean up and quit Pygame
pygame.quit()
