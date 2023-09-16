from random import randint

class Die():
    """A class representing a dice"""
    
    def __init__(self, num_sides=6):
        """Dice default to 6 sides"""
        self.num_sides = num_sides
        
    def roll(self):
        """Returns a random value between 1 and the number of sides of the dice"""
        return randint(1, self.num_sides)