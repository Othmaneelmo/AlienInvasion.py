import sys #tools to exit the game when the player quits
import pygame #contains functionalities to make the game
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

        pygame.init()      #initialize pygame imported modules
        self.settings = Settings()      #create settings instance 

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_lenght))      #set screen size using Settings
        self.bg_color = (self.settings.bg_color)      #set background color

        #make Ship()instace with AlienInvasion as argument
        self.ship = Ship(self)



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
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _event_check_keyup(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
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
