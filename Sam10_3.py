def sum_n(num):
    try:
        num += 3
        print(num)
    except TypeError:
        print("Ожидалось число. Неподходящий тип данных")

if __name__ == '__main__':
    sum_n(5)
    sum_n(0.1643)
    sum_n("fsdfsdfsdfs")
    sum_n('f')