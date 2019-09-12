"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""
answers = {
    "как дела?" : "Хорошо",
    "что делаешь?" : "Работаю",
    "мы уже приехали?" : "Нет",
}


def ask_user_dict():
    question = str()
    while True:
        question = input('Ваш вопрос? ')
        if question.lower() != 'пока':
            print(answers.get(question.lower(), 'Не знаю'))
        else:
            break


def ask_user():
    print('Задайте свой вопрос программе, чтобы получить ответ.\nДля выхода из программы напишите "Пока"\n')

    try:
        ask_user_dict()
    except KeyboardInterrupt:
        print('\nПока!')


if __name__ == "__main__":
    ask_user()
