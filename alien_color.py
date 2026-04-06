import random

alien_colors = ['red', 'green', 'yellow']
alien_color = random.choice(alien_colors)

if alien_color == 'green':
    points = 5
if alien_color == 'yellow':
    points = 10
if alien_color == 'red':
    points = 15