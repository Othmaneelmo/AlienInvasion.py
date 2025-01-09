import pygame

class Ship():
    '''
    Class to manage player ship
    '''
    def __init__(self, ai_game):
        '''
        initialize ship and starting position
        '''
        self.screen = ai_game.screen            #access screen made in __main__
        self.screen_rect = ai_game.screen.get_rect()        #retrieves the rectangular boundaries, to help with positioning

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)