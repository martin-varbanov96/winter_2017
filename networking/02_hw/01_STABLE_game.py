import pygame
import socket
import time

#some colors
BLACK = (0,0,0)
WHITE = (255,255,255)

#on every ip of this host
host = ''

#on this port no
port = 12345

#MAX BYTES
BYTES = 1024

#Full address
FULL_ADDRESS = (host, port)

#init socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#--=Question:=-- Is there a way to skip the part of making these variables global ?!
x_transport_cordinate = -9999
y_transport_cordinate = -9999


def draw_player(screen, x, y):
    #Just the "head" of my player figure
    pygame.draw.ellipse(screen, BLACK, [1+x,y,10,10], 0)

def position_changed(x, y):
    working_x, working_y = int(x), int(y)
    return True if working_x != int(x_transport_cordinate) or working_y != int(y_transport_cordinate) else False


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
    
    if(position_changed(x, y)):
        #Merge x and y to a string and send it to server 
        x_transport_cordinate = str(x)
        y_transport_cordinate = str(y)
        output_udp_info = x_transport_cordinate + " " + y_transport_cordinate
        output_udp_info=output_udp_info.encode('ascii')
        s.sendto(output_udp_info, FULL_ADDRESS)

        #--===TODO===--:: If no response is provided, game will freeze
        #Receives response from server and changes location of x and y 
        reposnce_server, adress = s.recvfrom(BYTES)
        working_response_server_var=reposnce_server.decode('ascii').split(' ')
        x = int(working_response_server_var[0])
        y = int(working_response_server_var[1])
    
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