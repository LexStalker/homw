import io
from pprint import pprint
def custom_write(file_name: str, strings: list):
    strings_position = {}
    strings_number = 0
    file = open(file_name= 'w', encoding= 'utf-8')
    for string in strings:
        byte_position = file.tell()
        strings_number += 1
        file.write(strings + '\n')
        strings_position[(strings_number, byte_position)] = string
        return strings_position
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)

