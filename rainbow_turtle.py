# Import from turtle
from turtle import *
# Import color from colorsys
import colorsys

# Set the drawing speed
speed(0)
# Set the background color
bgcolor("black")
# Set the hue to determine the color
hue_color = 0

for outer_loop in range(200):
    for inner_loop in range(18):
        c = colorsys.hsv_to_rgb(hue_color, 1, 1)
        color(c)
        hue_color += 0.005
        right(90)
        circle(150 - inner_loop * 6, 90)
        left(90)
        circle(150 - inner_loop * 6, 90)
        right(180)
    circle(40, 24)
done()

