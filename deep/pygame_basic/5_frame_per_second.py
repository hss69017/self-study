import pygame

pygame.init() #초기화, necessary

# setting the size of the screen
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# setting the title of the screen
pygame.display.set_caption("GJ Game") # game name

# FPS
clock = pygame.time.Clock()

# opening the background image
background = pygame.image.load("/Users/gunju/Desktop/self study/python/deep/pygame_basic/love_background.jpeg")

# calling the character(sprite)
character = pygame.image.load("/Users/gunju/Desktop/self study/python/deep/pygame_basic/busan_character.jpeg")
character_size = character.get_rect().size # getting the size of the image
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

# coordinate
to_x = 0
to_y = 0

# moving speed
character_speed = 0.6

# event loop
running = True # Is the game being played?
while running:
    dt = clock.tick(30) # setting the fps
    # print("fps: " + str(clock.get_fps()))

    for event in pygame.event.get(): # During the game, when an event occurs, execute this.
        if event.type == pygame.QUIT: # when I click the X(closing the window, quit)
            running = False

        if event.type == pygame.KEYDOWN: # checking whether I press the keyboard
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # stop pressing the keyboard
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # 'dt': clock.tick(~), '* dt': regardless of fps, fix the speed of the game
    character_y_pos += to_y * dt

    # limit the moving place of the character
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    screen.blit(background, (0, 0)) # drawing the background

    screen.blit(character, (character_x_pos, character_y_pos)) # drawing the character
    
    pygame.display.update() # drawing the background continuously

# quit the game
pygame.quit()