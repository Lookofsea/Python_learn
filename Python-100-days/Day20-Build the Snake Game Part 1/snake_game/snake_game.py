
import pygame
import random

# initialize pygame
pygame.init()

# set the screen size
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# set the title of the game window
pygame.display.set_caption('Snake Game')

# set the game clock
clock = pygame.time.Clock()

# set the font for the game
font = pygame.font.SysFont('Arial', 30)

# set the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# set the game variables    
snake_speed = 10
snake_block = 10
snake_list = []
food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
direction = 'RIGHT'


# define the snake function
def snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, green, [x, y, snake_block, snake_block])


# define the food function
def food(food_x, food_y):
    pygame.draw.rect(screen, red, [food_x, food_y, snake_block, snake_block])


# define the game over function
def game_over():
    game_over_text = font.render('Game Over!', True, red)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 4)
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()
    quit()


# main game loop
while True:
    # set the screen background
    screen.fill(black)

    # check for the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # check if the arrow keys are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'

    # move the snake
    if direction == 'RIGHT':
        snake_x = snake_list[-1][0] + snake_block
        snake_y = snake_list[-1][1]
    elif direction == 'LEFT':
        snake_x = snake_list[-1][0] - snake_block
        snake_y = snake_list[-1][1]
    elif direction == 'UP':
        snake_x = snake_list[-1][0]
        snake_y = snake_list[-1][1] - snake_block
    elif direction == 'DOWN':
        snake_x = snake_list[-1][0]
        snake_y = snake_list[-1][1] + snake_block

    # check if the snake has eaten the food
    if snake_x == food_x and snake_y == food_y:
        food_x = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        food_y = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
        snake_length = len(snake_list)
        snake_list.append((0, 0))
        for i in range(snake_length - 1, 0, -1):
            snake_list[i] = (snake_list[i - 1][0], snake_list[i - 1][1])

    # check if the snake has hit the boundaries
    if snake_x >= screen_width or snake_x < 0 or snake_y >= screen_height or snake_y < 0:
        game_over()

    # check if the snake has hit itself
    for x, y in snake_list[:-1]:
        if x == snake_x and y == snake_y:
            game_over()

    # update the snake list
    snake_list.append((snake_x, snake_y))
    del snake_list[0]

    # draw the snake and the food
    snake(snake_block, snake_list)
    food(food_x, food_y)

    # update the screen
    pygame.display.flip()

    # set the game clock
    clock.tick(snake_speed)