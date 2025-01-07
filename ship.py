import pygame

class Ship():
    '''
    Class to manage player ship
    '''
    def __init__(self, ai_game):
        '''
        initialize ship and starting position
        '''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()        #make rectangle of the ship object, to help with positioning

        self.image = pygame.image.load("images/ship.bmp")
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blitme(self.image, self.screen)