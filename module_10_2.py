from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100
        self.days = 0
        print(f'{self.name}, на нас напали!')
    def run(self):
        while self.enemy > 0:
            self.days += 1
            sleep(1)
            self.enemy -= self.power
            print(f'{self.name}, сражается {self.days} {self.str_day()}, осталость {self.enemy} войнов')
        print(f'{self.name} одержал победу спустя {self.days} {self.str_day()}!')
    def str_day(self):
        day_ = int(str(self.days)[-1])
        if day_ == 1:
            return 'день'
        elif day_ in (2,3,4):
            return 'дня'
        else:
            return 'дней'
def str_day(days):
    day_ = str(days)[-1]
    print(day_)
    if day_ == 1:
        return 'день'
    elif day_ in (2, 3, 4):
        return 'дня'
    else:
        return 'дней'


if __name__ == '__main__':

    first_knight = Knight('Sir Lancelot', 10)
    first_knight.start()
    second_knight = Knight("Sir Galahad", 20)
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print('Битва окончена')