import pygame
import random 
from models import GameObject
from utils import load_sprite

class Asteroids:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")

        self.screen = pygame.display.set_mode((1080, 1080))
        self.background = load_sprite("space", False)
        self.clock = pygame.time.Clock()
        self.spaceship = GameObject(
            (540, 540), load_sprite("spaceship"), (0, 0)
        )
        self.asteroid = GameObject(
            (540, 540), load_sprite("asteroid"), (1, 0)
        )
    
    def main_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                quit()
    
    def _game_logic(self):
        self.spaceship.move()
        self.asteroid.move()

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        self.spaceship.draw(self.screen)
        self.asteroid.draw(self.screen)
        pygame.display.flip()
        print("Collides:", self.spaceship.collides_with(self.asteroid))