import sys #tools to exit the game when the player quits
import pygame #contains functionalities to make the game

class AlienInvasion:
    '''class to manage overall assets and behaviors'''
    
    def __init__(self):
        '''initialize game and create ressources'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))

        #set background color
        self.bg_color = (5, 5, 30)

    def run_game(self):
        '''start main loop for game'''
        while True:
            #watch for any keyboard or mouse inputs
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #redraw the screen during each loop iteration
            self.screen.fill(self.bg_color)
            #make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    #make game instance, run game
    ai = AlienInvasion()
    ai.run_game()

