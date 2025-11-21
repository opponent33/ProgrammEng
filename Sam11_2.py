from Sam11_1 import fib

with open("fib.txt", "w") as file:
    for num in fib(200):
        file.write(str(num) + '\n')
