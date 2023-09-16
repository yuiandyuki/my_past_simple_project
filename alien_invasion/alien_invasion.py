import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # Initalize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Create the Play button
    play_button = Button(ai_settings, screen, "Play")
    
    # Create a spaceship, a bullet group and an alien group
    ship = Ship(ai_settings ,screen)
    bullets = Group()
    aliens = Group()
    
    # Create an instance for storing game stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Create an alien group
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Start the main loop of the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        
        if stats.game_activate:
            ship.update()
            bullets.update()
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        
run_game()

