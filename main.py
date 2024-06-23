from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)

snake=Snake()
food=Food()
Score=Scoreboard()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


game_is_on=True
while game_is_on:
    Score.Update_scoreboard()
    screen.update()
    time.sleep(0.1)
    snake.Move()
    
    if snake.head.distance(food) < 15:
        food.refresh()
        Score.add_point()
        snake.Extend()
    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
        Score.Reset()
        snake.Reset()
    for segment in snake.Segments[1:]:
        if snake.head.distance(segment) < 10:
            Score.Reset()
            snake.Reset()

        

screen.exitonclick()