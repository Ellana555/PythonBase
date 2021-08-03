import numpy as np

# загадали число
number =  np.random.randint(1, 101)
print("Загаданное число =",number)

def game_core_v1(number):
    ''' Задача решалась методом пополам
     Сначала установили число 50 (середину диапазона),
     а после последовательно уменьшали или увеличивали число значение,
     в зависимости от того, больше оно или меньше нужного.
     Функция возвращает угаданное число в среднем за 6 попыток'''
    count = 1 # 1 попытка в случае совпадения предполагаемого числа с загаданным
    predict = 50
    # диапазон от 51 до 100
    if number > predict:
        predict += 25
        print(predict)
        count += 1
        if number > predict:
            predict += 12
            print(predict)
            count += 1
            if number > predict:
                predict += 7
                print(predict)
                count += 1
            else:
                predict -= 6
                print(predict)
                count += 1

        elif number < predict:
            predict -= 12
            print(predict)
            count += 1
            if number > predict:
                predict += 7
                print(predict)
                count += 1
            else:
                predict -= 6
                print(predict)
                count += 1

    # диапазон от 1 до 49
    else:
        predict -= 25
        print(predict)
        count += 1
        if number > predict:
            predict += 12
            print(predict)
            count += 1
            if number > predict:
                predict += 7
                print(predict)
                count += 1
            else:
                predict -= 6
                print(predict)
                count += 1
        elif number < predict:
            predict -= 12
            if number > predict:
                predict += 7
                print(predict)
                count += 1
            else:
                predict -= 6
                print(predict)
                count += 1
    # Циклы с предусловием для оставшихся значений
    while number != predict:
        count+=1
        print("Попытка = ",count - 1, "Предполагаемое число = ", predict, )
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
        print(number)
    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за {score} попыток")
    return (score)

# запуск для проверки рабочей функции 
game_core_v1(number) 
# запуск проверки на скорость второй функции
score_game(game_core_v1)