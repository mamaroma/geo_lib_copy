def area(a, b):
    '''принимает стороны a > 0 и b > 0, возвращает произведение a и b'''
    if not isinstance(a, int) and not isinstance(a, float):
        return "error"

    elif not isinstance(b, int) and not isinstance(b, float):
        return "error"

    elif a <= 0 or b <= 0:
        return "error"

    return a * b


def perimeter(a, b):
    '''принимает на вход a > 0 и b > 0, возвращает периметр прямоугольника со сторонами a и b'''
    if not isinstance(a, int) and not isinstance(a, float):
        a = 0

    if not isinstance(b, int) and not isinstance(b, float):
        b = 0

    if a <= 0 or b <= 0:
        return "error"

    return 2 * (a + b)
