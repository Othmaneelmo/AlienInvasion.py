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
        self.text_color = (250, 230, 10)
        self.font = pygame.font.SysFont(None, 48)

        #Prepare initial score image
        self.prep_score()

    def prep_score(self):
        """turn score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Display score at top-right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Draw score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
