import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")

screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

#create car manager
car_manager = CarManager()

#create scoreboard
scoreboard = Scoreboard()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    #dd collision detection
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            print("Game Over")
            break
        
    if player.finish_line():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()
        
def restart():
    global game_is_on
    game_is_on = True
    player.reset_position()
        

screen.exitonclick()