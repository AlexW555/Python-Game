# import the pygame module, so you can use it
import pygame
import math
pygame.init()

#Define some colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255,0)
RED = (255,0,0)

PI = 3.141592653

size = (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Professor Craven's Cool Game")

#Loop until the user clicks the close buton.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#-------- Main Program Loop --------
while not done:
    # ---- Main event loop ------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit")
            done = True

            
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key")
        


# - Game logic here

# - Game Drawing here

# First clear the screen to white. Dont put draw commands above this as it
# will be erased.
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (55,50,20,25),0)
    pygame.draw.line(screen, GREEN, [0,0],[100,100],5)

    #Draw on the screen several times from 0,10 to 100,110

    y_offset = 0
    for y_offset in range(0,100,10):
        pygame.draw.line(screen, RED, [0,10+y_offset],[100,110+y_offset],5)

    for i in range(200):
        radians_x = i / 20
        radians_y = i / 6

        x = int(75*math.sin(radians_x)) + 200
        y = int(75*math.cos(radians_y)) + 200

        pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)

# --- Update the screen with what we have drawn
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


