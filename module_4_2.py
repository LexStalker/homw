def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

#inner_function() # Строка для проверки, вывод ошибки
# inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?

test_function() # Работает))




