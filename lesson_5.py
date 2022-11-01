# задача 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Делаем игру против бота


import random
import re





def takecandy(candy):
        take = int(input('Заберите конфеты не более 28 и не меньше 1: '))
        while take > 28:
            take = int(input('Заберите конфеты не более 28 и не меньше 1: '))
        if take <= candy:
            candy = candy - take    
            print('Осталось', end=' ')
            return candy
        elif take > candy:
            print('Вы не можете взять столько кофет')
            take = int(input('Заберите конфеты не более 28 и не меньше 1: '))
        elif candy == 0:
            print('Вы победили!')
   

def invert(index):
    if index == 1:
        index = 0
    else:
        index = 1    
    return index

def takebot(candy):
    remind = candy
    take = 28
    while remind != 0:
        temp = candy - take
        remind = temp % 29
        if remind > 0:
            take -= 1
        elif temp == 0:
            print('Бот победил!')
        else:
            break
        
    print(f'Бот забирает {take}')
    print(f'Ocтаток', end = ' ')
    return temp

while True:
    command = input('Введите команду: ')
    if command == '/start':
        print('Вас приветствует бот! Выберите вариант : /1 - Игра двух игроков, /2 - Игра с ботом')
    if command == '/1':
        users = []
        candy = 2021    
        for i in range(2):
            users.append(input(f'Введите имя {i+1} - го игрока: '))
        print('Идет жеребьевка ......')
        index = random.randint(0,1)
        print(f'{users[index]} делайте ход')
        candy = takecandy(candy)
        print(candy)
        while candy > 0:
            index = invert(index)
            if index == 1:
                print(f'Ваш ход {users[index]}')
                candy = takecandy(candy)
                print(candy)
            else:
                print(f'Ваш ход {users[index]}')
                candy = takecandy(candy)
                print(candy)
            
    elif command == '/stop':
        break
    elif command == '/2':
        candy = 2021
        users = ['bot']
        name = input('Введите ваше имя: ')
        users.append(name)
        index = random.randint(0,1)
        if users[index] == 'bot':
            take = 20
            print(f'Бот взял {take} конфет') 
            candy = candy - take
            print(f'Осталось {candy} конфет')
        else:
            take = int(input('Заберите конфеты не более 28: '))
            while take > 28:
                take = int(input('Заберите конфеты не более 28: '))      
            candy = candy - take
            print(f'Осталось {candy} конфет')

        while candy > 0:
            index = invert(index)
            if index == 1:
                print(f'Ваш ход {users[index]}')
                candy = takecandy(candy)
                print(candy)
            else:
                print(f'Ходит {users[index]}')
                candy = takebot(candy)
                print(candy)        


задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
Функции FIND и COUNT юзать нельзя.

stroka = input('Input string: ')

for i in range(len(stroka)):
  if stroka[i:i+3] =='абв':
    stroka = stroka.replace(stroka[i:i+3],'')
print(stroka)


задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.

my_file = open("data.txt", "w")
my_file.write("Привет, файл!")
my_file.close()

with open("data.txt") as data:
    a = data.read()
    print(a)



def rle_encode(data):
    encoding = ''
    prev_el = ''
    count = 1
    
    for elem in data:  
        if elem != prev_el:
            if prev_el:
                encoding += str(count) + prev_el
            count = 1
            prev_el = elem
        else:
            count += 1
    else:
        encoding += str(count) + prev_el
        return encoding 

encoding = rle_encode(a)
print(encoding)


def rle_decode(data):
    decode = ''
    count = ''
    for el in data:
        if el.isdigit():
            count += el
        else:
            decode += el * int(count)
            count = ''
    return decode

decode = rle_decode(encoding)
print(decode)

# задача 4 необязательная Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , 
# Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9

a = '5*x^3 + 2*x^2 + 6'
b = '7*x^2 + 6*x + 3'



# 5;3 2;2 7;2 6;1

# lst = re.sub(r'[*]','=',c)
# print(lst)

lst1 = a.split(' + ')
print(lst1)

lst2 = b.split(' + ')
print(lst2)

sp1 = []
for i in lst1:
    sp1.append(i.split('*'))
print(sp1)

sp2 = []
for i in lst2:
    sp2.append(i.split('*'))
print(sp2)


res = sp1 + sp2
print(res)

for i in res:
    i[0] = int(i[0])
print(res)


      


  
  


















    





























# matcha = re.findall(r'[\d][\S]x[\S][\d]',a)
# matchb = re.findall(r'[\d][\S]x[\S][\d]',b)
# print(matcha)
# print(matchb)





