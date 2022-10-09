from random import randint

# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет




try:
    daynum = int(input("Введите день недели - "))
    if daynum == 6 or daynum == 7:
        print("Выходной день")
    elif daynum > 7 or daynum == 0:
        print("Введите в диапазоне от 1 до 6")
    else:
        print("Нет")
except:
    print("Введите целое число")


# задача 2. Напишите программу для проверки 
# истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def predicate(x,y,z):
    a = not (x or y or z)
    b = not x and not y and not z
    return a == b

x = int(input("Введите x: "))
y = int(input("Введите y: "))
z = int(input("Введите z: "))

print(predicate(x,y,z))



# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

try:

    x = float(input("Введите координаты точки X - "))

    y = float(input("Введите координаты точки Y - "))

    if x > 0 and y > 0:
        print("В 1 -й четверти")
    elif x < 0 and y > 0:
        print("Во 2 -й четверти")
    elif x < 0 and y < 0:
        print("В 3 -й четверти")
    else:
        print("В 4-й четверти")
except:
    print("Введите число")


# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!

# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0

# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

try:
    num_1 = float(input("Введите первое число"))
    num_2 = float(input("Введите второе число"))
    operation = input("Введите одно из следующих операций (+, -, /, *, mod, pow, div) - ")

    if operation == "+":
        result = num_1 + num_2
        print(f"Результат операции сложения {num_1} и {num_2} равно {result}")
    elif operation == "-":
        result = num_1 - num_2
        print(f"Результат вычитания от {num_1}  {num_2} равно {result}")
    elif operation == "/":
        if num_2 != 0:
            result = num_1 / num_2
            print(f"Результат деления {num_1} на {num_2} равно {result}")
        else:
            print("Делить на ноль нельзя")
    elif operation == "*":
        result = num_1 * num_2
        print(f"Результат умножения {num_1} на {num_2} равно {result}")
    elif operation == "mod":
        result = num_1 % num_2
        print(f"Остаток от деления {num_1} на {num_2} равен {result}")
    elif operation == "pow":
        result = num_1 ** num_2
        print(f"{num_1} в степени {num_2} равен {result}")
    elif operation == "div":
        result = num_1 // num_2
        print(f"Целочисленное от деления {num_1} на {num_2} равно {result}")
    else:
        print("Неверно")

except:
    print("Введите число")



# Задача 5 VERY HARD SORT необязательная

# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# # После сортировки
# 1 2 3 4
# 5 7 9 10

raw = int(input("Введите количество строк - "))
columns = int(input("Введите количество столбцов - "))

valmin = int(input("Введите миним. значение"))
valmax = int(input("Введите макс. значение"))


def create_array2d(raw,columns,valmin,valmax):
    lst = []
    for i in range(raw):
        lst.append([0] * columns)

    for i in range(raw):
        for j in range(columns):
            lst[i][j] = randint(valmin,valmax)
    return lst

def sort_array2d(array2d):    
    for run in range(columns):
        for i in range(raw):
            for j in range(columns-1):
                if array2d[i][j] > array2d[i][j+1]:
                    temp = array2d[i][j]
                    array2d[i][j] = array2d[i][j+1]
                    array2d[i][j+1] = temp 
            
    for run in range(raw):
        for j in range(columns):
            for i in range(raw - 1):
                if array2d[i][j] > array2d[i+1][j]:
                    temp = array2d[i][j]
                    array2d[i][j] = array2d[i+1][j]
                    array2d[i+1][j] = temp 
                    
    return array2d
                    
def show_array2d(array):
    for i in range(raw):
        for j in range(columns):
            print(array[i][j], end=" ")
        print()
    return array
        


new_array = create_array2d(raw,columns,valmin,valmax)
show = show_array2d(new_array)        
print(f'Исходный массив {show}')
sort_array = sort_array2d(new_array)
print(f'Отсортированный массив {show_array2d(sort_array)}')














