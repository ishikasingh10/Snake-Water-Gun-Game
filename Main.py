import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up game window
window = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake Water Gun Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Load images for Snake, Water, Gun
snake_img = pygame.image.load('snake.png')
water_img = pygame.image.load('water.png')
gun_img = pygame.image.load('gun.png')

# Set up fonts
font = pygame.font.SysFont("comicsansms", 24)
large_font = pygame.font.SysFont("comicsansms", 36)

# Game variables
player_score = 0
rounds = 5
streak = 0
choices = ['Snake', 'Water', 'Gun']

def display_text(text, color, y_position):
    label = font.render(text, True, color)
    window.blit(label, (250, y_position))

def game_round(player_choice):
    global player_score, streak

    computer_choice = random.choice(choices)
    
    # Check for winner
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (player_choice == 'Snake' and computer_choice == 'Water') or \
         (player_choice == 'Water' and computer_choice == 'Gun') or \
         (player_choice == 'Gun' and computer_choice == 'Snake'):
        result = "You win!"
        player_score += 1
        streak += 1
        if streak == 3:
            player_score += 2  # Streak bonus
    else:
        result = "You lose!"
        streak = 0  # Reset streak on loss
    
    return result, computer_choice

def game_loop():
    global player_score, streak

    run_game = True
    player_choice = ''
    game_result = ''
    computer_choice = ''
    
    while run_game:
        window.fill(WHITE)
        display_text("Snake Water Gun Game", BLUE, 20)
        display_text(f"Score: {player_score}", GREEN, 60)
        display_text(f"Streak: {streak}", RED, 100)

        if game_result:
            display_text(game_result, BLACK, 200)

        if player_choice == 'Snake':
            window.blit(snake_img, (150, 250))
        elif player_choice == 'Water':
            window.blit(water_img, (150, 250))
        elif player_choice == 'Gun':
            window.blit(gun_img, (150, 250))

        if computer_choice == 'Snake':
            window.blit(snake_img, (350, 250))
        elif computer_choice == 'Water':
            window.blit(water_img, (350, 250))
        elif computer_choice == 'Gun':
            window.blit(gun_img, (350, 250))

        pygame.display.update()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    player_choice = 'Snake'
                elif event.key == pygame.K_w:
                    player_choice = 'Water'
                elif event.key == pygame.K_g:
                    player_choice = 'Gun'

                if player_choice:
                    game_result, computer_choice = game_round(player_choice)

        pygame.time.delay(1000)

    pygame.quit()
    sys.exit()

# Run the game
game_loop()
