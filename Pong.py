import turtle

win = turtle.Screen()
win.title("Pong")  # names the window
win.bgcolor("black")  # colour of the background
win.setup(width=800, height=550)
win.tracer(0)  # manually controls when the window updates

# Score
score_a = 0 #sets scores to 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # sets speed to the max
paddle_a.shape("square")  # shape
paddle_a.color("white")  # colour of the shape
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # strtches the shape
paddle_a.penup()
paddle_a.goto(-350, 0)  # placement of the shape

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#midline
midline = turtle.Turtle()
midline.speed(0)
midline.color("light grey")
midline.goto(0,0)
midline.shape ("square")
midline.shapesize(stretch_wid=30, stretch_len=0.35)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.6  # change in movement in the x direction
ball.dy = 0.6  # change in movement in the y direction



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 230)
pen.write("Player A: 0  Player B: 0", align="center", font=("Carrier", 24, "normal"))


# Function (does something that was defined for it)
def paddle_a_up():  # Function to move paddle up
    y = paddle_a.ycor()  # Gets the y-coordinate of paddle A
    y += 40 #adds 40 to the y-coordinate of paddle A everytime key is pressed
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 40
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 40
    paddle_b.sety(y)


# Keyboard binding
win.listen()  # tells window to listen to keyboard
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_a_up, "w")  # calls the function
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    win.update()
    if score_a == 5 or score_b == 5:    #End of game text appearance
        pen.goto(0, 0)
        pen.write("Game Over", align="center", font=("Carrier", 60, "normal"))
        ball.dy=0
        ball.dx=0
        ball.hideturtle()

    if score_a == 5:
        pen.goto(0, -50)
        pen.write("Player A Wins", align="center", font=("Carrier", 40, "normal"))
    if score_b == 5:
        pen.goto(0, -50)
        pen.write("Player B Wins", align="center", font=("Carrier", 40, "normal"))

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 275:  # Since screen is 600 pxels large, and ball is 20
        ballsety = (275)
        ball.dy *= -1  # reverses direction

    if ball.ycor() < -275:
        ballsety = (-275)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Carrier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Carrier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1.05

    if (ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1.05
