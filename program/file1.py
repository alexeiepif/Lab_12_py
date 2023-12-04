#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random as rnd
import matplotlib.pyplot as plt
from functools import lru_cache
import numpy as np
import timeit


def factorial_rec(n):
    """
    Функция, вычисляющая факториал рекурсивно
    """
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)


def fib_rec(n):
    """
    Функция, вычисляющая число фибонначи рекурсивно
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n - 2) + fib_rec(n - 1)

@lru_cache
def factorial_rec_lru(n):
    """
    Функция, вычисляющая факториал рекурсивно

    Оптимитизирована с использованием lru_cache
    """
    if n == 0:
        return 1
    else:
        return n * factorial_rec_lru(n - 1)

@lru_cache
def fib_rec_lru(n):
    """
    Функция, вычисляющая число фибонначи рекурсивно

    Оптимитизирована с использованием lru_cache
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec_lru(n - 2) + fib_rec_lru(n - 1)


def factorial_iter(n):
    """
    Функция, вычисляющая факториал итеративно
    """
    product = 1
    while n > 1:
        product *= n
        n -= 1
    return product


def fib_iter(n):
    """
    Функция, вычисляющая число фибонначи итеративно
    """
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a


def create_graph(b, c, namegraph):
    """
    Создание графика из точек и настройка окна
    """
    plt.scatter(b, c, s=5)
    plt.title(namegraph)
    plt.xlabel("Число, переданное в функцию")
    plt.ylabel("Время работы функции")


def func_time(case_func, size):
    """
    Замер времени выполнения функций для разных случаев
    """
    time = []
    repeat = 50
    N = [i for i in range(30)]
    for n in N:
        timer = timeit.timeit(
            lambda: case_func[0](n),
            number=repeat
        ) / repeat

        time.append(timer)

    plt.figure(case_func[1], size)
    plt.subplots_adjust(left=0.25)
    # Создание графиков
    create_graph(N, time, case_func[1])


if __name__ == '__main__':
    # Настройка размера окон
    dpi = 100
    width_inches = (1680 / dpi) / 4
    height_inches = (850 / dpi) / 2
    size = (width_inches, height_inches)
    functions = {
        factorial_rec: "Факториал рекурсивный",
        factorial_rec_lru: "Факториал рекурсивный с @lru_cache",
        factorial_iter: "Факториал итеративный",
        fib_rec: "Fibonacci рекурсивный",
        fib_rec_lru: "Fibonacci рекурсивный c @lru_cache",
        fib_iter: "Fibonacci итеративный"
    }
    for func_case in functions.items():
        func_time(func_case, size)

    # Показ графиков†
    plt.show()
