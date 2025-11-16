
def read_data(filename):
    try:
        with open(filename) as file:
            data = file.readlines()
            print(data[1], end= "\n")
            print(data[0], end= "\n")
    except :
        print("Файл пустой или его не существует")

read_data("test1")
read_data("test2")