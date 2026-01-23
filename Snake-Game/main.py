import time
import turtle as t
import snake as s
import Food as f
import scoreboard as sc

screen=t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake game ")
screen.tracer(0)

snake=s.Snake()
food=f.Food()
scoreboard=sc.Scoreboard()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with tail.
    for turtle in snake.turtles[1:]:
        if snake.head.distance(turtle) < 10:
            scoreboard.reset()
            snake.reset()

    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.xcor()>280 or snake.head.xcor()<-280:
        scoreboard.reset()
        snake.reset()





screen.exitonclick()