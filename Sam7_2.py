def main():
    while True:
        print("\n1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            show_expenses()
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

def add_expense():
    date = input("Введите дату (гггг-мм-дд): ")
    category = input("Введите категорию расхода: ")
    amount = input("Введите сумму расхода: ")
    description = input("Введите описание расхода: ")
    with open('expenses.txt', 'a', encoding='utf-8') as file:
        file.write(f"{date} | {category} | {amount} | {description}\n")
    print("Расход успешно добавлен!")

def show_expenses():
    try:
        with open('expenses.txt', 'r', encoding='utf-8') as file:
            expenses = file.readlines()

        if not expenses:
            print("Расходы пока не добавлены.")
        else:
            print("\nВсе расходы:")
            for i, expense in enumerate(expenses, 1):
                print(f"{i}. {expense.strip()}")
    except FileNotFoundError:
        print("Файл с расходами не найден. Сначала добавьте расходы.")


if __name__ == "__main__":
    main()