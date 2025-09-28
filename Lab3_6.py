string = '124abc'
value = input("Введите символ: ")
for i in string:
    if i == value:
        index = string.index(i)
        print(f"Буква {value} есть в строке под {index} индексом")
        break
    else:
        print(f"Буквы {value} нет в указанной строке")