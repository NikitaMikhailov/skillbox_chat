"""
Пример программы для работы с функциями (аналог файла 01_hours_salary.py)

Аргументы
- стоимость часа в руб
- количество дней в руб

Сделать
- функцию, которая вернет размер зарплаты в руб
"""
def salary_func(hour_cost: int, day_quantity: int):
    final = 0.87 * (hour_cost * 8) * day_quantity
    return final

hour_cost = int(input("Укажите стоимость часа >>> "))
day_quantity = int(input("Укажите количество дней >>> "))

print(salary_func(hour_cost, day_quantity))


