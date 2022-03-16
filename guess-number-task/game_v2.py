"""Игра угадай число
Компьютер сам загадывает и сам угадывает число 
за минимальное количество попыток
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min = 0
    max = 101

    predict_number = np.random.randint(min+1, max) 
    
    while True:
        count += 1
         # предполагаемое число
        if number > predict_number:
            min = predict_number #устанавливаем это число как минимальное 
        
        if number < predict_number:
            max = predict_number #устанавливаем это число как максимальное 
            
        if number == predict_number:
            break  # выход из цикла если угадали
        
        predict_number = np.random.randint(min+1, max) 
        
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
