import pygame
from pygame import Vector2

# Define our generic object class
# give it all the properties and methods of pygame.sprite.Sprite
class Object(pygame.sprite.Sprite):
    objects = []
    def __init__(self, name, size, position, velocity):
        super(Object, self).__init__()
        # "player", "enemy", "bullet"
        self.name = name
        self.position = position
        # creates the texture
        self.surf = pygame.Surface(size)
        # creates the "hit-box"
        self.rect = self.surf.get_rect()
        self.velocity = velocity
        self.surf.fill((200, 200, 200))
        Object.objects.append(self)

    def move(self, direction):
        self.position += direction
        self.rect.topleft = self.position  # Update the rect position



    def update(self):
        pass

    def draw(self, display_screen):
        display_screen.blit(self.surf, self.position)

    def delete(self):
        Object.objects.remove(self)