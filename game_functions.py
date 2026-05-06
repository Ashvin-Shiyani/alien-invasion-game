import pygame
import sys
from bullets import Bullet
from alien import Alien
from time import sleep


def keydown_events(game_settings, screen, ship, bullets, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < game_settings.bullets_allowed:
            new_bullet = Bullet(game_settings, screen, ship)
            bullets.add(new_bullet)


def keyup_events(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(game_settings, screen, stats, play_button, ship, sb, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        if stats.score > stats.highscore:
            stats.highscore = stats.score
            sb.prep_highscore()
        stats.reset_stats()
        sb.prep_score()
        sb.prep_level()
        sb.prep_lives()
        pygame.mouse.set_visible(False)
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()


def check_events(game_settings, screen, bullets, ship, sb, stats, aliens, play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_settings.initialize_dynamic_settings()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(game_settings, screen, stats,
                              play_button, ship, sb, aliens, bullets, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            keydown_events(game_settings, screen, ship, bullets, event)

        elif event.type == pygame.KEYUP:
            keyup_events(ship, event)


def update_screen(game_Settings, screen, bullets, ship, aliens, stats, sb, play_button):
    screen.fill(game_Settings.bg_color)

    for bullet in bullets:
        bullet.draw_bullets()

    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    sb.show_highscore()
    sb.show_level()
    sb.show_lives()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()


def update_bullets(bullets, aliens):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def get_column_number(game_settings, alien_width):
    available_space = game_settings.screen_width-(3*alien_width)
    return int(available_space/(2*alien_width))


def get_row_number(game_settings, ship_height, alien_height):
    available_space_y = game_settings.screen_height - \
        ship_height-(4*alien_height)
    return int(available_space_y/(2*alien_height))


def create_aliens(game_settings, screen, aliens, row_number, column_number):
    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width+(2 * alien_width * column_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height+(2*alien.rect.height*row_number)
    aliens.add(alien)


def create_fleet(game_settings, screen, ship, aliens):
    new_alien = Alien(game_settings, screen)
    colums = get_column_number(game_settings, new_alien.rect.width)
    rows = get_row_number(game_settings, ship.rect.height,
                          new_alien.rect.height)

    for row_number in range(rows):
        for column_number in range(colums):
            create_aliens(game_settings, screen, aliens,
                          row_number, column_number)


def change_fleet_direction(game_settings, aliens):
    for alien in aliens:
        alien.rect.y += game_settings.fleet_drop_speed


def check_fleet_edges(game_settings, aliens):
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(game_settings, aliens)
            game_settings.fleet_direction *= -1
            break


def ship_hit(game_settings, stats, screen, ship,  aliens, bullets, sb):

    if stats.ship_left > 0:
        stats.ship_left -= 1
        sb.prep_lives()
        aliens.empty()
        bullets.empty()

        create_fleet(game_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(1.0)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottoms(game_settings, stats, screen, ship,  aliens, bullets, sb):
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(game_settings, stats, screen, ship, aliens, bullets, sb)
            break


def update_aliens(game_settings, stats, screen, ship, sb, aliens, bullets):
    check_fleet_edges(game_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(game_settings, stats, screen, ship, aliens, bullets, sb)
    check_aliens_bottoms(game_settings, stats, screen,
                         ship, aliens, bullets, sb)


def check_bullet_alien_collisons(game_settings, screen, ship, stats, sb, aliens, bullets):
    collisions = pygame.sprite.groupcollide(
        bullets, aliens, True, True)

    if len(aliens) == 0:
        stats.level += 1
        sb.prep_level()
        bullets.empty()
        game_settings.increase_speed()
        create_fleet(game_settings, screen, ship, aliens)

    if collisions:
        for aliens_hit in collisions.values():
            stats.score += game_settings.alien_points*len(aliens_hit)
        sb.prep_score()
        if stats.highscore < stats.score:
            stats.highscore = stats.score
            sb.prep_highscore()
