import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        '''
        Create Bullet object at Ship's position
        '''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #Create bullet rect at (0,0), then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #Store bullet position as float value
        self.y = float(self.rect.y)

    
    def update(self):
        #self.rect.x = self.x       #allow bullet to go sideways depending on ship movement and speed
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y        #update rect position

    def draw_bullet(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            self.rect
        )
