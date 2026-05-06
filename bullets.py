import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, game_settings, screen, ship):
        super().__init__()
        self.game_settings = game_settings
        self.screen = screen

        self.rect = pygame.Rect(
            0, 0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.moving_factor = game_settings.bullet_speed_factor
        self.color = game_settings.bullet_bg_color

    def draw_bullets(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        self.y -= self.moving_factor
        self.rect.y = self.y
