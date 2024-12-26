import pygame
import objects
from pygame.locals import *

class Bullet(objects):
    def __init__(self, position, direction):
        def __init__(self, size, position, velocity):
            super().__init__("bullet", size, position, velocity)

    def destroy(self):
        if