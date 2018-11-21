# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color,'!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                print('Верно! \n** дракон кричит от боли **')
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if dragon.is_alive():
            break
        print(dragon._color, 'повержен!\n')
        if hero.is_alive():
            print('Поздравляем! Вы победили!')
            hero.exp_gain(dragon)
            print('Ваш накопленный опыт:', hero._experience)
            if hero.is_lvl_up() == True:
                hero.lvl_up()
                print('Поздравляем! Новый уровень, ваши характеристики возросли')
                hero.exp_down()
            
    print('К сожалению, Вы проиграли...')
    print('Хотите начать заново?')
    if input() == 'да':
        start_game()


def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами и не только!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')