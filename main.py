import pygame
# import pygame.locals for easier
# access to key coordinates
from pygame.locals import *
from pygame.math import Vector2

import objects
from bullet import Bullet

def create_object(new_object):
    objects.append(new_object)
    return new_object

def remove_object(object_to_remove):
    objects.remove(object_to_remove)

# initialize pygame
pygame.init()

# Define the dimensions of screen object
screen = pygame.display.set_mode((800, 600))

# instantiate all square objects
player = Player(size=player_size, position=player_pos, velocity=player_velocity)

create_object(Object(Vector2(0, 0)))
create_object(Bullet(Vector2(0.1, 0.1), Vector2(0.2, 0.2)))

gameOn = True
# Our game loop
while gameOn:
    # for loop through the event queue
    for event in pygame.event.get():

        # Check for KEYDOWN event
        if event.type == KEYDOWN:

            # If the Backspace key has been pressed set
            # running false to exit the main loop
            if event.key == K_BACKSPACE:
                gameOn = False

        # Check for QUIT event
        elif event.type == QUIT:
            gameOn = False

    # Draw background
    screen.fill((255, 255, 255))

    # Update all objects
    for obj in objects:
        obj.update()

    # Draw all objects
    for obj in objects:
        obj.draw(screen)


    # Update the display using flip
    pygame.display.flip()