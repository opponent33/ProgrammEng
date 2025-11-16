def check(input_func):
    def output_func(*args):
        name, age = args[0], args[1]
        if age < 0 or age > 130:
            age = "Недопустимый возраст"
            return name, age
    return output_func

@check
def personal_info(name, age):
    print(f"Name: {name}, Age: {age}")


if __name__ == '__main__':
    print(personal_info("Vladimir", 38))
    print(personal_info("Alexandr", -5))
    print(personal_info("Pyotr", 138, 15, 48, 2))

