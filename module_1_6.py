my_dict = {'Alex': 1994, 'Denis': 2002}
print(my_dict)
print(my_dict['Alex'])
print(my_dict.get('Egor'))
my_dict.update({'Damir': 1991,
                'Chery': 2024})
print(my_dict)
a = my_dict.pop('Chery')
print(my_dict)
print(a)

my_set = {1, 2, 3, 4, 1, 2, 3, 4, 5, 'func', 'voice', 'func'}
print(my_set)
print(my_set.add(6))
print(my_set.add(8))
print(my_set.discard(4))
print(my_set)