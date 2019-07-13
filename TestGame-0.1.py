# import the pygame module, so you can use it
import pygame
import random
pygame.init()

#Define some colours
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255,0)
RED = (255,0,0)

PI = 3.141592653

size = (400,400)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Professor Craven's Cool Game")

#Loop until the user clicks the close buton.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


rect_x = 50
rect_y = 50

rect_change_x = 5
rect_change_y = 5

snow_list = []

for i in range(50):
        x = random.randrange(0,400)
        y = random.randrange(0,400)
        snow_list.append([x,y])

        
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

    
    pygame.draw.rect(screen, BLACK, (rect_x,rect_y,50,50))
    pygame.draw.rect(screen, RED, (rect_x + 10,rect_y + 10,30,30))
    rect_x += rect_change_x
    rect_y += rect_change_y

    if rect_y > 350 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 350 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    

    for i in range(len(snow_list)):
        pygame.draw.circle(screen, BLACK, snow_list[i], 2)

        snow_list[i][1] += 1

        if snow_list[i][1] > 400:
            #Reset it to just above the top of the screen
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            #Give new X Position
            x = random.randrange(0,400)
            snow_list[i][0] = x
        
    


    score = 20
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Score: " + str(score), True, BLACK)

    screen.blit(text, [250,250])
    
    #Draw on the screen several times from 0,10 to 100,110


# --- Update the screen with what we have drawn
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


