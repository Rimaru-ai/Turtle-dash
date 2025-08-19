import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from obstacle_manager import ObstacleManager


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
obstacle_manager = ObstacleManager()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    obstacle_manager.create_obstacle()

    # Detect collision with obstacles
    for obs in obstacle_manager.all_obstacles:
        if player.distance(obs) < 25:  # collision range
            if scoreboard.lives > 1:
                scoreboard.lose_life()
                player.goto_start()
            else:
                scoreboard.lose_life()
                game_is_on = False
                scoreboard.game_over()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            if scoreboard.lives > 1:  # still has lives left
                scoreboard.lose_life()
                player.goto_start()  # reset player to bottom
            else:
                scoreboard.lose_life()
                game_is_on = False
                scoreboard.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()
        obstacle_manager.all_obstacles.clear()
        
screen.exitonclick()
