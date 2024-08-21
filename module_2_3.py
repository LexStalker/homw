my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
n = 0
while n < len(my_list):
    number = my_list[n]
    n = n + 1
    if number == 0:
        continue
    elif number < 0:
       # print('Дошли до отрицательного числа:', number) # Сторока для проверки вывода
        break  # Выходим из цикла, если встретили отр. число.
    elif n == len(my_list):
        print(number)
    else:
        print(number)


