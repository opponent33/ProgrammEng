from math import sqrt
def geron(perimetr, a, b ,c):
    halfperimetr = perimetr / 2
    result = sqrt(halfperimetr * (halfperimetr - a)*(halfperimetr - b) * (halfperimetr - c))
    return result