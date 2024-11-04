from threading import Thread, Lock
import random
from time import sleep
class Bank():
    def __init__(self):
        self.lock = Lock()
        self.balance = 0
    def deposit(self):
        for i in range(100):
            #print(i,"-",self.lock.locked())
            transaction = random.randint(50,500)
            self.balance += transaction
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            print(f"Пополнение: {transaction}. Баланс: {self.balance}")
            sleep(0.001)


    def take(self):
        for i in range(100):
            transaction = random.randint(50, 500)
            print(f'Запрос на {transaction}')
            if transaction <= self.balance:
                self.balance -= transaction
                print(f"Снятие: {transaction}. Баланс: {self.balance}")
                sleep(0.001)
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()



if __name__ == "__main__":
    bk = Bank()
    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print(f'Итоговый баланс: {bk.balance}')
