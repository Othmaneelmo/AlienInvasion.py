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

        #fullscreen Borderless
        screen_size_info = pygame.display.Info() #getting screen size informations

        self.fs_width , self.fs_height = screen_size_info.current_w , screen_size_info.current_h 

        #Maximized Window (with borders)
        self.mw_width, self.mw_height = screen_size_info.current_w - 10 ,  screen_size_info.current_h - 50

        #Default ship's speed
        self.ship_speed = 0.5
        



