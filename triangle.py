def area(a, h):
    '''получает на вход a > 0 и h > 0, возвращает площадь треугольника со стороной a, и высотой h, проведённой к этой стороне'''
    if not isinstance(a, int) and not isinstance(a, float):
        return "error"

    elif not isinstance(h, int) and not isinstance(h, float):
        return "error"

    elif a <= 0 or h <= 0:
        return "error"

    return a * h / 2


def perimeter(a, b, c): 
    '''получает на вход a > 0, b > 0 и с > 0, возвращает площадь треугольника со сторонами а, b и с'''
    if not isinstance(a, int) and not isinstance(a, float):
        return "error"

    elif not isinstance(b, int) and not isinstance(b, float):
        return "error"

    elif not isinstance(c, int) and not isinstance(c, float):
        return "error"

    elif a <= 0 or b <= 0 or c <= 0:
        return "error"

    return a + b + c
