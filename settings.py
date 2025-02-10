import pygame

class Settings():
    '''
    Class to store all settings 
    '''
    def __init__(self):
        #Screen Settings
        self.bg_color = (5, 5, 30)

        #default window Dimensions
        self.screen_width = 1200
        self.screen_height = 800

        #Default ship's speed
        self.ship_speed = 0.3

        #bullet
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullet_allowed = 10 

        #Alien settings
        self.alien_speed = 0.1
        self.squadron_drop_speed = 1
        self.squadron_direction = 1 #1 is right, -1 is left
        



