import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''
    Class to manage player ship
    '''
    def __init__(self, ai_game):
        '''
        initialize ship and starting position
        '''
        super().__init__()
        self.screen = ai_game.screen            #share the same screen used in __main__
        self.screen_rect = ai_game.screen.get_rect()        #retrieves the rectangular boundaries, to help with positioning
        self.settings = ai_game.settings        #share the same screen used in __main__

        self.image = pygame.image.load("images/ship.bmp")       #importing image
        self.rect = self.image.get_rect()       #retrieve the rectangular boundaries for the image, to help with positioning the ship
        self.rect.midbottom = self.screen_rect.midbottom     #placing ship in midbottom of screen

        #store decimal value for ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Movement flags
        self.moving_right = False       #not miving by default
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    
    def update(self):
        '''
         Update the ship's position according to the moving flag value
        '''
        #Update ship's x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:       #if falg = True and ship not at the border of screen yet
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

        invisible_wall_top = self.screen_rect.top + 500 
        #Update ship's y value, not rect
        if self.moving_up and self.rect.top > invisible_wall_top:       #if falg = True and ship not at the border of screen yet
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)


    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def blitme(self):
        self.screen.blit(self.image, self.rect)     #allow ship surface to be placed on screen surface
        