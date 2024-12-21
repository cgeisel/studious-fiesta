import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
running = True

# surface
surface = pygame.Surface((100, 200))
surface.fill('darkorange')
x = 100
y = 150

# import an image
player_surface = pygame.image.load(join('images', 'player.png')).convert_alpha()
star_surface = pygame.image.load(join('images', 'star.png')).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw
    # fill window with red color
    display_surface.fill('darkgray')
    for position in star_positions:
        display_surface.blit(star_surface, position)
    
    x += 1
    display_surface.blit(player_surface, (x, y))

    pygame.display.update()

pygame.quit()