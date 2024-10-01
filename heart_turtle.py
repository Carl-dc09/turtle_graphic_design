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

# Set the background color
bgcolor("black")
