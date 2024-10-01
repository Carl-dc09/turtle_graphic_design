# Import turtle module
from turtle import *
# Import colors
import colorsys

# Set the background color
bgcolor("black")

# Set the drawing speed
tracer(500)

# Set a function to draw
def draw():
    # Set a value for the color transitions
    hue = 0
    # Set the loop
    for iteration in range(100):
        # Convert into RGB color
        colors_ = colorsys.hsv_to_rgb(hue, 1, 1)
    