from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Today {dt.today().day()}."
        f"Day of Week -  {dt.today().isoweekday()}."
    )
    n = int(input("Enter count of days: "))
    today = dt.today()
    result = today + td(days=n)
    print(
        f"Через {n} дней будет {result.date()}."
        f"День недели - {result.isoweekday()}."
    )
if __name__ == '__main__':
    main()