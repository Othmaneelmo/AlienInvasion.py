import sys #tools to exit the game when the player quits
import pygame #contains functionalities to make the game
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'

from settings import Settings
from ship import Ship


class AlienInvasion:
    '''
    class to manage overall assets and behaviors
    '''
    
    def __init__(self):
        '''
        initialize game and create ressources
        '''
        pygame.init()      #initialize pygame modules

        self.settings = Settings()      #create settings instance  
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  #set screen size using Settings

        self.bg_color = (self.settings.bg_color)      #set background color
        pygame.display.set_caption("Alien Invasion")
        #make Ship()instace with AlienInvasion as argument
        self.ship = Ship(self)

        print("Ship rect:", self.ship.rect)
        print("Ship x:", self.ship.x)
        print("Screen dimensions:", self.screen.get_rect().size)




    def run_game(self):
        '''start main loop for game'''
        while True:
            #watch for any keyboard or mouse inputs
            self._check_events()
            self.ship.update()
            self._update_screen()

           

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                #KEY DOWN EVENT
                elif event.type == pygame.KEYDOWN:
                     self._event_check_keydown(event)

                #KEY UP EVENT
                elif event.type == pygame.KEYUP:
                     self._event_check_keyup(event)

                
    def _event_check_keydown(self, event):
        #right arrow / D --> move right
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        #left arrow / A --> move left
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = True
        #backspace --> QUIT
        if event.key == pygame.K_BACKSPACE:
             sys.exit()
        # F11 --> Full-screen toggle
        if event.key == pygame.K_F11:
             self._toggle_fullscreen_borderless()
        if event.key == pygame.K_F10:
             self._toggle_maximized_window()

    def _toggle_fullscreen_borderless(self):
        #Exit FULLSCREEN
        if self.screen.get_flags() & pygame.FULLSCREEN:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
            
        #Enter FULLSCREEN
        else:
            #save default screen sizes
            #self.settings.screen_width, self.settings.screen_height = self.screen.get_rect().width, self.screen.get_rect().height

            self.screen = pygame.display.set_mode((self.settings.fs_width, self.settings.fs_height), pygame.FULLSCREEN)

            print("Ship rect:", self.ship.rect)
            print("Ship x:", self.ship.x)
            print("Screen dimensions:", self.screen.get_rect().size)            
            

            #print(self.ship.rect , self.ship.rect.x , self.ship.rect.y)
            #print(self.screen.get_rect())

        #Get New Screen Dimensions
        new_screen_rect = self.screen.get_rect()
        self.ship.screen_rect = new_screen_rect

        scale_x = new_screen_rect.width / self.settings.screen_width
        scale_y = new_screen_rect.height / self.settings.screen_height

        self.ship.rect.x = int(self.ship.rect.x * scale_x)
        self.ship.rect.y = int(self.ship.rect.y * scale_y)
        self.ship.x = float(self.ship.rect.x)
        self.ship.y = float(self.ship.rect.y)       

        self.settings.fs_width = new_screen_rect.width
        self.settings.fs_height = new_screen_rect.height

            
    def _toggle_maximized_window():
         pass
    
    def _event_check_keyup(self, event):
        #right arrow / D --> move right
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        #left arrow / A --> move left
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False

    
         

    def _update_screen(self):
            #redraw the screen during each loop iteration
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            #make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':      #only run when script is ran directly (ex: not when imported)
    #make game instance, run game
    ai = AlienInvasion()
    ai.run_game()


