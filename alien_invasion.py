import sys #tools to exit the game when the player quits
import pygame #contains functionalities to make the game
#import os
#os.environ['SDL_VIDEO_CENTERED'] = '1'

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien 


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
        pygame.display.set_caption("Alien Invasion") #change window caption
        #make Ship()instace with AlienInvasion as argument
        self.ship = Ship(self)      #create ship instance
        self.bullets = pygame.sprite.Group()        #add bullet sprites group

        self.aliens = pygame.sprite.Group()
        self._create_squadron()


    def run_game(self):
        '''start main loop for game'''
        while True:
            #watch for any keyboard or mouse inputs
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
        
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

        #backspace --> QUIT
        if event.key == pygame.K_BACKSPACE:
             sys.exit()


    def _event_check_keyup(self, event):
        #right arrow / D --> move right
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        #left arrow / A --> move left
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.ship.moving_down = False


    def _fire_bullet(self):
        '''
        Create new bullet and add it to bullets group
        '''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    

    def _create_squadron(self):
        #make an alien
        alien = Alien(self)

        #spacing between aliens is 1 alien width
        alien_width = alien.rect.width
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // 2 * alien_width
        
        #Create 1st row of aliens
        for alien_number in range(number_aliens_x):
            alien = Alien(self)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

        


    def _update_bullets(self):
        '''
        Update bullet position and remove old ones
        '''
        self.bullets.update()
        #remove bullets when they reach top of screen
        for bullet in self.bullets.copy():      #iterate over a copy to safely remove bullets without affecting original list
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)


    def _update_screen(self):
            #redraw the screen during each loop iteration
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            #make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':      #only run when script is ran directly (ex: not when imported)
    #make game instance, run game
    ai = AlienInvasion()
    ai.run_game()


