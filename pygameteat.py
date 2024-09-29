import pygame
import math
# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
x = 50
y = 50
radius = 50
vel = 5
isjump = False
jumpcount = 10
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frames
    screen.fill("white")

    # RENDER YOUR GAME HERE
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel
    if keys[pygame.K_d] and x < 500:
        x += vel
    if not(isjump):
        if keys[pygame.K_w] and y > vel:
            y -= vel
        if keys[pygame.K_s] and y < 500:
            y += vel
        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1
        else:
            isjump = False
            jumpcount = 10
    pygame.draw.circle(screen, (250,0,0) , (x,y) , 50)
    pygame.draw.line(screen,(0,0,0),(0,150),(500,150),5)
    
    pygame.display.update
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
pygame.quit