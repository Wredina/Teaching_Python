from create_date import *
from time import sleep


def add_person():
    name = info_user_write()
    take_info = open(
        'D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'a', encoding='utf-8')
    take_info.writelines(name)
    take_info.close()


def print_data():
    with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'r', encoding='utf-8') as take_info:
        print(take_info.read())
        sleep(5)


def search_user_info():
    search = input('что ищем? ')
    with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'r', encoding='utf-8') as take_info:
        print(*list(filter(lambda x: search in x, take_info)))
        sleep(5)


def dell_user():
    dell = input('кого удаляем? ')
    with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'r', encoding='utf-8') as take_info:
        text_data = take_info.readlines()
        with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'w', encoding='utf-8') as take_info:
            for line in text_data:
                if dell not in line:
                    take_info.writelines(line)
            print('контакт удалён')
            sleep(5)


def change_user():
    what_change = input('''что хоти изменить:
1 - фамилию
2 - имя
3 - отчество
4 - телефон
введите номер: ''')
    user = input('кого меняем? ')
    new_iformation = input('на что меняем? ')
    with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'r+', encoding='utf-8') as take_info:
        text_data = take_info.readlines()
        with open('D:\программирование\Обучение_тестировщик\Less_1\знакомство_с_Python\\task_49\\tel.txt', 'w', encoding='utf-8') as take_info:
            for line in text_data:
                if user in line:
                    #     new_info = line.replace(user, new_iformation)
                    #     take_info.writelines(new_info)
                    # else:
                    #     take_info.writelines(line)
                    line = list(line.split())
                    if what_change == '1':
                        line.pop(0)
                        line.insert(0, new_iformation)
                        line = ' '.join(line)
                        take_info.writelines(line + '\n')
                    elif what_change == '2':
                        line.pop(1)
                        line.insert(1, new_iformation)
                        line = ' '.join(line)
                        take_info.writelines(line + '\n')
                    elif what_change == '3':
                        line.pop(2)
                        line.insert(2, new_iformation)
                        line = ' '.join(line)
                        take_info.writelines(line + '\n')
                    elif what_change == '4':
                        line.pop(3)
                        line.insert(3, new_iformation)
                        line = ' '.join(line)
                        take_info.writelines(line + '\n')
                    else:
                        print('ввели не коректные данные')
                        sleep(5)
                else:
                    take_info.writelines(line)
