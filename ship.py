import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, screen, game_settings):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load('finalship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    def update_ship(self):

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_moving_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_moving_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx
