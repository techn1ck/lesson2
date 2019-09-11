"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

# я понимаю, что нужно использовать if-elif-else,
# но уж очень понравилось решение со словарем

def check_age(age):
    try:
        age = int(age)
        return {
            age < 0 : 'Сначала нужно родиться',
            0 <= age < 3 : 'Лучше побыть с мамой, но, если совсем никак, вам в ясли',
            3 <= age < 7 : 'Вам в детский сад',
            7 <= age < 18 : 'Вам в школу',
            18 <= age < 22 : 'Вам в ВУЗ',
            22 <= age : 'Арбайтен, майн либе :)'
        }[True]
    except ValueError:
        return 'Неверный формат данных. Введите, пожалуйста, целое число'


def main():
    age = input("Введите ваш возраст в полных годах:")
    age_type = check_age(age)
    print (age_type)


if __name__ == "__main__":
    main()
