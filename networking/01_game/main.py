import pygame
#setup
pygame.init()
BLACK = (0, 0,0)
WHITE = ( 255, 255, 255)

def draw_player(screen, x, y):
	pygame.draw.ellipse(screen, BLACK, [1+x, y, 10, 10], 0)
pygame.mouse.set_visible(0)
#clock for FPS:
clock = pygame.time.Clock()
#setup widt and height
size = (400,300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My aadsa pygame")

#-- Main Loop --
 
done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	pos=pygame.mouse.get_pos()
	x = pos[0]
	y=pos[1]
	screen.fill(WHITE)
	#draws player
	draw_player(screen, x, y)
	pygame.display.flip()
	clock.tick(20)
#shutdown
pygame.quit()
