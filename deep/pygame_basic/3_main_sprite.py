import pygame

pygame.init() #초기화, necessary

# setting the size of the screen
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# setting the title of the screen
pygame.display.set_caption("GJ Game") # game name

# opening the background image
background = pygame.image.load("/Users/gunju/Desktop/self study/python/deep/pygame_basic/love_background.jpeg")

# calling the character(sprite)
character = pygame.image.load("/Users/gunju/Desktop/self study/python/deep/pygame_basic/busan_character.jpeg")
character_size = character.get_rect().size # getting the size of the image
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# event loop
running = True # Is the game being played?
while running:
    for event in pygame.event.get(): # During the game, when an event occurs, execute this.
        if event.type == pygame.QUIT: # when I click the X(closing the window, quit)
            running = False

    screen.blit(background, (0, 0)) # drawing the background

    screen.blit(character, (character_x_pos, character_y_pos)) # drawing the character
    
    pygame.display.update() # drawing the background continuously

# quit the game
pygame.quit()