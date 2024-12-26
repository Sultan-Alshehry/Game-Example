import pygame
from objects import Object
from pygame.locals import *
from pygame import Vector2

objects = []
class Player(Object):
    def __init__(self, size, position, velocity):
        super().__init__("player", size, position, velocity)

    def player_movement(self):
        # Get keys pressed for continuous movement
        keys = pygame.key.get_pressed()
        direction = 'w'
        # Update player position based on input
        movement = Vector2(0, 0)
        if keys[K_w]:  # Move up
            movement.y -= Player.velocity.y
            direction = 'w'
        if keys[K_s]:  # Move down
            movement.y += Player.velocity.y
            direction = 's'
        if keys[K_a]:  # Move left
            movement.x -= Player.velocity.x
            direction = 'a'
        if keys[K_d]:  # Move right
            movement.x += Player.velocity.x
            direction = 'd'
        # Move the player and update position
        player.move(movement)
        if keys[K_SPACE]:  # Shoot a bullet
            bullet = Object(Vector2(5, 5), player.position + player_size / 2, Vector2(0, -bullet_speed))
            objects.append(bullet)

        # Ensure player stays within screen bounds
        player.position.x = max(0, min(WIDTH - player_size.x, player.position.x))
        player.position.y = max(0, min(HEIGHT - player_size.y, player.position.y))


# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Player Class Prototype")

# Player variables
player_size = Vector2(25, 25)
player_velocity = Vector2(5, 5)  # Adjusted to a visible value
bullet_speed = 15
player_pos = Vector2(400, 300)
player = Object(size=player_size, position=player_pos, velocity=player_velocity)




# Clock for limiting FPS
clock = pygame.time.Clock()

gameOn = True
# Game loop
while gameOn:
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:  # Window close event
            gameOn = False
        elif event.type == KEYDOWN:
            # Check specific keys for actions
            if event.key == K_BACKSPACE:  # Exit on Backspace
                gameOn = False
    player.player_movement()
    
    # Update bullets
    for bullet in objects:
        bullet.move(Vector2(0, -bullet_speed))  # Bullets move upward
        if bullet.position.y < 0:  # Remove bullets that go out of bounds
            objects.remove(bullet)



    # Draw background
    screen.fill((255, 0, 0))  # Red background

    # Draw the player (a white rectangle)
    player.draw(screen)

    # Draw bullets
    for bullet in objects:
        bullet.draw(screen)
    
    # Update the display
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

pygame.quit()
