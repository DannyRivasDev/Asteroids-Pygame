import pygame
import random

pygame.init()
pygame.display.set_caption("Asteroids")
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    screen.fill((0, 0, 128))
    x = random.randint(10, 790)
    y = random.randint(10, 590)
    r = random.randint(20, 50)
    pygame.draw.circle(screen, (188, 188, 188), (x, y), r)
    pygame.display.flip()