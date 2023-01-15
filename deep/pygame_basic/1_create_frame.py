import pygame

pygame.init() #초기화, necessary

# setting the size of the screen
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# setting the title of the screen
pygame.display.set_caption("GJ Game") # game name

# event loop
running = True # Is the game being played?
while running:
    for event in pygame.event.get(): # During the game, when an event occurs, execute this.
        if event.type == pygame.QUIT: # when I click the X(closing the window, quit)
            running = False

# quit the game
pygame.quit()