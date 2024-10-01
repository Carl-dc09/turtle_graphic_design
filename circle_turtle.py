# Import turtle module
import turtle
from turtle import *
# Import colors
import colorsys

# Create new turtle
turtle_ = turtle.Turtle()
# Set a background color
screen_color = turtle.Screen().bgcolor("black")
# Set the drawing speed
turtle_.speed(500)

# Set a value for hue
hue_increment = 70
hue_value = 0

# Create a loop
for iteration_loop in range (720):
    # Set the color
    saturated_color = colorsys.hsv_to_rgb(hue_value, 1, 0.8)
    hue_value += 1/hue_increment
    turtle_.color(saturated_color)
    # Set the position
    turtle_.left(1)
    turtle_.fd(1)
