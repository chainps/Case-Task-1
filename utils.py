import datetime
from constants import WEEKDAYS_RU

def get_day_of_week(day, month, year):
    """Определяет день недели по дате."""
    try:
        birth_date = datetime.date(year, month, day)
        return WEEKDAYS_RU[birth_date.weekday()]
    except ValueError:
        return None # Если дата некорректна

def is_leap_year(year):
    """Определяет, является ли год високосным."""
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def calculate_age(day, month, year):
    """Вычисляет текущий возраст пользователя."""
    today = datetime.date.today()
    birth_date = datetime.date(year, month, day)
    age = today.year - birth_date.year
    
    # Корректировка, если день рождения еще не наступил в этом году
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
        
    return age