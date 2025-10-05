from for_import2 import geron

a = int(input("Введите сторону A: "))
b = int(input("Введите сторону B: "))
c = int(input("Введите сторону C: "))
def treangle(a ,b ,c):
    perimetr = a + b + c
    if (a + b > c) and (b + c > a) and (c + a > b):
        print(geron(perimetr, a, b, c))
    else: print("Такого треугольника не существует")

if __name__ == '__main__':

    treangle(a, b, c)