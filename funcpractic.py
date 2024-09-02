# Максимум в списке
# Подсчёт четных чисел в списке
# Уникальный список


def find_max(list_):
    max_ = list_[0]
    for i in list_:
        if i > max_:
            max_ = i
    return max_


print(find_max([25, 36, -2, -6, 64, 258]))

def count_even(list_):
    counter = 0
    for i in list_:
        if i == 0:          # 0 входит в чётные числа, строка чтобы убрать привязку к определению 0 как чётного числа.
            continue
        if i % 2 == 0:
            counter += 1
    return counter

print(count_even([2, 4, 6, 8, 3, 5, 9, 12, 0]))


def unique(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)

    return new_list


print(unique([1, 2, 3, 4, 5, 6, 7, 8, 12, 1, 2, 3, 4, 5, 6, 7, 8, 14]))

