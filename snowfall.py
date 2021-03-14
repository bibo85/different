# -*- coding: utf-8 -*-

# Реализация снегопада через классы с помощью библиотеки simple-draw

from random import randint
import simple_draw as sd  # simple-draw

WIDTH = 1200
HEIGHT = 600

N = 40  # Количество снежинок в снегопаде


class Snowflake:

    def __init__(self):
        self.x = randint(0, WIDTH)
        self.y = randint(HEIGHT, HEIGHT * 3)
        self.length = randint(10, 50)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        # закрашиваем предыдущую снежинку цветом фона для получения эффекта полета снежинок
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def move(self):
        self.x += randint(-10, 10)  # горизонтальный сдвиг по x координат
        self.y -= randint(5, 15)  # вертикальный сдвиг по y координат

    def draw(self):
        next_point = sd.get_point(self.x, self.y)
        sd.snowflake(center=next_point, length=self.length)  # отрисовка снежинки цветом

    def can_fall(self):
        return self.y > self.length  # если снежинка еще не упала


def get_flakes(count):
    new_flakes = []
    for _ in range(count):
        new_flake = Snowflake()
        new_flakes.append(new_flake)
    return new_flakes


def get_fallen_flakes(flakes):
    fallen_flakes = []
    for i, flake in enumerate(flakes):
        if not flake.can_fall():
            fallen_flakes.append(i)
    return fallen_flakes


def remove_flakes(fallen_flakes, flakes):
    for i in sorted(fallen_flakes, reverse=True):  # обратная сортировка, чтобы удалить отдельные индексы
        del flakes[i]


def append_flakes(count_fallen_flakes, flakes):
    for _ in range(count_fallen_flakes):
        flake = Snowflake()
        flakes.append(flake)


sd.resolution = (WIDTH, HEIGHT)

flakes = get_flakes(N)  # создать список снежинок

while True:
    sd.start_drawing()
    for flake in flakes:  # рисуем снежинки
        flake.clear_previous_picture()  # очистка предыдущего положения снежинки
        flake.move()  # сдвиг
        flake.draw()  # отрисовка
    fallen_flakes = get_fallen_flakes(flakes)  # считаем сколько снежинок уже упало
    if fallen_flakes:
        remove_flakes(fallen_flakes, flakes)  # Удаляем те, что упали
        flakes.extend(get_flakes(len(fallen_flakes)))  # добавляем сверху столько, сколько уже упало
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
