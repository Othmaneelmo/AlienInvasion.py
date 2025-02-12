import pygame

class Settings():
    '''
    Class to store all settings 
    '''
    def __init__(self):
        """Initialize game static settings"""
        #Screen Settings
        self.bg_color = (5, 5, 30)

        #default window Dimensions
        self.screen_width = 1200
        self.screen_height = 800

        #ship settings
        self.ship_speed = 0.1
        self.ship_limit = 3


        #bullet
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullet_allowed = 5

        #Alien settings
        self.alien_speed = 0.1
        self.squadron_drop_speed = 10
        #How quickly the game speeds up
        self.speedup_scale = 1.2

        #How quickly the alien points value increases
        self.score_value = 1.5
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize settings that change through out the game"""
        self.ship_speed = 0.2
        self.bullet_speed = 0.5
        self.alien_speed = 0.1
        self.squadron_direction = 1 #1 is right, -1 is left
        self.alien_points = 50
    
    def increase_speed(self):
        """Increase Speed Settings"""
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_value)
        print("Current alien point", self.alien_points)

    


        



