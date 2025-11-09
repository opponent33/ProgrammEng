class Ivan:
    __slots__ = ["name"]

    def __init__(self, name):
        if name == "Иван":
            self.name = f"Yes, I'm {name}"
        else:
            self.name = f"No, I'm {name}"

person1 = Ivan('Алексей')
person2 = Ivan("Иван")
print(person1.name)
print(person2.name)

person2.surname == "Петров"