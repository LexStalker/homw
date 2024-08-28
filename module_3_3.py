# Задача "Распаковка"
#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'Строка', c = True):
    print(a, b, c)

print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
#2.Распаковка параметров:
values_list = [1, 'Текст', True]
values_dict = {'a': 1, 'b': 'Текст', 'c': True}
print_params(*values_list)
print_params(**values_dict)
#3.Распаковка + отдельные параметры
values_list2 = [2, True]
print_params(*values_list2, 42)