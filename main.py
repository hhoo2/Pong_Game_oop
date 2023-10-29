'''the main class code for the Pong game sets up the game screen, paddles, ball, and scoreboard. It creates a game loop to control the ball's movement, handle collisions, update scores, and enable paddle control based on the ball's position. The game continues until a player wins or the user closes the window by clicking.'''


# Import necessary modules
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
from line import line

# Create the game window
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Create paddles, ball, and scoreboard objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Create a line in the middle of the screen
line = line(0, -300, 600)

instruction_message = """
Welcome to Pong!

Instructions:
- Use '↑' and '↓' for right user
- Use 'w' and 's' key for left user
- Your goal is to bounce the ball past your opponent's paddle.
- The first player to reach 3 points wins the game.
Do you want to play the game? 
Click "OK" to start the game!

Enjoy the game!
"""

# Ask the player if they want to play the game
play_game = screen.textinput(title="Pong Game", prompt= instruction_message)

# Set up keyboard input
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

if play_game == "" or "yes" or "y":
  # Start the game loop
  game_is_on = True
  while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (
        (ball.distance(r_paddle) < 50 and ball.xcor() > 320)
        or (ball.distance(l_paddle) < 50 and ball.xcor() < -320)
    ):
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


# Close the game window when clicked
screen.exitonclick()
