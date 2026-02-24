import datetime
from utils import get_day_of_week, is_leap_year, calculate_age
from display import print_stylized_date, show_results

def main():
    print("Программа анализа даты рождения.")
    
    try:
        # Запрос данных
        d = int(input("Введите день рождения (число): "))
        m = int(input("Введите месяц рождения (число): "))
        y = int(input("Введите год рождения (число): "))

        # Проверка корректности даты перед вычислениями
        datetime.date(y, m, d)

        # Вычисления (логика)
        weekday = get_day_of_week(d, m, y)
        leap = is_leap_year(y)
        age = calculate_age(d, m, y)

        # Вывод результатов
        show_results(d, m, y, weekday, leap, age)
        print_stylized_date(d, m, y)

    except ValueError:
        print("\n[ОШИБКА] Вы ввели некорректные данные или несуществующую дату!")
    except Exception as e:
        print(f"\n[ОШИБКА] Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    main()