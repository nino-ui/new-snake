import pygame
import time
import random

pygame.init()

# define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# set the window dimensions
width = 600
height = 400

# create the window
dis = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game by Edureka')

# set the game speed
clock = pygame.time.Clock()

# set the block size
block_size = 10

# define the font style for displaying the score
font_style = pygame.font.SysFont(None, 30)

# define a function to display the score
def display_score(score):
    value = font_style.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# define a function to draw the snake
def draw_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], block_size, block_size])

# define the game loop function
def game_loop():
    game_over = False
    game_close = False

    # set the starting position of the snake
    x1 = width / 2
    y1 = height / 2

    # set the initial change in position of the snake
    x1_change = 0
    y1_change = 0

    # create the food at a random location
    food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0

    # create a list to store the segments of the snake
    snake_list = []
    length_of_snake = 1

    # start the game loop
    while not game_over:

        # if the game has ended, ask the player if they want to play again or quit
        while game_close == True:
            dis.fill(black)
            game_over_font = pygame.font.SysFont(None, 40)
            game_over_text = game_over_font.render("Game Over!", True, red)
            dis.blit(game_over_text, [width / 3, height / 3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # handle the player's input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # update the snake's position
        x1 += x1_change
        y1 += y1_change

        # check if the snake has hit the boundaries of the window
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # draw the food
        pygame.draw.rect(dis, blue, [food_x, food_y, block_size, block_size])

        # update the snake's segments
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # draw the snake
        draw_snake(block_size, snake_list)

        # display the score
        display_score(length_of_snake - 1)

        # update the display
        pygame.display.update()

        # check if the snake has collided with the food
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
            length_of_snake += 1

        # set the game speed
        clock.tick(20)

    # quit pygame and exit the program
    pygame.quit()
    quit()

# start the game
game_loop()
