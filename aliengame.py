import pygame
from Settings import settingsofGame
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import Game_stats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    game_settings = settingsofGame()
    ship = Ship(screen, game_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(game_settings, screen, ship, aliens)
    stats = Game_stats(game_settings)
    play_button = Button(game_settings, screen, "Play")
    sb = Scoreboard(game_settings, screen, stats)

    while True:

        gf.check_events(game_settings, screen, bullets,
                        ship, sb, stats, aliens, play_button)
        if stats.game_active:
            ship.update_ship()
            gf.update_bullets(bullets, aliens)
            gf.update_aliens(game_settings, stats, screen,
                             ship, sb, aliens, bullets)
            gf.check_bullet_alien_collisons(
                game_settings, screen, ship, stats, sb, aliens, bullets)
        gf.update_screen(game_settings, screen, bullets,
                         ship, aliens, stats, sb, play_button)


run_game()
