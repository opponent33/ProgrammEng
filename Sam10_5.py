class AccessError(Exception):
    def __init__(self, user, couse):
        self.user = user
        self.couse = couse
        message = f"Отказ в доступе для пользователя '{self.user}'. Причина: {self.couse}"
        super().__init__(message)

def check_age(user_name, age):
    min_age = 18
    if age < min_age:
        couse = f"Возраст ({age} лет) ниже минимально допустимого ({min_age} лет)."
        raise AccessError(user_name, couse)
    print(f"Доступ разрешен для {user_name} (Возраст: {age}).")

def check_time_access(user_name, curr_time):
    bgn_ban = 23
    finish_ban  = 7
    if curr_time >= bgn_ban or curr_time < finish_ban:
        couse = "Доступ запрещен в ночное время (с 23:00 до 07:00)."
        raise AccessError(user_name, couse)
    print(f"Доступ разрешен для {user_name} (Время: {curr_time}:00).")

try:
    check_age("Алиса", 25)
    check_age("Борис", 16)
except AccessError as e:
    print(f"Обработанная ошибка: {e}")

try:
    check_time_access("Виктор", 14)
    check_time_access("Дарья", 4)
except AccessError as e:
    print(f"Обработанная ошибка: {e}")