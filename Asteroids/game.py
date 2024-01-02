import pygame
import random 

class Asteroids:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Asteroids")

        self.screen = pygame.display.set_mode((800, 600))
    
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
        self.screen.fill((0, 0, 128))
        x = random.randint(10, 790)
        y = random.randint(10, 590)
        r = random.randint(20, 50)
        pygame.draw.circle(self.screen, (188, 188, 188), (x, y), r)
        pygame.display.flip()
        pygame.display.flip()