import pygame.font

class ScoreBoard:
    """class to report score info"""

    def __init__(self, ai_game):
        """Initialize score keeping attributes"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        #Font settings for score
        self.score_text_color = (250, 230, 10)
        self.high_score_text_color = (70, 250, 240)

        self.font = pygame.font.SysFont(None, 48)

        #Prepare initial score image
        self.prep_score()

        self.prep_high_score()

    def prep_score(self):
        """turn score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.score_text_color, self.settings.bg_color)

        #Display score at top-right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """turn high score into a rendered image"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.high_score_text_color, self.settings.bg_color)

        #Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top

    def check_high_score(self):
        """check to see if there is new high score"""
        if self.stats.score > self.stats.high_score :
            self.stats.high_score = self.stats.score
            self.prep_high_score()


    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
