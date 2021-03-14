# -*- coding: utf-8 -*-

import simple_draw as sd

# Функция-фабрика для отрисовки фигур многоугольников
# Функция принимать параметр n - количество сторон

POINT_X = 300
POINT_Y = 150
ANGLE = 13
LENGTH = 100


def get_polygon(n):  # фабрика фигур
    def drawing_shape(point, angle, length):  # общая функция отрисовки фигуры
        start_point = point
        shape_angle = round(360 / n)  # вычисляем градус каждого угла фигуры
        for current_angle in range(angle, 360 - shape_angle, shape_angle):  # проходим по углам фигуры
            point = sd.vector(start=point, angle=current_angle, length=length)
        sd.line(start_point=point, end_point=start_point)  # соединяем первую и последнюю точки линией

    return drawing_shape


N = int(input('Введите количество сторон фигуры: '))

draw_triangle = get_polygon(n=N)
draw_triangle(point=sd.get_point(POINT_X, POINT_Y), angle=ANGLE, length=LENGTH)

sd.pause()
