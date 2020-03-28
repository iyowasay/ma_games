import turtle
import random
import time
import tkinter as tk
from tkinter import messagebox


def choose_color(t):
    ans = t.textinput("Green, Blue, Purple, Orange", "Choose a color!")
    if ans is None or ans.lower() not in ["blue", "orange", "purple", "green"]:
        print("Choose again please.")
        choose_color(t)
    else:
        return ans

screen = turtle.Screen()
screen.bgcolor("green")
answer = screen.textinput("Welcome to Snakeeeee", "What is your name?")
if answer is None or answer.lower().startswith('n'):
    print("Goodbye!")
    screen.clear()
    screen.bye()
else:
    player_name = answer
    time.sleep(0.65)
    head_color = choose_color(screen)


window = turtle.Screen()
window.bgcolor("black")
window.title("Snakeeeee")
window.tracer(0)

#constants
touch_accuracy = 16
move_speed = 19
snake_number = 1
# square_size = 18
delay = 0.06
current_score = high_score = 0
bad = None

#border
border_number = 284
smaller_bound = 250
border_constrain = 290

border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
length = 290
border.setposition(-length, -length)
border.pendown()
border.pensize(3)
for side in range(4):
    border.fd(length*2)
    border.lt(90)
border.hideturtle()

#snake
snake = turtle.Turtle()
snake.shape("square")
snake.color(head_color)
snake.pensize(3)
snake.penup()
snake.speed(0)
snake.setposition(0, 0)
snake.direction = "stop"

#good food
dot = turtle.Turtle()
dot.color("red")
dot.shape("circle")
dot.pensize(3)
dot.penup()
dot.speed(0)
dot.setposition(random.randint(- border_number, border_number), random.randint(- border_number, border_number))


#score
score = turtle.Turtle()
score.color("white")
score.shape("square")
score.penup()
score.speed(0)
score.hideturtle()
score.goto(0, 300)
score.write(player_name + "'s Score: 0  High Score: 0 ", align="center", font=("Courier", 24, "normal"))


def move():
    if snake.direction == "right":
        pre_x[0] = snake.xcor()
        pre_y[0] = snake.ycor()
        x = snake.xcor()
        snake.setx(x + move_speed)
    elif snake.direction == "left":
        pre_x[0] = snake.xcor()
        pre_y[0] = snake.ycor()
        x = snake.xcor()
        snake.setx(x - move_speed)
    elif snake.direction == "up":
        pre_x[0] = snake.xcor()
        pre_y[0] = snake.ycor()
        y = snake.ycor()
        snake.sety(y + move_speed)
    elif snake.direction == "down":
        pre_x[0] = snake.xcor()
        pre_y[0] = snake.ycor()
        y = snake.ycor()
        snake.sety(y - move_speed)
    elif snake.direction == "stop":
        snake.setposition(0, 0)

    for i in range(snake_number - 1):
        pre_x[i + 1] = add_snake[i].xcor()
        pre_y[i + 1] = add_snake[i].ycor()
        add_snake[i].setx(pre_x[i])
        add_snake[i].sety(pre_y[i])


def move_right():
    snake.direction = "right"
def move_left():
    snake.direction = "left"
def move_up():
    snake.direction = "up"
def move_down():
    snake.direction = "down"
def pause():
    snake.direction = "stop"
def close_it():
    window.bye()


#keypress
window.listen()
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(close_it, "Escape")
# window.onkeypress(pause, "p")
# window.onkeypress(close_it, "c")

add_snake = []
while True:
    window.update()
    pre_x = [None] * snake_number
    pre_y = [None] * snake_number

    move()
    if snake.xcor() > border_constrain or snake.xcor() < -border_constrain or snake.ycor() > border_constrain or \
            snake.ycor() < -border_constrain:
        snake.direction = "stop"
        messagebox.showinfo(title=None, message="Out of bounds!")
        window.listen()
        for n in add_snake:
            n.goto(10000, 10000)

        snake_number = 1
        delay = 0.06
        time.sleep(0.1)
        add_snake = []
        if bad:
            bad.goto(-10000, -10000)
            bad = None
    else:
        for k in range(snake_number - 1):
            if (add_snake[k].xcor() == snake.xcor() and add_snake[k].ycor() == snake.ycor()) or (bad and bad.xcor() - touch_accuracy < snake.xcor() < bad.xcor() + touch_accuracy and bad.ycor() - touch_accuracy < snake.ycor() < bad.ycor() + touch_accuracy):
                snake.direction = "stop"
                messagebox.showinfo(title=None, message="You LOSERRR!")
                window.listen()

                for n in add_snake:
                    n.goto(10000, 10000)

                snake_number = 1
                delay = 0.06
                time.sleep(0.1)
                add_snake = []
                if bad:
                    bad.goto(-10000, -10000)
                    bad = None
                break

    if dot.xcor() - touch_accuracy < snake.xcor() < dot.xcor() + touch_accuracy and dot.ycor() - touch_accuracy < snake.ycor() < dot.ycor() + touch_accuracy:
        snake_number += 1
        dot.setposition(random.randint(-border_number, border_number), random.randint(-border_number, border_number))
        if 10 < snake_number <= 20 and (snake_number+1) % 4 == 0:
            bad.setposition(random.randint(- smaller_bound, smaller_bound), random.randint(- smaller_bound, smaller_bound))

        delay -= 0.0015
        add_snake.append(turtle.Turtle())
        add_snake[snake_number - 2].shape("square")
        add_snake[snake_number - 2].color("white")
        add_snake[snake_number - 2].pensize(3)
        add_snake[snake_number - 2].penup()
        add_snake[snake_number - 2].speed(0)
        add_snake[snake_number - 2].setposition(snake.xcor(), snake.ycor())
    if not bad and current_score >= 90:
        # bad food
        bad = turtle.Turtle()
        bad.color("yellow")
        bad.shape("circle")
        bad.pensize(3)
        bad.penup()
        bad.speed(0)
        bad.setposition(random.randint(- smaller_bound, smaller_bound), random.randint(- smaller_bound, smaller_bound))

    current_score = (snake_number - 1) * 10
    if current_score >= high_score:
        high_score = current_score
    score.clear()
    score.write(player_name + "'s Score: " + str(current_score) + " High Score: " + str(high_score), align="center",
                font=("Courier", 24, "normal"))
    time.sleep(delay)

