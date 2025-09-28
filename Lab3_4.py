numbers = [1, 2, 3, 4, 54, 6, 73, 8, 9, 322]
value = int(input("enter the nuber: "))
if value in numbers:
    if value % 2 == 0:
        print("Переменная четная и есть в массиве")
    else:
        print("Переменная нечетная и есть в массиве")
else:
    print(f"Переменной нет в массиве и она равна {value}")