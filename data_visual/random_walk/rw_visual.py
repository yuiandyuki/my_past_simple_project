import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Simulate a random walk continuously as long as the program is active
while True:
    # Create a RandomWalk instance and draw all the points it contains
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Set the size of the drawing window
    plt.figure(dpi=80, figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    # # highlight start and end
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    # # Hide axes (bug)
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
