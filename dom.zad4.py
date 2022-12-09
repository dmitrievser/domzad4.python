# Задача 1. Вычислить число пи c заданной точностью d
#
# Пример:
# o	при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

from math import pi

d = input('Введите число d (точность вычисления числа Пи): ').split('.')
t = len(d[1])

print(round(pi, t))

# Задача 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.


n = int(input('Введите натуральное число N: '))
res_list = []

dl = 2
while dl <= n:
    if n % dl == 0:
        n /= dl
        res_list.append(dl)
    else:
        dl += 1

print(res_list)

# Задача 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#
# [1, 2, 2, 3, 4]  -> [1, 3, 4]

user_set = [int(i) for i in input('Введите последовательность чисел: ').split()]
sl = {}
res_list = []

for el in user_set:
    sl[f'{el}'] = user_set.count(el)

for key, value in sl.items():
    if value == 1:
        res_list.append(int(key))

print(res_list)

# Задача 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# Пример:
# o	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень k: '))

random_coef = []
for i in range(0, k + 1):
    n = random.randint(0, 9)
    random_coef.append(n)


# функция возвращает многочлен на основе списка коэффициентов
def create_mn(k, coef):
    mn = []
    for i in range(0, len(coef) - 2):
        if coef[i] == 0:
            continue
        elif coef[i] == 1:
            x = f'x^{k - i}'
        else:
            x = f'{coef[i]}x^{k - i}'
        mn.append(x)
    for i in range(len(coef) - 2, len(coef) - 1):
        if coef[i] == 0:
            continue
        elif coef[i] == 1:
            x = 'x'
        else:
            x = f'{coef[i]}x'
        mn.append(x)
    for i in range(len(coef) - 1, len(coef)):
        if coef[i] == 0:
            continue
        else:
            x = f'{coef[i]}'
        mn.append(x)
    return mn


res_mn = ' + '.join(create_mn(k, random_coef)) + ' = 0'
print(res_mn)

with open('for_task_4.txt', 'w') as file:
    file.write(res_mn)

# Задача 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


with open('for_task_5_1.txt') as f1:  # получаем 1й многочлен из одного файла
    first_mn = f1.read()

with open('for_task_5_2.txt') as f2:  # получаем 2й многочлен из другого файла
    second_mn = f2.read()

print(first_mn, second_mn, sep='\n')  # выводим исходные многочлены в терминал


# функция удаляет символы сложения и равенство нулю и возвращает список членов многочлена
def eliminate_symbols(mn):
    mn = mn.split()
    sp_mn = []
    for el in mn:
        if el == '+' or el == '=' or el == '0':
            continue
        else:
            sp_mn.append(el)
    return sp_mn


# функция возвращает словарь из членов многочлена со значением коэффициентов
def separate_mn(sp_mn):
    slov = {}
    for el in sp_mn:
        if 'x^' in el:
            cort = el.split('x')
            if cort[0] == '':
                slov[f'x{cort[1]}'] = '1'
            else:
                slov[f'x{cort[1]}'] = f'{cort[0]}'
        elif 'x' in el:
            cort = el.split('x')
            if cort[0] == '':
                slov[f'x{cort[1]}'] = '1'
            else:
                slov[f'x{cort[1]}'] = f'{cort[0]}'
        else:
            cort = (el, '^0')
            slov[f'{cort[1]}'] = f'{cort[0]}'
    return slov


# функция возвращает суммарный
def sum_mn(sl_1, sl_2):
    sum_sl = {}
    if len(sl_1) >= len(sl_2):
        big_sl = sl_1
        small_sl = sl_2
    else:
        big_sl = sl_2
        small_sl = sl_1
    for key, value in big_sl.items():
        if key in small_sl:
            sum_sl[key] = int(big_sl[key]) + int(small_sl[key])
        else:
            sum_sl[key] = int(big_sl[key])
    for key, value in small_sl.items():
        if key not in big_sl:
            sum_sl[key] = int(small_sl[key])
    sum_sl = dict(sorted(sum_sl.items(), key=lambda x: x[0], reverse=True))
    return sum_sl


# функция возвращает многочлен на основе суммарного словаря
def create_mn(sum_slov):
    mn = []
    for key, value in sum_slov.items():
        if value == 1:
            c = f'{key}'
        else:
            c = f'{value}{key}'
        if key == '^0':
            c = f'{value}'
        mn.append(c)
    return mn


slov_1 = separate_mn(eliminate_symbols(first_mn))
slov_2 = separate_mn(eliminate_symbols(second_mn))
res_sl = sum_mn(slov_1, slov_2)
result = ' + '.join(create_mn(res_sl)) + ' = 0'
print('\nСумма многочленов равна: ')
print(result)

with open('for_task_5_fin.txt', 'w') as file:
    file.write(result)

