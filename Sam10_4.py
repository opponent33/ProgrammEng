class MyDecorator:
    def __init__(self, func):
        self.func = func
        self.count = 0
        print(f"Декоратор создан для функции: {self.func.__name__}")
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Вызвана функция: '{self.func.__name__}' (Вызов: #{self.count}) ---")
        result = self.func(*args, **kwargs)
        return result

@MyDecorator
def say_hello(name):
    print(f"Привет!{name}! Добро пожаловать!")

@MyDecorator
def add_numbers(a, b):
    sum_result = a + b
    print(f"Cумма числа {a} и числа {b} это {sum_result}.")
    return sum_result

say_hello("Алиса")
say_hello("Боб")
result = add_numbers(10, 5)
print(f"Возвращенное значение: {result}")
say_hello("Карл")
add_numbers(100, 200)
