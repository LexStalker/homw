immutable_var = tuple([1, 2, 3, 'a', 'b'])
print(immutable_var)
# immutable_var [0] = 4 # кортеж не поддерживает обращение по элементам #Убрать решётку для фукциональности работы ошибки.
mutable_list =  [1, 2, 3, 'a', 'b', 'yes']
print(mutable_list)
mutable_list[-1] = 'no'
print(mutable_list)