import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class that manages the bullets fired by the spaceship"""
    
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object where the spaceship is"""
        super().__init__()
        self.screen = screen
        
        # Create a rectangle representing the bullet at (0, 0), and then set the correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # store the bullet position expressed as a decimal
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """move the bullet up"""
        # Update the decimal value representing the position of the bullet
        self.y -= self.speed_factor
        # Update the position of the rect representing the bullet
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        