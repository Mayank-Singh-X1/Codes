import sys
import pygame
class AlineInvasion:
    def __inti__(self):
        pygame.init()  #initializes the game and create egame resources
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()