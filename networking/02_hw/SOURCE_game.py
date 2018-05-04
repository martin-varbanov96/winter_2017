import pygame

#some colors
BLACK = (0,0,0)
WHITE = (255,255,255)

def draw_player(screen, x, y):
    #Just the "head" of my player figure
    pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0)

#setup
pygame.init()

#setup the width and height of the window
size = (400,300)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My first pygame game")

#hide the mouse
pygame.mouse.set_visible(0)

#for limiting the FPS
clock = pygame.time.Clock()

#--- MAIN LOOP ---
done = False
while not done:
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If he clicked the window close button
            done = True

    #place my player where the mouse cursor is
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    #the background
    screen.fill(WHITE)

    #draw the player
    draw_player(screen, x, y)

    #screen refresh
    pygame.display.flip()

    #20 FPS should do
    clock.tick(20)

#A gracefull shutdown
pygame.quit()