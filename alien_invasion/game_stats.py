class GameStats():
    """Track game stats"""
    
    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Make the game inactive at first
        self.game_activate = False
        # Under no circumstances should the highest score be reset
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize stats that may change during the game run"""
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        