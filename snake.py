import turtle
import random
import math
import time

delay=0.1
#screen
wn = turtle.Screen()
wn.title('snake game')
wn.bgpic("C:/Users/MODT/py/game/bgg.gif")
wn.setup(width=736, height=736)

#boundries
pen=turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color('lightpink')
pen.setposition(-300,-300)
pen.pendown()
pen.showturtle()
pen.pensize(3)
def draw() :
    global pen
    wn.tracer(1)
    pen.penup()
    pen.hideturtle()
    pen.pendown()
    pen.showturtle()
    for side in range(4):
        pen.forward(600)
        pen.left(90)
    pen.hideturtle()
    wn.tracer(0)

#snake
snake = turtle.Turtle()
snake.speed(0)
snake.color('darkgreen')
snake.shape('triangle')
snake.shapesize(0.75)
snake.penup()
snake.direction = "stop"

#writing score
score=0
score_d = turtle.Turtle()
score_d.color("deeppink")
score_d.hideturtle()
score_d.penup()
score_d.goto(-250, 250)   
score_d.write(f'Score:{score}', align="center", font=("Arial", 16, "normal"))

#writing lives
lives=6
lives_d = turtle.Turtle()
lives_d.color("deeppink")
lives_d.hideturtle()
lives_d.penup()
lives_d.goto(-170, 250)   
lives_d.write(f'lives:{lives}', align="center", font=("Arial", 16, "normal"))

wn.tracer(0)

#apple
apple = turtle.Turtle()
apple.hideturtle()
apple.color('red')
apple.shape('circle')
apple.penup()

#spawn
def respawn(thing,x,y,h=0):
    thing.hideturtle()
    thing.setposition(x, y)
    thing.setheading(h)
    thing.showturtle()
    wn.ontimer(thing.showturtle, 100)

#collision
def isCollision(t1,t2,thr):
    d=math.sqrt(((t1.xcor()-t2.xcor())**2)+((t1.ycor()-t2.ycor())**2))
    if d < thr :
        return True
    else:
        return False

#food poss
def move_food():
    x = random.randint(-295, 295)
    y = random.randint(-295, 295)
    return [x , y]

#body 
snake_body=[]
#mooving
step=15
def move():
    if snake.direction == 'up':
        snake.sety(snake.ycor()  +step)
    if snake.direction == 'down':
        snake.sety(snake.ycor()  -step)
    if snake.direction == 'right':
        snake.setx(snake.xcor()  +step)
    if snake.direction == 'left':
        snake.setx(snake.xcor()  -step)
    
def turnright():
    if snake.direction !='left':
        snake.direction = 'right'
        snake.setheading(0)
def turnleft():
    if snake.direction !='right':
        snake.direction = 'left'
        snake.setheading(180)
def goup():
    if snake.direction !='down' :
        snake.direction = 'up'
        snake.setheading(90)
def godown():
    if snake.direction !='up' :
        snake.direction = 'down'
        snake.setheading(270) 

#keys
turtle.listen()
turtle.onkey(turnright,'Right')
turtle.onkey(turnleft,'Left')
turtle.onkey(goup,'Up')
turtle.onkey(godown,'Down')

speed=2
# lost 
lost = turtle.Turtle()
lost.color("deeppink")
lost.hideturtle()
lost.penup()
lost.goto(-100, 280)   

replay = turtle.Turtle()
replay.color("deeppink")
replay.hideturtle()
replay.penup()
replay.goto(-250, 100)   

leave = turtle.Turtle()
leave.color("deeppink")
leave.hideturtle()
leave.penup()
leave.goto(20, 100)   

def close_game():
    wn.bye()

def game_over():
    global lost,replay,leave 
    snake.hideturtle()
    apple.hideturtle()
    score_d.clear()
    lives_d.clear()
    pen.clear()
    lost.write(f'GAME OVER !', align="left", font=("Arial", 24, "normal"))
   
    replay.write(f'-To restart:\n press Enter ', align="left", font=("Arial", 20, "normal"))
  
    leave.write('-To exit: .\n press space ', align="left", font=("Arial", 20, "normal"))

    turtle.listen()
    turtle.onkey(main_game,'Return')
    turtle.onkey(close_game,'space')

def main_game():
    global lives,score,snake_body
    leave.clear()
    replay.clear()
    lost.clear()
    for seg in snake_body:
        seg.hideturtle()
    snake_body = []
    lives_d.write(f'lives:{lives}', align="center", font=("Arial", 16, "normal"))
    score=0
    lives=6
    score_d.write(f'Score:{score}', align="center", font=("Arial", 16, "normal"))
    draw()
    X,Y = move_food()
    apple.showturtle()
    respawn(apple,X,Y)
    respawn(snake,0,0)
    
    while lives!= 0 :
        wn.update()
    
        time.sleep(delay)
        for i in range(len(snake_body)-1,0,-1):
            x = snake_body[i-1].xcor()
            y = snake_body[i-1].ycor() 
            respawn(snake_body[i],x,y)
        if len(snake_body) > 0 :
            respawn(snake_body[0],snake.xcor(),snake.ycor())

        move()

        if ( snake.xcor() >= 300 or  snake.xcor() <= -300 ) or (snake.ycor() >= 300 or  snake.ycor() <= -300) or any(isCollision(snake,t,10)for t in snake_body[1:]):
            respawn(snake,0,0,snake.heading())
            lives -= 1
            lives_d.clear()
            lives_d.write(f'lives:{lives}', align="center", font=("Arial", 16, "normal"))
        if isCollision(snake,apple,20) :
            score += 1
            score_d.clear()
            score_d.write(f'Score:{score}', align="center", font=("Arial", 16, "normal"))
            tail = turtle.Turtle()
            tail.shape("square")
            tail.color("green")
            tail.shapesize(0.75)
            tail.penup()
            tail.hideturtle()
            snake_body.append(tail)
            X,Y = move_food()
            respawn(apple,X,Y)
    game_over()

main_game()

wn.mainloop()