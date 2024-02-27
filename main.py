from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#Setting up Screen and background color
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        print("nom nom nom")



    #Detect collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                game_is_on=False
                scoreboard.game_over()
"""    
    for seg in segments:
        seg.forward(20)
    """
"""
segment_1 = Turtle(shape="square")
segment_1.color("White")

segment_2 = Turtle(shape="square")
segment_2.color("White")
segment_2.goto(-20,0)

segment_3 = Turtle(shape="square")
segment_3.color("White")
segment_3.goto(-30,0)

"""
screen.exitonclick()