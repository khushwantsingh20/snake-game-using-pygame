import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game settings
SNAKE_SIZE = 20
SNAKE_SPEED = 5

# Clock to control the frame rate
clock = pygame.time.Clock()

# Font for the game over message
font = pygame.font.SysFont(None, 55)

# Function to display text on the screen
def show_message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH // 4, HEIGHT // 2])

# Main function to run the game
def game_loop():
    # Initial snake position and movement
    snake_pos = [100, 50]
    snake_body = [[100, 50], [80, 50], [60, 50]]
    direction = 'RIGHT'
    change_to = direction

    # Insect position
    insect_pos = [random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                  random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
    insect_spawn = True

    # Main game loop
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # Validate direction change
        direction = change_to

        # Move the snake
        if direction == 'UP':
            snake_pos[1] -= SNAKE_SIZE
        if direction == 'DOWN':
            snake_pos[1] += SNAKE_SIZE
        if direction == 'LEFT':
            snake_pos[0] -= SNAKE_SIZE
        if direction == 'RIGHT':
            snake_pos[0] += SNAKE_SIZE

        # Snake body growing mechanism: add a new block at the head
        snake_body.insert(0, list(snake_pos))

        # Check if the snake has eaten the insect
        if snake_pos[0] == insect_pos[0] and snake_pos[1] == insect_pos[1]:
            # If eaten, spawn a new insect
            insect_spawn = False
        else:
            # Remove the last block of the snake's body if no insect is eaten
            snake_body.pop()

        # Respawn insect at a random position if eaten
        if not insect_spawn:
            insect_pos = [random.randrange(1, (WIDTH // SNAKE_SIZE)) * SNAKE_SIZE,
                          random.randrange(1, (HEIGHT // SNAKE_SIZE)) * SNAKE_SIZE]
            insect_spawn = True

        # Fill screen with black
        screen.fill(BLACK)

        # Draw the snake
        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], SNAKE_SIZE, SNAKE_SIZE))

        # Draw the insect
        pygame.draw.rect(screen, RED, pygame.Rect(insect_pos[0], insect_pos[1], SNAKE_SIZE, SNAKE_SIZE))

        # Check for collisions with walls
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
                snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            show_message('Game Over!', RED)
            pygame.display.flip()
            pygame.time.sleep(2)
            pygame.quit()
            sys.exit()

        # Check for collisions with itself
        for block in snake_body[1:]:
            if snake_pos == block:
                show_message('Game Over!', RED)
                pygame.display.flip()
                pygame.time.sleep(2)
                pygame.quit()
                sys.exit()

        # Update the display
        pygame.display.update()

        # Control the game speed
        clock.tick(SNAKE_SPEED)

# Run the game
if __name__ == "__main__":
    game_loop()
