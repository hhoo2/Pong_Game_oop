from turtle import Turtle

class Scoreboard(Turtle):
    """
    A class representing the scoreboard in the Pong game.

    Attributes:
        l_score (int): The score of the left player.
        r_score (int): The score of the right player.

    Methods:
        __init__(self): Initializes a new Scoreboard object.
        update_scoreboard(self): Clears and updates the scoreboard display.
        l_point(self): Increments the score of the left player and updates the scoreboard.
        r_point(self): Increments the score of the right player and updates the scoreboard.
    """

    def __init__(self):
        """
        Initializes a new Scoreboard object.

        The scoreboard is initially set up with white text and hidden.
        The scores for both the left and right players start at 0.
        """
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clears and updates the scoreboard display.

        The method clears the current scoreboard and writes the scores
        of both players at their respective positions.
        """
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 90, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 90, "normal"))

    def l_point(self):
        """
        Increments the score of the left player and updates the scoreboard.

        This method is called when the left player scores a point.
        """
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """
        Increments the score of the right player and updates the scoreboard.

        This method is called when the right player scores a point.
        """
        self.r_score += 1
        self.update_scoreboard()
