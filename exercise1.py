#!/usr/bin/env python
'''

For every line, please add a comment describing what it does. 

Try to describe each line within the context of the program as a whole, rather than just mechanically

Feel free to alter the parameters to see how things change. That can be a great way to be able to intuit what is supposed to be happening

I will do the first two lines for you as an example


'''
import sys, pygame	# imports the sys and pygame modules so they can be used in this program
assert sys.version_info >= (3,4), 'This script requires at least Python 3.4' # requires that the Python 3.4 (or higher version) interpreter is being used; i.e., not compatible with Python 2

screen_size = (800,600) # sets a variable to a tuple.
FPS = 60 # sets a variable for fps. An integer

def main(): #defines a function called main. This is the main method, meaning it is the function that is used to run a program.
	pygame.init() #This utilizes a method from pygame. Likely initializes the screen.
	screen = pygame.display.set_mode(screen_size) # Defines screen size for the pygame display, using a pygame method, based on the screen_size variable defined earlier.
	clock = pygame.time.Clock() # instantiates an object of the clock class.

	while True:
		clock.tick(FPS) # sets the clocks tick to the FPS variable.
		screen.fill((0,0,0))  # fills the screen, as defined earlier, with one color. Specifically black in this case.

		for event in pygame.event.get(): # For each event in pygame, this is run through. 
			if event.type == pygame.QUIT: # if the event is found to be the event pygame.QUIT,
				pygame.quit() # do method pygame.quit, which quits
				sys.exit(0) # and do sys.exit()

		pygame.display.flip() # flips switches all at once so the image is drawn all at once on the screen.

if __name__ == '__main__': # if the program is being run directly, this with run the main method. If this is imported, it instead does not run it.
	main() # calls the main method.
