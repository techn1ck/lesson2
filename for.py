"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
from random import randint


"""
Промежуточное задание 1
- создать список из 10 целых чисел
- вывести на экран каждое число, увеличенное на 1

Сначала сделал влоб
    numbers = list()
    for i in range(10):
        numbers.append(randint(0,50))
Потом подсмотрел более изящное решение
"""
def first_task():
    numbers = [randint(0,50) for _ in range(10)]

    print(numbers)
    
    for number in numbers:
        print(number + 1)
        

"""
Промежуточное задание 2
- ввести с клавиатуры строку
- Вывести эту же строку вертикально: по одному символу на строку консоли.

"""
def second_task():
    string = input("Введите строку: ")
    for letter in string:
        print(letter)


"""
Основное задание 

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
def get_school_data(classes):
    data = list()
    for school_class in classes:
        data.append({
            'school_class' : school_class,
            'scores' : [randint(2,5) for _ in range(10)]
            })
    return data


def main():
    # список классов в школе задаю вручную
    # при необходимости можно заполнить рандомно или запросить у пользователя
    classes = ['1а', '1б', '2а', '2б', '3а'] 
    
    # заполняю список оценок для учеников
    data = get_school_data(classes)
 #   print(data)

    # считаю средний балл по школе и по каждому классу
    score_sum = 0
    avg_score = dict() # в этот словарь записываю средний балл по каждому классу
    for school_class in data:
        avg_score[ school_class['school_class'] ] = sum( school_class['scores'] ) / len( school_class['scores'] )
        score_sum += avg_score[ school_class['school_class'] ]
    
    avg_school_score = score_sum / len(avg_score)
    print(f"Средний балл по школе - {avg_school_score:.1f}")

    for school_class in avg_score:
        print(f"- средний балл класса {school_class} - {avg_score[school_class]:.1f}")
    
    
    
    
if __name__ == "__main__":
    main()
 #   first_task()
 #   second_task()
    
