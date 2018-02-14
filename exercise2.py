#!/usr/bin/env python
'''

For this exercise, draw randomly-sized, randomly-colored, rectangles in random locations on the screen
It might be helpful to define a list of colors you want to use
hint: where you place the screen.fill(black) will affect whether or not the squares persist on the screen

'''
import sys, pygame, random
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' 

screen_size = (800,600)
FPS = 60
black = (0,0,0)
orange = (255,150,0)
red = (255,0,0)
green = (0,255,0)
dark_green = (0,128,0)
yellow = (255,255,0)
purple = (150, 15, 150)
blue = (0, 40, 255)
indigo = (0, 0, 100)

def main():
        pygame.init()
        screen = pygame.display.set_mode(screen_size)
        clock = pygame.time.Clock()

        (x,y,width,height) = (100,100,50,50)
        screen.fill(black)
        while True:
                clock.tick(FPS)
                (x,y,width,height) = (random.randint(1,800),random.randint(1,600),random.randint(10,500),random.randint(10,500))

                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                color = random.choice((indigo, orange, red, green, dark_green, yellow, purple, blue))
                pygame.draw.rect(screen, color, (x,y,width,height))
                pygame.display.flip()

if __name__ == '__main__':
	main()
