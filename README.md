# BoBa: The Bouncing Ball

> Inspired by the lore of Zima Blue

## Description

BoBa is a ball bouncing around within a window. I built this to demonstrate the principles of animation and collision detection using the Python's Turtle module.

### Documentation

Below is a concise explanation of BoBa's code

#### Import the Turtle Module

First, we import the [Turtle module](https://docs.python.org/3/library/turtle.html):

``` Python
import turtle
```

#### Set Up the Window

Then, we configure the window where the animation will be displayed. The settings include: the title, background color, size, and turning off automatic updates.

``` Python
window = turtle.Screen()
window.title("BoBa: The Bouncing Ball")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)
```

#### Create BoBa, the Bouncing Ball

Any entity that exists, even in the real world, does so by virtue of its properties and BoBa is no exception. To create BoBa, we need to set its properties.

The properties we set for BoBa include: speed, shape, color, initial position, and velocity (dx and dy)

``` Python
BoBa = turtle.Turtle()
BoBa.speed(0)
BoBa.shape("circle")
BoBa.color("skyblue")
BoBa.pendown()
BoBa.goto(0, 0)
BoBa.dx = 1
BoBa.dy = 3
```

#### Main Loop

The main loop is a while loop that runs indefinitely:

``` Python
while True:
  statement(s)
```

This loop updates the window's display and controls the movement of BoBa.

To update the window's display after each iteration of the main loop, we call the ```window.update()``` method under the main loop.

##### Move BoBa

BoBa's position is updated in each iteration of the main loop. To do this, we need to add its velocity (dx and dy) to its current coordinates using the setx() and sety() methods.

``` Python
BoBa.setx(BoBa.xcor() + BoBa.dx)
BoBa.sety(BoBa.ycor() + BoBa.dy)
```

##### Border Collisions

We use control flow statements to check for collisions with the borders of the window. If the ball hits the top or bottom border, its vertical velocity (dy) is reversed. If it hits the left or right border, its horizontal velocity (dx) is reversed.

``` Python
if BoBa.ycor() > 290:
  BoBa.sety(290)
  BoBa.dy *= -1

if BoBa.ycor() < -290:
  BoBa.sety(-290)
  BoBa.dy *= -1

if BoBa.xcor() > 390:
  BoBa.setx(390)
  BoBa.dx *= -1

if BoBa.xcor() < -390:
  BoBa.setx(-390)
  BoBa.dx *= -1
```

#####
