import json
import random

# задача 1. Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.
try:
    n = int(input('Введите натуральное число: '))
except:
    print('Введите натуральное число')
sp = []
while n != 1:
    for i in range(2,n+1):
        if n % i == 0:
            n = int(n / i)
            sp.append(i)
            break

print(sp)

            


# задача 2 . Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
try:
    num_list = input('Введите последовательность чисел через пробел: ')
    num_list = [int(i) for i in num_list.split()]
except:
    print('Введите числа')
unic_list = [] 
size = len(num_list)

def unic_el(lst):
    count = 0
    for i in range(size):
        for j in range(size):
            if lst[i] == lst[j]:
                count = count + 1
        if count == 1:
            unic_list.append(lst[i])
            count = 0
        else:
            count = 0
    print(f'список неповторяющихся элементов исходной последовательности')
    return unic_list
newlist = unic_el(num_list)
print(newlist)


# задача3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# *Пример:* 

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input('Введите степень: '))
koef = [i for i in range(100)]

x = None
polinom = f"{koef[random.randint(0,100)]} * x ** {k} + {koef[random.randint(0,100)]} * x ** {k-1} + {koef[random.randint(0,100)]}" 
with open ('file.txt', 'w') as data:
    data.write(polinom)

