import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():

    def __init__(self, game_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_lives()

    def prep_lives(self):
        self.lives_group = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.screen, self.game_settings)
            ship.image = pygame.transform.scale(ship.image, (50, 50))
            ship.rect.x = 10 + ship_number * \
                (ship.rect.width + 10)
            ship.rect.y = 10
            self.lives_group.add(ship)

    def show_lives(self):
        self.lives_group.draw(self.screen)

    def prep_score(self):
        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.game_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right-20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)

    def prep_highscore(self):
        highscore_str = "{:,}".format(self.stats.highscore)
        self.highscore_image = self.font.render(
            highscore_str, True, self.text_color, self.game_settings.bg_color)

        self.highscore_rect = self.highscore_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = 20

    def show_highscore(self):
        self.screen.blit(self.highscore_image, self.highscore_rect)

    def prep_level(self):
        level = str(self.stats.level)
        self.level_image = self.font.render(
            level, True, self.text_color, self.game_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right-20
        self.level_rect.top = 70

    def show_level(self):
        self.screen.blit(self.level_image, self.level_rect)
