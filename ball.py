from turtle import Turtle

class Ball(Turtle):
  """
  A class representing a ball in the Pong game.

  Attributes:
      x_move (int): The horizontal movement speed of the ball.
      y_move (int): The vertical movement speed of the ball.
      move_speed (float): The speed at which the ball moves.

  Methods:
      __init__(self): Initializes a new ball object.
      move(self): Moves the ball based on its current speed.
      bounce_y(self): Inverts the vertical movement direction of the ball.
      bounce_x(self): Inverts the horizontal movement direction of the ball.
      reset_position(self): Resets the ball's position and speed.
  """

  def __init__(self):
      """
      Initializes a new Ball object.

      The ball is initially set as a white circle with a starting
      horizontal and vertical movement speed and a move speed.
      """
      super().__init__()
      self.shape("circle")
      self.color("white")
      self.penup()
      self.x_move = 10
      self.y_move = 10
      self.move_speed = 0.1

  def move(self):
      """
      Move the ball based on its current speed.

      The ball's position is updated by adding its horizontal and vertical
      movement speed to its current position.
      """
      new_x = self.xcor() + self.x_move
      new_y = self.ycor() + self.y_move
      self.goto(new_x, new_y)

  def bounce_y(self):
      """
      Invert the vertical movement direction of the ball.

      This method is called when the ball hits the top or bottom wall.
      """
      self.y_move *= -1
      self.move_speed *= 0.8

  def bounce_x(self):
      """
      Invert the horizontal movement direction of the ball.

      This method is called when the ball hits a paddle.
      """
      self.x_move *= -1

  def reset_position(self):
      """
      Reset the ball's position and speed.

      The ball is placed back to the center of the screen, and its
      movement speed is reset to its initial value.
      """
      self.goto(0, 0)
      self.move_speed = 0.1
      self.bounce_x()
