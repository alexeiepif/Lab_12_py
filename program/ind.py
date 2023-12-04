#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Опишите рекурсивную функцию, которая по заданным вещественному х и целому n
# вычисляет величину x^n.

def recursive_function(x, n):
    """
    Рекурсивная функция вычисляющая x^n
    """
    if n == 0:
        return 1
    elif n < 0:
        return 1 / recursive_function(x, abs(n))
    else:
        return x * recursive_function(x, n-1)


if __name__ == '__main__':
    x, n = tuple(
        map(
            int,
            input("Введите 2 числа х и n через пробел ").split()
        )
    )
    x_n = recursive_function(x, n)
    print("{}^{} = {}".format(x, n, x_n))
