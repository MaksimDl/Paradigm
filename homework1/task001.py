# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

from random import randint
from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    # Метод сортировки списка пузырьком. Оптимизированный флагом (Если перестановок не было, цикл завершаем)
    if len(arr) == 0:
        raise ValueError(
            'На вход не должен подаваться пустой список')

    while True:
        fl = 1   # Протестировал с флагом, и без (на 100000 прокрутках). С флагом на порядок быстрее.
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                fl = 0
        if fl == 1:
            return arr

numbers = [randint(0, 200) for i in range(20)]
print(numbers)
print(bubble_sort(numbers))
