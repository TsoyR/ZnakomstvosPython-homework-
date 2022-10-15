import math

# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
#  Через строку нельзя решать.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

num1 = float(input("Введите целое или дробное число: "))

def sum_of_floatdigit(num):
    a = int(num)
    b = num - a
    temp_a = 0
    temp_b = 0
    sum = 0
    while a != 0:
        temp_a = temp_a + a % 10
        a = a // 10
    while b != 0:
        temp_b = temp_b + int(b*10)
        b = b * 10 - int(b * 10)
        b = round(b,10)
    sum = temp_a + temp_b
    return sum

result = sum_of_floatdigit(num1)

print(result)    
# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4) try:
try:    
    n = int(input("Введите число: "))
    numbers = []
    temp = 1
except:
    print("Введите целое число")

for i in range(n):
    temp = 1 * temp * (i+1)
    numbers.append(temp)
print(numbers)
    



# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.


str_1 = input("Введите первую строку: ")
str_2 = input("Введите вторую строку: ")

list1 = []
stop = len(str_2)
count = 0
for i in range(len(str_1)):
    list1.append(str_1[i:stop + i])

for i in range(len(list1)):
    if list1[i] == str_2:
        count = count + 1

print(f"Строка {str_2} найдена {count} раз(a)")
                 
# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном пространстве.

N = int(input("Введите размерность пространства:  "))

dot = 2
sp = []
r = 0
for i in range(dot):
    sp1=[]
    for j in range(N):
        print(f"{i + 1} точка")
        temp = float(input("Введите координату  "))
        sp1.append(temp)
    sp.append(sp1)
print(sp)

for i in range(1):
    for j in range(N):
        s = (sp[i][j] - sp[i+1][j])**2
        r =  r + s
print(r)
r = math.sqrt(r)
print(r)  
# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , сколько времени отработала программа.