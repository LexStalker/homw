def add_everything_up(a, b):
    """
    Складывает числа (int, float) и строки (str).
    Если аргументы имеют разные типы (число и строка), возвращает их строковое представление.
    """
    try:
        # Если оба аргумента являются числами, складываем их
        return a + b
    except TypeError:
        # Если аргументы имеют разные типы, возвращаем их строковое представление
        return str(a) + str(b)

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
