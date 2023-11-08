def area(a):
    '''получает на вход a, возвращает площадь квадрата со стороной a'''
    if not isinstance(a, int) and not isinstance(a, float):
        return "error"
    elif a <= 0:
        return "error"

    return a * a


def perimeter(a):
    '''получает на вход a, возвращает периметр квадрата со стороной a'''
    if not isinstance(a, int) and not isinstance(a, float):
        return "error"
    elif a <= 0:
        return "error"

    return 4 * a
