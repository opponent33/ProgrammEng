class Tomato:
    states = ["отсутствует",
              "Цветение",
              "Зеленый",
              "Красный"]
    def __init__(self, _index, _state = states[0]):
        self._index = _index
        self._state = _state

    def get_state(self):
        return self._state

    def set_state(self, _state):
        self._state = _state

    def grow(self):
        # Находим текущую стадию в списке и берем следующую
        # Переводим помидор на следующую стадию, если он еще не созрел
        curr_state = self.states.index(self.get_state())
        if curr_state < len(self.states) - 1:
            self.set_state(self.states[curr_state + 1])
        else:
            print("Такой стадии нет!")

    def is_ripe(self):# Проверяем, созрел ли помидор (достиг последней стадии)
        return self.get_state() == "Красный"

class TomatoBash:
    def __init__(self, count):
        self.count = count
        self.tomatoes = []
        for index in range(self.count):
            self.tomatoes.append(Tomato(index))
    def grow_all(self):# Растим все помидоры на кусте
        for tomato in self.tomatoes:
            tomato.grow()
        print("Все помидоры чуть-чуть подросли")

    def all_are_ripe(self):
        # Проверяем, все ли помидоры на кусте созрели
        count_of_ripe = 0
        for tomato in self.tomatoes:
            if tomato.is_ripe():
                count_of_ripe += 1
        if count_of_ripe == self.count:
            print("Все помидоры созрели")
            return True
        else:
            print(f"Созрело {count_of_ripe} из {self.count} помидоров")
            return False

    def give_away_all(self): # Проверяем все ли созрели, собираем урожай, очищаем список помидоров
        if self.all_are_ripe():
            self.tomatoes.clear()
            print("Урожай собран.")


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):# Садовник ухаживает за растением
        self._plant.grow_all()

    def harvest(self): # Сбор урожая
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
        else:# Если не созрели - выводим сообщение
            print("Вы еще не можете убрать урожай. Не все помидоры выросли")

    @staticmethod # Статический метод - выводит справочную информацию
    def knowledge_base():
                # Статический метод - выводит справочную информацию
                print("Cправка по садоводству:")
                print("1. Помидоры проходят 4 стадии созревания:")
                print("- отсутствует")
                print("- цветение")
                print("- зеленый")
                print("- красный")
                print("2. Садовник должен ухаживать за кустом, чтобы помидоры росли")
                print("3. Урожай можно собрать только когда все помидоры красные\n")

if __name__ == "__main__":
    # Выводим справку по садоводству
    Gardener.knowledge_base()

    # Создаем куст с 3 помидорами
    bush = TomatoBash(7)
    # Создаем садовника с именем Петрович для ухода за кустом
    gardener = Gardener("Петрович", bush)

    # Последовательность действий:
    # 1. Садовник ухаживает за кустом первый раз
    gardener.work()
    # 2. Пытается собрать урожай (еще рано)
    gardener.harvest()
    # 3. Продолжает ухаживать
    gardener.work()
    # 4. Еще раз ухаживает
    gardener.work()
    # 5. Собирает урожай (теперь все помидоры созрели)
    gardener.harvest()
