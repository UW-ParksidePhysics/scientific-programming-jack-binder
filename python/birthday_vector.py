from vpython import *

# GlowScript 3.0 VPython

# Written by Ruth Chabay, licensed under Creative Commons 4.0.
# All uses permitted, but you must not claim that you wrote it, and
# you must include this license information in any copies you make.
# For details see http://creativecommons.org/licenses/by/4.0

scene.background = color.white
scene.width = 600
scene.height = 600
scene.forward = vector(-.5, -.3, -1)

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

cylinder(color=vector(1, 0, 0), pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.3)
label(pos=vector(11, 0, 0), text="x", color=color.red, opacity=0, height=30, box=0)
cylinder(color=color.green, pos=vector(0, 0, 0), axis=vector(0, 10, 0), radius=0.3)
label(pos=vector(0, 11, 0), text="y", color=color.green, opacity=0, height=30, box=0)
label(pos=vector(0, 0, 11), text="z", color=color.blue, opacity=0, height=30, box=0)

arrow(pos=vector(0, 0, 0), axis=vector(5, 3, 25), color=color.yellow, shaftwidth=0.5)
label(pos=vector(5, 3, 25), text="r=5x+3y+25z", color=color.orange, height=30, box=0)
