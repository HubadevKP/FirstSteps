# Global definitions for cal300
# Adding, Minus, Devide, Multiply, expo, square, pitagoras
# Ver 0.00.01 - 04.04.18


import math


def add(x, y):
    '''

    :param x: float number
    :param y: float number
    :return: x + y
    '''
    return x + y


def sub(x, y):
    '''

    :param x: float number
    :param y: float number
    :return: x - y
    '''
    return x - y


def multi(x, y):
    '''

    :param x: float number
    :param y: float number
    :return: x * y
    '''
    return x * y


def div(x, y):
    '''

    :param x: float number
    :param y: float number
    :return: x / y
    '''
    return x / y


def expo(x, y):
    '''

    :param x: float number
    :param y: float number
    :return: x ** y
    '''
    return x ** y


def sqr(x):
    '''

    :param x: float number
    :return: square root x based on math python
    '''
    return math.sqrt(x)

def mod(x, y):
    '''

    :param x: float number
    :param y: float number
    :return: modulus x, y
    '''
    return x % y

def pit (x,y):
    '''

    :param x: float number
    :param y: float number
    :return: function to found c ** 2 in pitagoras
    '''
    return math.sqrt(x ** 2 + y ** 2)

