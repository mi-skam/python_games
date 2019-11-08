
import os
import turtle

wn = turtle.Screen()
wn.title("Pong by plumps")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # stops window from updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # create rectangular paddle shape
paddle_a.penup() # don't draw a line under moving
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # create rectangular paddle shape
paddle_b.penup() # don't draw a line under moving
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation
ball.shape("square")
ball.color("white")
ball.penup() # don't draw a line under moving
ball.goto(0, 0)

## movement for every frame
ball.dx = 2
ball.dy = 2

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0 PlayerB: 0", align="center", font=("Courier", 24, "normal"))
# Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "v")
wn.onkeypress(paddle_a_down, "i")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # move the ball 
    # TODO: fix speed 
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking 
    # TODO: use relative coordinates
    ## top
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    ## bottom
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    ## right 
    if ball.xcor() > 390:
        ball.goto(0, 0) # recenter the ball
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"PlayerA: {score_a} PlayerB: {score_b}", align="center", font=("Courier", 24, "normal"))


    ## left
    if ball.xcor() < -390:
        ball.goto(0, 0) # recenter the ball
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"PlayerA: {score_a} PlayerB: {score_b}", align="center", font=("Courier", 24, "normal"))


    # paddle and ball collisions
    ## right
    if (ball.xcor() > 340 and ball.xcor() < 350) and \
       (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
       ball.setx(340)
       ball.dx *= -1
       os.system("aplay bounce.wav&")
    ## left
    if (ball.xcor() < -340 and ball.xcor() > -350) and \
       (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
       ball.setx(-340)
       ball.dx *= -1
       os.system("aplay bounce.wav&")