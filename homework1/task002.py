# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
# Пример процедуры для сортировки списка чисел в порядке убывания, используя алгоритм сортировки выбором:

from random import randint
from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        raise ValueError(
            'На вход не должен подаваться пустой список')
    return sorted(arr, reverse=True)


numbers = [randint(0, 200) for i in range(20)]
print(numbers)
print(bubble_sort(numbers))
