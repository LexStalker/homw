import threading
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding= 'utf8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1}\n')
            sleep(0.1)

time_start = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_end = datetime.now()

time_res_fun = time_end - time_start
print(f'Время выполнения - {time_res_fun}')

thr1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thr2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thr3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thr4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thr1.start()
thr2.start()
thr3.start()
thr4.start()
thr1.join()
thr2.join()
thr3.join()
thr4.join()
time_end = datetime.now()
time_res_f = time_end - time_start
print(f'Выполнение в потоке - {time_res_f}')
print(f'Разница в выполнении - {time_res_f - time_res_fun}')