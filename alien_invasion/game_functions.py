import sys
import pygame
from time import sleep
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Responding to keystrokes and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)
            
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks the Play button"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_activate:
        # reset game settings
        ai_settings.initialize_dynamic_settings()
        
        # hide cursor
        pygame.mouse.set_visible(False)
        
        # reset game stats
        stats.reset_stats()
        stats.game_activate = True
        
        # Reset scoreboard image
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        
        # Empty alien list and bullet list
        aliens.empty()
        bullets.empty()
        
        # Create a new group of aliens and center the spaceship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Response to keydown"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def check_keyup_events(event, ship):
    """Response to keyup"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    
def fire_bullet(ai_settings, screen, ship, bullets):
    """If the limit has not been reached, fire a bullet"""
    # Create a bullet and add it to the group bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
                
def get_number_aliens_x(ai_settings, alien_width):
    """Calculate how many aliens can fit in each row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Calculate how many rows of aliens can fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it on the current line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Create Alien Crowds"""
    # Create an alien, and count how many aliens can fit in a row
    # Alien Pitch to Alien Width
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    
    # Create Alien Crowds
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
            
def change_fleet_direction(ai_settings, aliens):
    """Moves a whole group of aliens down and changes their direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1      
    
def check_fleet_edges(ai_settings, aliens):
    """Take approprite action when aliens reach the edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
 
def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Check if a bullet hit the alien
    # If so, delete the corresponding bullets and aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    
    if len(aliens) == 0:
        # Delete existing bullets ,speed up the game ,move up a level and create a new group of aliens
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)
        
        
def check_alien_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat it like a spaceship has been hit
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break
        
def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """Respond to a spaceship hit by aliens"""
    if stats.ship_left > 0:
        # Decrement ships_left by 1
        stats.ship_left -= 1
        
        # update scoreboard
        sb.prep_ships()
    
        # Empty alien list and bullet list
        aliens.empty()
        bullets.empty()
    
        # Create a new group of aliens and place the spaceship at the bottom center of the screen
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    
        # pause
        sleep(0.5)
    
    else:
        stats.game_activate = False
        pygame.mouse.set_visible(True)
        
def check_high_score(stats, sb):
    """Check if a new highest score is born"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
                      
def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """
    Checks to see if any aliens are on the edge of the screen and updates the position of the entire swarm
    """ 
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # Detecting collisions between aliens and spaceships
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
        
    # Check if any aliens reach the bottom of the screen
    check_alien_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)
    
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Update the position of the bullet and delete the bullet that has disappeared"""
    # Update the position of the bullet
    bullets.update()
    
    # delete the bullet that has disappered
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
  
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """update the image on the screen and switch to the new screen"""
    # Redraw the screen each time through the loop
    screen.fill(ai_settings.bg_color)
    # Repainted all bullets behind spaceships and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    # show score
    sb.show_score()
    
    # Draw the Play button if the game is in1
    if not stats.game_activate:
        play_button.draw_button()
    # make the most recently drawn screen visible
    pygame.display.flip()
