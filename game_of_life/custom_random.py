from random import random

def random_from_f(arr : list, p_arr : list) -> int | None:
    """Retrun random from a Probability density function. It returns None if sigma of p_arr not equals 1, arr = xi, p_arr = f(xi)"""
    if len(arr) == 0 or len(p_arr) == 0:
        return None
    if len(arr) != len(p_arr):
        return None
    if not p_is_one(p_arr):
        return None
    acc = acc_p(p_arr)
    umbral = random()
    for index, e in enumerate(arr):
        if umbral < acc[index]:
            return e
    return None

def p_is_one(arr : list) -> bool:
    """Returns true if the p (probability) is equal to 1 |
       Retorna true si la probbilidad es igual a 1"""
    p = 0
    for e in arr:
        p += e
    return p == 1

def acc_p(arr : list) -> list:
    """Returns an array with the probabilty acc |
       Retorna un arreglo de probailidad acumulada"""
    acc = list()
    previous = 0
    for e in arr:
        acc.append(e + previous)
        previous += e
    return acc

# nums = [1, 2, 3]
# p_nums = [0.01, 0.20, 0.79]
# for i in range(10):
#     print(random_from_f(nums, p_nums))