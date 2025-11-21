def fib(n):
    num1 = 1
    num2 = 1
    for i in range(n):
        yield num1
        fib_num = num1 + num2
        num1 = num2
        num2 = fib_num



if __name__ == '__main__':
    for fib in fib(200):
        print(fib)