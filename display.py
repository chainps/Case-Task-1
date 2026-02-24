from constants import DIGIT_PATTERNS

def print_stylized_date(day, month, year):
    """Выводит дату звездочками (ASCII-арт)."""
    # Формируем строку: дд мм гггг
    date_str = f"{day:02d} {month:02d} {year:04d}"
    
    print("\nВаша дата рождения в стилизованном формате:")
    # Вывод построчно (всего 5 строк по высоте символов)
    for row in range(5):
        line_output = ""
        for char in date_str:
            line_output += DIGIT_PATTERNS[char][row] + "  "
        print(line_output)

def show_results(day, month, year, weekday, is_leap, age):
    """Выводит итоговую информацию в консоль."""
    print(f"\n--- Результаты анализа ---")
    print(f"Дата рождения: {day:02d}.{month:02d}.{year}")
    print(f"День недели: {weekday}")
    
    leap_text = "високосный" if is_leap else "не високосный"
    print(f"Год: {leap_text}")
    
    print(f"Ваш возраст: {age} лет")