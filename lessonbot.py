import random
import json 
quewstions = ['На следующий праздник я хочу в подарок','У меня хорошо получаеться']
responce = [['просто внимание','билеты в Лас-Вегас','фотоссесию в вечернем платье'],['писать стихи','рисовать животных','жонглировать гирями']]

size = len(quewstions)
scoredict = {}
def save():
    with open('scoredict.json','w',encoding='utf-8') as sc:
        sc.write(json.dumps(scoredict,ensure_ascii=False))
    print('Файл сохранен')
while True:
    command = input('Введите команду: ')
    if command == '/start':
        print('Вас приветсвует бот: ')
        countusers = int(input('Введите количество игроков: '))
        users = []
        for i in range(countusers):
            temp = input(f'Введите никнейм {i+1}-го участника: ')
            users.append(temp)
    elif command == '/random':
        index = random.randrange(0,size)
        print(quewstions[index])
        answer = responce[index]
        for i in range(len(answer)):
            print(f'{i+1} - {answer[i]}')
        myanswer = input('Введите номер Вашего ответа: ')
        usersscore = []
        score = 0
        for i in range(countusers):
            temp = input(f'Введите номер ответа {users[i]} : ')
            if myanswer == temp:
                score += 1
                usersscore.append(score)
                print(f'Угадал {users[i]}')
            else:
                usersscore.append(0)

        scoredict = dict(zip(users,usersscore))
        print(scoredict)
       

    elif command == '/stop':
        save()
        break



    

    
        