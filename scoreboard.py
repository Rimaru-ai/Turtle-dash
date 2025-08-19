from turtle import Turtle

FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.lives = 3
        self.highscore = self.load_highscore()   # NEW
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}  Lives: {self.lives}  High Score: {self.highscore}",
                   align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        # Update high score before showing Game Over
        if self.level > self.highscore:
            self.highscore = self.level
            self.save_highscore()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    # NEW methods
    def load_highscore(self):
        try:
            with open("highscore.txt", "r") as f:
                return int(f.read())
        except:
            return 0

    def save_highscore(self):
        with open("highscore.txt", "w") as f:
            f.write(str(self.highscore))
