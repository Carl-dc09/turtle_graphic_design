# Import from turtle
from turtle import *
# Import color from colorsys
import colorsys
import time

# Set the drawing speed
speed(0)
tracer(5)
# Hide the cursor
hideturtle()
# Set the background color
bgcolor("black")
# Set the hue for color
hue_color = 0

# Countdown to mark the start of drawing
def start_countdown(seconds):
     penup()
     goto(0, 0)
     color("white")

     for i in range(seconds, 0, -1):
          clear()
          bgcolor(colorsys.hsv_to_rgb(i / seconds, 1, 1))
          write(f"Starting in {i}...", align="center", font=("Arial", 26))
          update()
          time.sleep(1)

     clear()
     write("Go!", align="center", font=("Arial", 24))
     update()
     time.sleep(1)
     clear()
     update()

# To draw a specific pattern
def draw_pattern(hue_color):
    # To draw the outer loop
    for outer_loop in range(16):
         # To draw the inner loop
         for inner_loop in range(18):
               # Convert the hue_color from the HSV color space to RGB format
               turtles_color = colorsys.hsv_to_rgb(hue_color, 1, 1)

               # Set the turtle's color
               color(turtles_color)
               # Set the drawing function
               hue_color += 0.005
               right(90)
               circle(150 - inner_loop * 6, 90)
               left(90)
               circle(150 - inner_loop * 6, 90)
               right(180)
         circle(40, 24)

def start_drawing():
     global hue_color
     bgcolor("black")

     # Set a multiple turtle's in a rows and columns
     for rows in range(2):
          for columns in range(3):
               penup()
               goto(-500 + columns * 500, 300 - rows * 500)
               pendown()
               draw_pattern(hue_color)
               hue_color += 0.1

     penup()
     goto(0, 0)
     clear()

     penup()
     goto(0, 200)
     color("white")
     write("I Love You!", align="center", font=("Arial", 72, "bold"))
     update()
     time.sleep(2)
     
     clear()
     update()

     heart_effect()

def heart_effect():
     penup()
     goto(0, -100)
     pendown()
     color("pink")
     begin_fill()

     left(50)
     forward(133)
     circle(50, 200)
     right(140)
     circle(50, 200)
     forward(133)

     end_fill()

     penup()
     goto(0, 0)
     update()

def start_again():
     global hue_color
     while True:
          start_countdown(5)
          start_drawing()

          ask_restart = textinput("Restart?", "Would you like to play my confession again? (Yes/No): ")
          if ask_restart is None or ask_restart.lower() != "yes":
               clear()
               penup()
               goto(0, 0)
               color("white")
               write("I hope I made you smile :).", align="center", font=("Arial", 26))
               update()
               time.sleep(2)

               for i in range(5, 0, -1):
                    clear()

                    bgcolor(colorsys.hsv_to_rgb(i / 5, 1, 1))
                    write(f"Closing in {i}...", align="center", font=("Arial", 26))
                    update()
                    time.sleep(1)
               clear()
               break

     exit()

start_again() 

