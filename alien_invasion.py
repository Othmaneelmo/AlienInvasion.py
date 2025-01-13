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
        pygame.init()      #initialize pygame modules
        self.settings = Settings()      #create settings instance 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))  #set screen size using Settings

        self.bg_color = (self.settings.bg_color)      #set background color
        pygame.display.set_caption("Alien Invasion")
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
        #right arrow / D --> move right
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = True
        #left arrow / A --> move left
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = True
        #backspace --> QUIT
        if event.key == pygame.K_BACKSPACE:
             sys.exit()
        # F11 --> Full-screen toggle
        if event.key == pygame.K_F11:
             self._toggle_fullscreen()

    def _toggle_fullscreen(self):
        #Exit FULLSCREEN
        if self.screen.get_flags() & pygame.FULLSCREEN:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        #Enter FULLSCREEN
        else:
            self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

        #Get New Screen Dimensions
        new_screen_rect = self.screen.get_rect()
        new_width = new_screen_rect.width
        new_height = new_screen_rect.height
        
        #Scale new ship position proportionnally to new screen size
        self.ship.rect.x = int(self.ship.rect.x * new_width / self.settings.screen_width)
        self.ship.rect.y = int(self.ship.rect.y * new_height / self.settings.screen_height)

        # Update the settings with the new dimensions
        self.settings.screen_width = new_width
        self.settings.screen_height = new_height

        #Update ship's boundaries
        self.ship.screen_rect = new_screen_rect
            
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
