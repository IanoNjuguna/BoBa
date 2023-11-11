'''
InfiniPong
'''

import turtle

"""
CREATE WINDOW
"""
window = turtle.Screen()
window.title("PONG by @IanoNjuguna")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

'''
SCORE AT THE BEGINNING
'''
score_a = 0
score_b = 0

'''
PADDLE A SPECS
'''
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

'''
PADDLE B SPECS
'''
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

'''
BALL SPECS
'''
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.pendown()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

'''
PEN (SCORE UPDATES)
'''
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 \t Player B: 0", align = "center", font = ("Courier", 24, "normal"))

'''
FUNCTIONS
'''
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)

'''
KEYBOARD BINDING
'''
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

'''
Main Game Loop
'''
while True:
    window.update()

    '''
    MOVE THE BALL
    '''
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    '''
    BORDER CHECK
    '''
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} \t Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} \t Player B: {}".format(score_a, score_b), align = "center", font = ("Courier", 24, "normal"))


    '''
    PADDLE & BALL COLLISIONS
    '''
    if (ball.xcor() > 345 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -345 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
