# Задача 1. Создайте программу для игры в "Крестики-нолики".
# import random 
# import re

# array = [['*']*3 for i in range(3)]
# print(array)

# def print_array(array):
#     for i in range(len(array)):
#         for j in range(len(array[i])):
#             print(array[i][j], end='  ')
#         print()



# def check_win(sign):
#     for row in array:
#         if row.count(sign) == 3:
#             return sign
#     for col in range(3):
#         if array[0][col] == sign and array[1][col] == sign and array[2][col] == sign:
#             return sign
#     if array[0][0] == sign and array[1][1] == sign and array[2][2] == sign:
#         return sign
#     if array[0][2] == sign and array[1][1] == sign and array[2][0] == sign:
#       return sign
        
#     else:
#          False


# def take_input(sign):
#     while True:
#         print(f'Куда поставить {sign} ?')
#         row = int(input('Введите строку: '))
#         col = int(input('Введите столбец: '))
#         if row > 3 and col > 3:
#             print('Ошибка ввода. Повторите! ')
#             continue
#         if (array[row-1][col-1] in 'xo'):
#             print('Эта ячейка уже занята. Повторите ввод ')
#             continue
#         array[row-1][col-1] = sign
#         break

# def take_input_bot(sign):
#     while True:
#         row = random.randint(1,3)
#         col = random.randint(1,3)
#         if (array[row-1][col-1] in 'xo'):
#             continue
#         array[row-1][col-1] = sign
#         print(f'Бот ставит  {sign} в ячейку {row},{col}')
#         break     

    
   

# choice = int(input('Введите 1 - орел или решку - 2: '))
# count = random.randint(1,2)
# while True:
#     print_array(array)
#     if count % 2 != 0:
#         print(f'Ваш ход')
#         sign = 'x'
#         take_input(sign)
#     else:
#         print('Ходит бот')
#         sign = 'o'
#         take_input_bot(sign)
#     if count > 4:
#         winner = check_win(sign)
#         if winner:
#             print_array(array)
#             print(winner,'выиграл')
#             break
#     count += 1
#     if count > 9:
#         print_array()
#         print('Ничья')
#         break

# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:* 
# 2+2 => 4; 
# 1+2*3 => 7; 
# 1-2*3 => -5;
# - Добавьте возможность использования скобок, меняющих приоритет операций.
#     *Пример:* 
#     1+2*3 => 7; 
#     (1+2)*3 => 9;

# expression = input('Введите арифметическое выражение: ')
# expression = expression.replace(" ","")

# def rpn(expression):
#     lex=parse(expression)
#     s2=[]
#     r=[]
#     oper=["+","-","*","/","(",")"]
#     for a in lex:
#         if a=="(":
#             s2=[a]+s2
#         elif a in oper:
#             if s2==[]:
#                 s2=[a]
#             elif a==")":
#                 while(True):
#                     q=s2[0]
#                     s2=s2[1:]
#                     if q=="(":
#                         break
#                     r+=[q]
#             elif prty(s2[0]) < prty(a):
#                 s2=[a]+s2
#             else:
#                 while(True):
#                     if s2==[]:
#                         break
#                     q=s2[0]
#                     r+=[q]
#                     s2=s2[1:]
#                     if prty(q)==prty(a):
#                         break
#                 s2=[a]+s2
#         else:
#             r+=[a]
#     while(s2 != []):
#         q=s2[0]
#         r+=[q]
#         s2=s2[1:]
    
#     return r
 
# def prty(o):
#     if o=="+" or o=="-":
#         return 1
#     elif o=="*" or o=="/":
#         return 2
#     elif o=="(":
#         return 0
 
# def parse(s):
#     delims=["+","-","*","/","(",")"]
#     lex=[]
#     tmp=""
#     for a in s:
#         if a != " ":
#             if a in delims:
#                 if tmp != "":
#                     lex+=[tmp]
#                 lex+=[a]
#                 tmp=""
#             else:
#                 tmp+=a
#     if tmp != "":
#         lex+=[tmp]
#     return lex

# expr = rpn(expression)


# expr2 = []
# for i in expr:
#     if i.isdigit():
#         expr2.append(int(i))
#     else:
#         expr2.append(i)

      
# def evaluate(expr2):
#     stack = []
#     for el in expr2:
#         if el == '+':
#             stack.append(stack.pop() + stack.pop())
#         elif el == '-':
#             to = stack.pop()
#             from_ = stack.pop()
#             stack.append(from_ - to)
#         elif el == '/':
#             to = stack.pop()
#             from_ = stack.pop()
#             stack.append(from_ / to)
#         elif el == '*':
#             to = stack.pop()
#             from_ = stack.pop()
#             stack.append(from_ * to)
#         else:
#             stack.append(el)
        
#     return stack.pop()

# result = evaluate(expr2)
# print(f'Ответ: {result}')


# Задача FOOTBALL необязательная: Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.

# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

# Формат ввода следующий:
# В первой строке указано целое число nn — количество завершенных игр.
# После этого идет nn строк, в которых записаны результаты игры в следующем формате:
# Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

# Вывод программы необходимо оформить следующим образом:
# Команда:Всегоигр Побед Ничьих Поражений Всегоочков

# Конкретный пример ввода-вывода приведён ниже.

# Порядок вывода команд произвольный.

# Sample Input:

# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:

# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6


n = int(input('Введите количество завершенных игр: '))

teams = {}


def res_first(s):
    first = [1, int(int(s[1]) > int(s[3])),
    int(int(s[1]) == int(s[3])), int(int(s[1]) < int(s[3])),
    int(int(s[1]) > int(s[3])) * 3]
    return first
def res_second(s):       
    second = [1, int(int(s[1]) < int(s[3])),
    int(int(s[1]) == int(s[3])), int(int(s[1]) > int(s[3])),
    int(int(s[1]) < int(s[3])) * 3]
    return second



for i in range(n):
    s = input('Введите название команды и количество голов через ";": ').split(';')
    first = res_first(s)
    second = res_second(s)

    if s[0] in teams:
        teams[s[0]] = map(sum, zip(teams[s[0]], first))
    else:
        teams[s[0]] = first
 
    if s[2] in teams:
        teams[s[2]] = map(sum, zip(teams[s[2]], second))
    else:
        teams[s[2]] = second
 
for t, v in teams.items():
    print(f'{t}:', *v)





    














