import pygame
import random 
from utils import load_sprite

class Asteroids:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")

        self.screen = pygame.display.set_mode((1080, 1080))
        self.background = load_sprite("space", False)
    
    def main_loop(self):
        while True:
            self._handle_input()
            self._game_logic()
            self._draw()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    
    def _game_logic(self):
        pass

    def _draw(self):
        self.screen.blit(self.background, (0, 0))
        x = random.randint(10, 1070)
        y = random.randint(10, 1070)
        r = random.randint(20, 50)
        pygame.draw.circle(self.screen, (188, 188, 188), (x, y), r)
        pygame.display.flip()