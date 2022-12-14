#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  # Подключение библиотеки 
import numpy  # Подключение библиотеки
import matplotlib.pyplot as mpp  # Подключение библиотеки, сокращение названия для вызова библиотеки 

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':  # Проверка запуска скрипта
    arguments = numpy.arange(0, 200, 0.1)  # Массив аргументов функции от 0 до 200 с шагом 0.1
    mpp.plot(  # Фунцкция, которая "вводит" точки графика
        arguments,  # Координаты точек по оси абсцисс
        [math.sin(a) * math.sin(a/20.0) for a in arguments]  # Координаты точек по оси ординат
    )
    mpp.show()  # Вывод графика на экран


