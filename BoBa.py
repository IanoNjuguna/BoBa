'''
BoBa: The Bouncing Ball

By @IanoNjuguna
'''

import turtle

"""
WINDOW
"""
window = turtle.Screen()
window.title("BoBa: The Bouncing Ball")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

'''
BoBa SPECS
'''
BoBa = turtle.Turtle()
BoBa.speed(0)
BoBa.shape("circle")
BoBa.color("skyblue")
BoBa.pendown()
BoBa.goto(0, 0)
BoBa.dx = 1
BoBa.dy = 3

'''
MAIN LOOP
'''
while True:
    window.update()

    '''
    MOVE BoBa
    '''
    BoBa.setx(BoBa.xcor() + BoBa.dx)
    BoBa.sety(BoBa.ycor() + BoBa.dy)

    '''
    BORDER COLLISIONS
    '''
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

