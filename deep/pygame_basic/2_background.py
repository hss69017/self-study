import pygame

pygame.init() #초기화, necessary

# setting the size of the screen
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# setting the title of the screen
pygame.display.set_caption("GJ Game") # game name

# opening the background image
background = pygame.image.load("/Users/gunju/Desktop/self study/python/deep/pygame_basic/love.jpeg")

# event loop
running = True # Is the game being played?
while running:
    for event in pygame.event.get(): # During the game, when an event occurs, execute this.
        if event.type == pygame.QUIT: # when I click the X(closing the window, quit)
            running = False

    # screen.fill((0, 0, 255)) # drawing the background with rgb
    screen.blit(background, (0, 0)) # drawing the background
    
    pygame.display.update() # drawing the background continuously

# quit the game
pygame.quit()