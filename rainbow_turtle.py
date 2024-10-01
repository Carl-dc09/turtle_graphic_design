# Import from turtle
from turtle import *
# Import color from colorsys
import colorsys

# Set the drawing speed
speed(0)
tracer(5)
hideturtle()
# Set the background color
bgcolor("black")
# Set the hue to determine the color
hue_color = 0

def draw_pattern(hue_color):
    for outer_loop in range(16):
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

for row in range(2):
     for columns in range(3):
          penup()
          goto(-500 + columns * 500, 300 - row * 500)
          pendown()

          draw_pattern(hue_color)
          hue_color += 0.1 
done()

