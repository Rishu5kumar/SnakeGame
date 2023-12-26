# Importing Libraries

import pygame
import time # various time-realted functions
import random # allows us to generate random numbers

# Initialize pygame
pygame.init() # This initalizes the Pygame library

#------------------

# Setting up a Gaming Display or window
width = 1200   # 1200 pixels
height = 600

# This creates a game window with specified width and height
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

#-------------------

# Colors
# Define color values using RGB value(Red , Green , blue)
white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)
green = (0,255,0)

#------------------
# Snake Properties
snake_block = 20  # size of snake in pexels
snake_speed = 10 

#---------------
# Fonts 
# 50 : font size
# None: Default
font_style = pygame.font.SysFont(None, 50)
# This line initializes a font style for rendering the text in the game


# --------------

score = 0

def show_score(score):
    score_text = font_style.render(f"Score: {score}", True, white)
    display.blit(score_text, (10, 10))
    # Blit method is used to draw the score text surface on the gaming window
    # The (10,10) tuple specifies the position of text
    
# ---------------

def snake_game():
    global score
    score = 0
    
    game_over = False  # Keeps track of whther the game is over or not
    
    game_close = False # keeps track of whther the game has been closed
    
    
    # Snake initial position
    x1 = width//2  # Initial x-coordinate of the snake
    y1 = height//2 # Initial y-coordinate of the snake
    
    x1_change = 0  # Initial change in x-coordinate (no movement)
    y1_change = 0  # Initila Change in y-coordinate (no movement)
    
    snake_list = [] # A list to store all the coordinates of the snake's body segments
    
    length_of_snake = 1 # Initial Length of the snake's body
    
    # Food Initial position
    
    food_x = round(random.randrange(0, width-snake_block) / 20) * 20
    food_y = round(random.randrange(0, height-snake_block) / 20) * 10
    
    # central loop that controls the game's progression
    while not game_over:
        
        while game_close:
            
            display.fill(black) # It fills the screen with black background
            
            message("Game Over Press Q-Quit or C-Play Again", red)
            pygame.display.update() # It updates the display to show message
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                        score=0
                        
                    if event.key == pygame.K_c:
                        snake_game()
                
    
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                    
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                    
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                    
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    
        
        # If the snake's head has reached the boundaries
        if x1 >= width or x1<0 or y1>=height or y1<0:
            game_close = True
            
        
        # updating Coordinates and clearing the screen
        
        x1 += x1_change
        y1 += y1_change
        display.fill(black)
        
        # Drawing Food and snake'head
        pygame.draw.rect(display, green, [food_x, food_y, snake_block, snake_block])
        
        # Upadate Snake's Body
        snake_head = []       
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        
        if len(snake_list) > length_of_snake:
            del snake_list[0]
            
            
    
        snake(snake_block, snake_list)
        
        
        # Score update
        show_score(score)
        pygame.display.update()  #
        
        # Food consumption:
        
        if x1 == food_x and y1==food_y:
            food_x = round(random.randrange(0, width-snake_block) / 20) * 20 
            food_y = round(random.randrange(0, height-snake_block) / 20) * 20
            score += 10
            length_of_snake += 1
            
        pygame.display.update()
        
        
        clock.tick(snake_speed)
        # It ensures that the game runs at a controlled frame rate
        
    pygame.quit()
    #quit()

# drwaing the snake's body segments on the screen
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, white, [x[0], x[1], snake_block, snake_block])
  
def message(msg, color):
    msgtext = font_style.render(msg, True, color)
    display.blit(msgtext, [width/3, height/2])
    
clock = pygame.time.Clock()
snake_game()
        
                    

                
                
                
            
        
        
            
    
    
    



