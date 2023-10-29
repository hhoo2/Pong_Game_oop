from turtle import Turtle

class line(Turtle):
  """
  A class representing a vertical dotted line in for Pong game.

  Attributes:
      x (int): The x-coordinate of the starting point.
      y (int): The y-coordinate of the starting point.
      length (int): The length of the line.
      color (str): The color of the line (default is "white").
      thickness (int): The thickness of the line (default is 3).

  Methods:
      __init__(self, x, y, length, color="white", thickness=3): Initializes a new Line object.
      draw_dotted_line(self, length): Draws the vertical line.
  """

  def __init__(self, x, y, length, color="white", thickness=3, gap_lengthlength = 20):
      """
      Initializes a new Line object.

      Args:
          x (int): The x-coordinate of the starting point.
          y (int): The y-coordinate of the starting point.
          length (int): The length of the line.
          color (str, optional): The color of the line (default is "white").
          thickness (int, optional): The thickness of the line (default is 3).
      """
      super().__init__()
      self.penup()
      self.goto(x, y)
      self.setheading(90)  # Set the heading to 90 degrees (upward)
      self.pendown()
      self.color(color)
      self.pensize(thickness)
      self.draw_dotted_line(length,gap_lengthlength)
      self.hideturtle()


  def draw_dotted_line(self, length, gap_length):
    total_distance = 0
    while total_distance < length:
        self.forward(gap_length)
        total_distance += gap_length
        self.penup()
        self.forward(gap_length)
        total_distance += gap_length
        self.pendown()