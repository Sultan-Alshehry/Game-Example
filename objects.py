import pygame
from pygame import Vector2

# Define our generic object class
# give it all the properties and methods of pygame.sprite.Sprite
class Object(pygame.sprite.Sprite):
    position = Vector2(0, 0)

    def __init__(self, position):
        super(Object, self).__init__()

        self.position = position

        # Define the dimension of the surface
        # Here we are making squares of side 25px
        self.surf = pygame.Surface((25, 25))

        # Define the color of the surface using RGB color coding.
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()

    def update(self):
        pass

    def draw(self, display_screen):
        display_screen.blit(self.surf, (self.position.x, self.position.y))

class Bullet(Object):

    direction = Vector2(0, 0)

    def __init__(self, position, direction):
        super(Bullet, self).__init__(position)
        self.direction = direction

    def update(self):
        self.position += self.direction