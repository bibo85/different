# -*- coding: utf-8 -*-

import turtle
import random

WIDTH = 600
HEIGHT = 600
DX = 3  # скорость движения по x
DY = 4  # скорость движения по x

# настройка игрового окна
window = turtle.Screen()
window.title('Bounce ball')

# рисуем игровое поле
border = turtle.Turtle()
border.speed(0)
border.pencolor('red')
border.pensize(5)
border.hideturtle()
border.penup()
border.goto(WIDTH // 2, HEIGHT // 2)
border.pendown()
border.goto(WIDTH // 2, -HEIGHT // 2)
border.goto(-WIDTH // 2, -HEIGHT // 2)
border.goto(-WIDTH // 2, HEIGHT // 2)
border.goto(WIDTH // 2, HEIGHT // 2)

# рисуем мячик
ball = turtle.Turtle()
ball.hideturtle()
ball.shape('circle')
ball.color('red')
ball.penup()

# заставляем мячик двигаться
random_x = random.randint(-WIDTH // 2 + 10, WIDTH // 2 - 10)
random_y = random.randint(-HEIGHT // 2 + 10, HEIGHT // 2 - 10)

ball.goto(random_x, random_y)
ball.showturtle()

while True:
    x, y = ball.position()
    if x + DX >= WIDTH // 2 - 7 or x + DX <= -WIDTH // 2 + 7:
        DX = -DX
    if y + DY >= HEIGHT // 2 - 7 or y + DY <= -HEIGHT // 2 + 7:
        DY = -DY
    ball.goto(x + DX, y + DY)

window.mainloop()
