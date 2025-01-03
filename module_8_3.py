class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, vin_number, numbers):
        self.model = model
        self.__vin = vin_number
        self.__numbers = numbers

        if not self.__is_valid_vin(vin_number):
            raise IncorrectVinNumber("Некорректный тип vin номер")

        if not self.__is_valid_numbers(numbers):
            raise IncorrectCarNumbers("Некорректный тип данных для номеров")

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            return False

        if vin_number < 1000000 or vin_number > 9999999:
            return False

        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            return False

        if len(numbers) != 6:
            return False

        return True

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')