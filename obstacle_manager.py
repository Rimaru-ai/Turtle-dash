from turtle import Turtle
import random

OBSTACLE_TYPES = ["circle", "triangle", "square"]
OBSTACLE_COLORS = ["brown", "darkgreen", "gray"]
MAX_OBSTACLES = 7

class ObstacleManager:

    def __init__(self):
        self.all_obstacles = []

    def create_obstacle(self):
        random_chance = random.randint(1, 15)  # not too frequent
        if random_chance == 1:
            obstacle = Turtle(random.choice(OBSTACLE_TYPES))
            obstacle.penup()
            obstacle.color(random.choice(OBSTACLE_COLORS))
            obstacle.shapesize(stretch_len=1.2, stretch_wid=1.2)

            x_position = random.randint(-250, 250)
            y_position = random.randint(-200, 200)
            obstacle.goto(x_position, y_position)

            self.all_obstacles.append(obstacle)

            # 🔥 If too many, remove the oldest one
            if len(self.all_obstacles) > MAX_OBSTACLES:
                old = self.all_obstacles.pop(0)
                old.hideturtle()
