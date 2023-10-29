from turtle import Turtle

class Paddle(Turtle):
  """
  A class representing a paddle in the Pong game.

  Attributes:
      position (tuple): The initial position of the paddle.

  Methods:
      __init__(self, position): Initializes a new paddle object.
      go_up(self): Moves the paddle upward.
      go_down(self): Moves the paddle downward.
      setup_controls(self, screen): Sets up keyboard controls for the paddle.
  """

  def __init__(self, position):
      """
      Initializes a new Paddle object.

      Args:
          position (tuple): The initial position of the paddle.
      """
      super().__init__()
      self.shape("square")
      self.color("white")
      self.shapesize(stretch_wid=5, stretch_len=1)
      self.penup()
      self.goto(position)

  def go_up(self):
      """
      Move the paddle upward.

      The paddle moves up by changing its y-coordinate position.
      """
      new_y = self.ycor() + 20
      self.sety(new_y)

  def go_down(self):
      """
      Move the paddle downward.

      The paddle moves down by changing its y-coordinate position.
      """
      new_y = self.ycor() - 20
      self.sety(new_y)

  def setup_controls(self, screen):
      """
      Set up keyboard controls for the paddle.

      This method allows the paddle to respond to the 'Up' and 'Down' arrow keys.

      Args:
          screen (Turtle.Screen): The game screen where keyboard input is listened to.
      """
      screen.listen()
      screen.onkey(self.go_up, "Up")
      screen.onkey(self.go_down, "Down")
