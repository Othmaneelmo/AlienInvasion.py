import pygame

class Ship():
    '''
    Class to manage player ship
    '''
    def __init__(self, ai_game):
        '''
        initialize ship and starting position
        '''
        self.screen = ai_game.screen            #share the same screen used in __main__
        self.screen_rect = ai_game.screen.get_rect()        #retrieves the rectangular boundaries, to help with positioning
        self.settings = ai_game.settings        #share the same screen used in __main__

        self.image = pygame.image.load("images/ship.bmp")       #importing image
        self.rect = self.image.get_rect()       #retrieve the rectangular boundaries for the image, to help with positioning the ship
        self.rect.midbottom = self.screen_rect.midbottom        #placing ship in midbottom of screen

        #store decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        #Movement flag
        self.moving_right = False       #not miving by default
        self.moving_left = False

    def update(self):
        '''
         Update the ship's position according to the moving flag value
        '''
        #Update ship's x value, not rect
        if self.moving_right:       #if falg = True
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)     #allow ship surface to be placed on screen surface