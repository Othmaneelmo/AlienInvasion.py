import sys #tools to exit the game when the player quits
import pygame #contains functionalities to make the game
from time import sleep
#import os
#os.environ['SDL_VIDEO_CENTERED'] = '1'

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien 
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard


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

        #Create instance to store game stats
        self.stats = GameStats(self)

        #Create instance to create scoreboard
        self.sb = ScoreBoard(self)

        #make Ship()instace with AlienInvasion as argument
        self.ship = Ship(self)      #create ship instance
        self.bullets = pygame.sprite.Group()        #add bullet sprites group
        

        self.aliens = pygame.sprite.Group()
        self._create_squadron()
        self.play_button = Button(self, "Play")


    def run_game(self):
        '''start main loop for game'''
        while True:
            #watch for any keyboard or mouse inputs
            self._check_events()

            if self.stats.game_active == True:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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

                #MOUSEBUTTON DOWN EVENT
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
    

    def _check_play_button(self, mouse_pos):
        """Start new game when player clicks play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and self.stats.game_active != True:
            #Reset game settings
            self.settings.initialize_dynamic_settings()
            #Hide Cursor
            pygame.mouse.set_visible(False)

            #Reset game stats
            self.stats.reset_stats()
            self.stats.game_active = True

            #remove remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Create new squadron and center ship
            self._create_squadron()
            self.ship.center_ship()


                
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
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2*alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        #determine number of rows that fit on screen
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (10 * alien_height) -ship_height
        number_rows = available_space_y // (2*alien_height)
        
        #Create full squadron of aliens
        for row_number in range (number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)


    def _create_alien(self, alien_number, row_number):
        """Create Alien and place it in row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)


    def _check_squadron_edges(self):
        """Respond appropriately if alien hits screen edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_squadron_direction()
                break


    def _change_squadron_direction(self):
        """Drop entire squadron and change its direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.squadron_drop_speed
        self.settings.squadron_direction *= -1

    def _update_bullets(self):
        '''
        Update bullet position and remove old ones
        '''
        self.bullets.update()
        #remove bullets when they reach top of screen
        for bullet in self.bullets.copy():      #iterate over a copy to safely remove bullets without affecting original list
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)
        self._check_bullet_alien_collions()


    def _check_bullet_alien_collions(self):
        """respond to bullet/alien collisions"""
        #Check for bullets that hit aliens
        #if so get rid of bullet and alien
        collisions = pygame.sprite.groupcollide(
        self.bullets, self.aliens, True, True
        )
        if collisions :
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()

        if not self.aliens:
            #Destroy existing bullets and make new squadron
            self.bullets.empty()
            self._create_squadron()
            self.settings.increase_speed()


    def _update_aliens(self):
        """Check if squadron is at an edge, then update all aliens position"""
        self._check_squadron_edges()
        self.aliens.update()

        #look for alien/ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("collision alien/ship happened!")
            self._ship_hit()
        
        #look for aliens hitting screen bottom
        self._check_aliens_bottom()


    def _ship_hit(self):
        """respond to ship/alien collision"""
        if self.stats.ships_left > 0:
            #decrement ship_left
            self.stats.ships_left -= 1

            #get rid of remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #create new squadron and center the ship
            self._create_squadron()
            self.ship.center_ship()

            #pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

        


    def _check_aliens_bottom(self):
        """Check if any alien reached screen bottom"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #same as if ship got hit
                self._ship_hit()
                break
        

    def _update_screen(self):
            #redraw the screen during each loop iteration
            self.screen.fill(self.bg_color)
            self.ship.blitme()
            self.sb.show_score()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            

            #draw play button if the game is inactive
            if self.stats.game_active == False:
                self.play_button.draw_button()
            #make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':      #only run when script is ran directly (ex: not when imported)
    #make game instance, run game
    ai = AlienInvasion()
    ai.run_game()


