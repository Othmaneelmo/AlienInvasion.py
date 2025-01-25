import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __inti(self, ai_game):
        '''
        initialize alien and starting position
        '''
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

