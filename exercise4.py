#!/usr/bin/env python
'''

For this exercise, draw a circle wherever the user clicks the mouse

'''
import sys, pygame,random
from datetime import datetime
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

screen_size = (800,600)
FPS = 60
black = (0,0,0)
white = (255,255,255)
orange = (255,150,0)
red = (255,0,0)
green = (0,255,0)
dark_green = (0,128,0)
yellow = (255,255,0)
purple = (150, 15, 150)
blue = (0, 40, 255)
indigo = (0, 0, 100)
colors = (white,orange,red,green,dark_green,yellow,purple,blue,indigo)

def main():
        pygame.init()
        screen = pygame.display.set_mode(screen_size)
        font = pygame.font.SysFont("arial",64)
        clock = pygame.time.Clock()

        (x,y,radius) = (100,100,20)
        screen.fill(black)
        while True:
                clock.tick(FPS)

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                        if event.type == pygame.MOUSEBUTTONUP:
                                pos = pygame.mouse.get_pos()
                                pygame.draw.circle(screen, random.choice(colors), pos, 100)
        
                pygame.display.flip()

if __name__ == '__main__':
	main()
