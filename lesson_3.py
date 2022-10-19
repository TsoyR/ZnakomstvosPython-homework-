import random
# Задача 1 Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



try:
    n = int(input("Введите количество элементов: "))

    created_list = []

    for i in range(n):        
        created_list.append(int(input(f"Введите {i + 1} - й элемент : ")))
    print(f'Исходный список {created_list}')
except:
    print("Введите целое число")

def sum_odd_pos(lst):
    sum = 0
    for j in range(len(lst)):
      if j % 2 != 0:
        sum = sum + lst[j]
    return sum

new_list = sum_odd_pos(created_list)
print(f'Сумма элементов на нечётных позициях равна {new_list}')

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
try:

    n = int(input("Введите количество элементов: "))  
    created_list = []
    for i in range(n):
        created_list.append(int(input(f"Введите {i + 1} элемент: ")))
    print(f'Исходный список{created_list}')
except:
    print("Введите целое число")

def pair_of_num(lst):
  num = []
  size = len(lst)
  circle = int(size / 2)
  if size % 2 == 0:
    for i in range(circle):
        num.append(lst[i] * lst[size - 1 - i])
    return num
  else:
    for i in range(circle):
        num.append(lst[i] * lst[size - 1 - i])
  num.append(lst[circle]**2)
  return num
  
new_list = pair_of_num(created_list)
print(f'Список произведения пар чисел {new_list}')

# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

try:
    n = int(input("Введите количество вещественных чисел: "))  
    created_list = []
    for i in range(n):
        created_list.append(float(input(f"Введите {i + 1} элемент: ")))
    print(f'Исходный список{created_list}')
except:
    print("Введите вещественное число")

def fractional_part(lst):
    fract_list = []
    int_part = 0
    size = len(lst)
    for i in range(size):
        int_part = int(lst[i])
        fract_part = lst[i] - int_part
        fract_part = round(fract_part,10)
        if fract_part != 0:
            fract_list.append(fract_part)
    try:    
        max = fract_list[0]
        min = fract_list[0]
        for j in range(len(fract_list)):
            if fract_list[j] > max:
                max = fract_list[j]
            elif fract_list[j] < min:
                min = fract_list[j]
        return (max - min)
    except:
        print('Дробные части равны нулю')

new_list = fractional_part(created_list)
print(f'Разница между максимальным и минимальным значением дробной части равна  {new_list}')

# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите десятичное число'))

def binary_num(n):
    quotient = n
    remind = 0
    binary_digit = ''
    while quotient != 0:
        remind = quotient % 2
        quotient = quotient // 2
        binary_digit = binary_digit + str(remind)
    return binary_digit[::-1]

numbers = binary_num(num)
print(numbers)

# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , 
# причем чтоб количество элементов было четное. Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно переместился на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.
try:
    m = int(input('Введите количество строк'))
    n = int(input('Введите количество столбцов'))
    if (m * n) % 2 != 0:
        print("Введите четное количество элементов")
        
    minval = int(input('Введите минимальное значение'))
    maxval = int(input('Введите максимальное значение'))
except:
    print("Введите целые числа")

sp = []
for i in range(m):
    sp1=[]
    for j in range(n):
        sp1.append(random.randint(minval,maxval))
    sp.append(sp1)


iteration = (m * n)/ 2

def random_sort(array):
    count = 0
    for k in range(m):
        for l in range(n):
            random_raw = random.randint(0,m-1)
            random_col = random.randint(0,n-1)
            temp = sp[random_raw][random_col]
            array[random_raw][random_col] = array[m-1-k][n-1-l]
            array[m-1-k][n-1-l] = temp
            count += 1
            if count == iteration:
                return array



def show_array(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            print(array[i][j], end = " " )
        print()
    return "* "*n
    
        

print(show_array(sp))            
sp_new = random_sort(sp)
print(show_array(sp_new))