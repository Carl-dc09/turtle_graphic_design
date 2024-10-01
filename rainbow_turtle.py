from turtle import *
import colorsys

speed(0)
bgcolor("black")
hue_color = 0
for outer_loop in range(16):
    for inner_loop in range(18):
        c = colorsys.hsv_to_rgb(hue_color, 1, 1)
        color(c)
        hue_color += 0.005
        rt(90)
        circle(150 - inner_loop * 6, 90)
        lt(90)
        circle(150 - inner_loop * 6, 90)
        rt(180)
    circle(40, 24)
done()
