# Import the turtle module
from turtle import *
# Import the math module
import math

# Calculate and return the y-coordinate of the heart shape
def heart_a(single_parameter):
    return 15*math.sin(single_parameter)**3
# Calculate and return the x-coordinate of the heart shape
def heart_b(single_parameter):
    return 12*math.cos(single_parameter)-5*\
           math.cos(2*single_parameter)-2*\
           math.cos(3*single_parameter)-\
           math.cos(4*single_parameter)

# Set the drawing speed
speed(0)

# Hide the cursor
hideturtle()

# Set the background color
bgcolor("black")

# Calculate the loop
for t_angle in range(6000):
    goto(heart_a(t_angle)*20, heart_b(t_angle)*20)
    for color_iteration in range(5):
        color("#f73487")
    goto(0, 0)

