from random import choice

class RandomWalk():
    """A class for generating random walk data"""
    
    def __init__(self, num_points=500):
        """Initialize the properties of the random walk"""
        self.num_points = num_points
        
        # All random walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """Compute all points included in the random walk"""
        
        # Walk continuously until the list reaches the specified length
        while len(self.x_values) < self.num_points:
            # Determine the direction to go and the distance to go in that direction
            x_step = self.get_step()
            y_step = self.get_step()
            
            # refuse to stand still
            if x_step == 0 and y_step == 0:
                continue
            
            # Calculate the x and y values ​​of the next point
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            
            self.x_values.append(next_x)
            self.y_values.append(next_y)
            
    def get_step():
        """Determine the direction to go and the distance to go in that direction"""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step