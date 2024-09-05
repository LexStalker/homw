import tkinter as tk        # tkinter Библиотека для графических окон.

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)




window = tk.Tk()
window.title('Калькулятор')     # .title для того чтобы переиминовать окно.
window.geometry('350x350')      # .geometry Для размера окна.
window.resizable(False, False)      # .resizzable(False) Для того чтобы окно нельзя было изменять в размере.
button_add = tk.Button(window, text='+', width=2, height=2, command=add)      #Создание кнопки
button_add.place(x=100, y=220)      # .place размещает элемент в окне.
button_sub = tk.Button(window, text='-', width=2, height=2, command=sub)
button_sub.place(x=125, y=220)
button_mul = tk.Button(window, text='*', width=2, height=2, command=mul)
button_mul.place(x=150, y=220)
button_div = tk.Button(window, text='/', width=2, height=2, command=div)
button_div.place(x=175, y=220)
# button_equ = tk.Button(window, text='=', width=2, height=4)
# button_equ.place(x=200, y=220)
number1_entry = tk.Entry(window, width=28,)      #.Entry для текстовых полей
number1_entry.place(x=100, y=50)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=100)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100,y=325)
number1 = tk.Label(window, text='Введите первое число:')    #.Label для создания надписей
number1.place(x=100, y=25)
number2 = tk.Label(window, text='Введите второе число:')
number2.place(x=100, y=75)
answer = tk.Label(window, text='Результат')
answer.place(x=100, y=300)
window.mainloop() #Обновляет информацию о просходящем на экране.

