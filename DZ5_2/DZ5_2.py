# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
game_mode = int(
    input('Выберите режим игры: 1 - С человеком, 2 - С ботом, 3 - С AI: '))
gamer1 = input('Введите имя первого игрока: ')
if game_mode == 1:
    gamer2 = input('Введите имя второго игрока: ')
if game_mode == 2:
    gamer2 = 'Bot'
if game_mode == 3:
    gamer2 = 'AI'

# порядок ходов игроков
list_gamers = [gamer1, gamer2]
list_gamers[0] = random.choice(list_gamers)
if list_gamers[0] == gamer1:
    list_gamers[1] = gamer2
else:
    list_gamers[1] = gamer1
print('Играют в Конфеты: ', gamer1, ' и ', gamer2,
      '. Первым будет ходить - ', list_gamers[0])
print('За ход можно взять не больше 28 конфет')

# игра
rest_candy = 2021
rest = 28
turn = 0
print('На столе', rest_candy, 'конфет')
while rest_candy > 0:
    print('Ход', turn + 1, '- Игрок', list_gamers[turn % 2], 'возьми конфеты:')
    if list_gamers[turn % 2] == 'Bot':
        count_candy = random.randint(1, rest)
        print(count_candy)
    elif list_gamers[turn % 2] == 'AI':
        count_candy = rest_candy % rest
        if count_candy < 1:
            count_candy = random.randint(1, rest)
        print(count_candy)
    else:
        count_candy = int(input())
        while count_candy > 29 or count_candy < 0 or count_candy > rest_candy:
            count_candy = int(
                input('Нельзя брать больше 28 конфет, попробуй еще раз: '))
    rest_candy -= count_candy
    rest = min(29, rest_candy)
    print('На столе', rest_candy, 'конфет')
    turn += 1
print('Победил игрок', list_gamers[turn % 2-1])
