class Settings():
    """Class that stores all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize game settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # ship settings 
        self.ship_limit = 3
        
        # bullet settings
        self.bullet_width = 30
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # alien settings
        self.fleet_drop_speed = 10

        # Increase speed of alien points
        self.score_scale = 1.5
        
        # At what speed to speed up the pace of the game
        self.speedup_scale = 1.2
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change as the game progresses"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.2
        
        # fleet direction is 1 means move to the right, -1 means move to the left
        self.fleet_direction = 1
        
        # keep score
        self.alien_points = 50
        
    def increase_speed(self):
        """increase speed setting"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
