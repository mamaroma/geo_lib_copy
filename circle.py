import math


def area(r):
    ''' получает на вход r > 0, возвращает площадь круга с радиусом r '''
    if not isinstance(r, int) and not isinstance(r, float):
        return "error"
    elif r <= 0:
        return "error"

    return math.pi * r * r


def perimeter(r):
    ''' получает на вход r > 0, возвращает периметр круга с радиусом r '''
    if not isinstance(r, int) and not isinstance(r, float):
        return "error"
    elif r <= 0:
        return "error"

    return 2 * math.pi * r