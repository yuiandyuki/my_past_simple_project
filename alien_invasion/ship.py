import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_settings, screen):
        """Initialize the spaceship and set its initial position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the spaceship image and get its bounding rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Place each new ship in the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # Store decimal values in the spaceship's attribute "center"
        self.center = float(self.rect.centerx)
        
        # move signal
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Adjust the spaceship's position according to the movement sign"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update the rect object based on self.center
        self.rect.centerx = self.center
        
    def center_ship(self):
        """Center the spaceship on the screen"""
        self.center = self.screen_rect.centerx
        
    def blitme(self):
        """Draw the spaceship at the specified position"""
        self.screen.blit(self.image, self.rect)