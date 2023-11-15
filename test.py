# number = int(input())
# number = abs(number)
# a = number // 100
# b = number % 100 // 10
# c = number % 10
# print(a + b + c)
'''n = input()
input(int(n[0]) + int(n[1]) + int(n[2]) == int(n[3]) + int(n[4]) + int(n[5]))'''
# n = int(input())
# m = int(input())
# k = int(input())
# if k < n * m and (k % m == 0 or k % n == 0):
#     print('yes')
# else:
#     print('no')
'''n = int(input())
n = abs(n)
a = 1
c = 1
while a <= n:
    c = c * a
    a += 1
print(c)
'''
# number = int(input())
# first_el, second_el = 0, 1
# next_el = first_el + second_el
# count = 3
# while next_el < number:
#     first_el, second_el = second_el, next_el
#     next_el = first_el + second_el
#     count += 1
# if next_el == number:
#     print(count)
# else:
#     print(-1)

# n = int(input())
# max_count = 0
# count = 0
# for _ in range(n):
#     temp = int(input())
#     if temp > 0:
#         count += 1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
# if max_count == 0 and count != 0:
#     print(count)
# else:
#     print(max_count)
'''list_1 = []
n = int(input('write size list - '))
for _ in range(n):
    list_1.append(int(input('write numbers - ')))
print(len(set(list_1)))
k = int(input('write K - '))
list_2 = []
for i in range(1, k + 1):
    list_2.append(list_1[- i])
for i in range(len(list_1) - k):
    list_2.append(list_1[i])
print(list_2)'''
# text_list = list(input('write - '))
# my_dict = {}
# new_list = []
# for letter in text_list:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
#     if my_dict[letter] > 1:
#         new_list.append(letter + '_' + str(my_dict[letter]))
#     else:
#         new_list.append(letter)
#
# print(' '.join(new_list))
'''text = input('write: ')
text_list = text.split()
print(len(set(text_list)))'''
# my_list = list(input("write: "))
# print(*[letter for letter in my_list if my_list.count(letter) == 1])
'''import random

stack_size = int(input('Введите количество монет = '))
coins = [random.randint(0, 1) for _ in range(stack_size)]
print(coins)

if coins.count(1) < coins.count(0):
    print(f'перевернуть единички, количество переводов = {coins.count(1)}')
elif coins.count(1) == coins.count(0):
    print("переворачивай что хочешь;)")
else:
    print(f'перевернуть нулики, количетство переводов = {coins.count(0)}')
'''

# RLE алгоритм реализовать


'''def fibonacci(num):
    if num in (1, 2):
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


n = int(input("write - "))
for i in range(1, n + 1):
    print(f"{fibonacci(i)} - {i}")'''

# import random
# n = int(input('write: '))
# my_list = [random.randint(2, 5) for _ in range(n)]
# print(*my_list)
# min_num = 5
# max_num = 2
# for i in range(n):
#     if my_list[i] > max_num:
#         max_num = my_list[i]
#     elif my_list[i] < min_num:
#         min_num = my_list[i]
# for i in range(n):
#     if my_list[i] == max_num:
#         my_list[i] = min_num
#     elif my_list[i] == min_num:
#         my_list[i] = max_num
# print(*my_list)
'''def search_numbers(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return "no"
    return "yes"


num = int(input("write - "))
print(search_numbers(num))
'''
'''N = int(input('write N - '))
list_1 = [int(input("write numbers - ")) for _ in range(N)]
print(list_1)
M = int(input('write M - '))
list_2 = [int(input("write numbers - ")) for _ in range(M)]
print(list_2)


def chek_num(list_n, list_m):
    set_3 = set(list_n).difference(set(list_m))
    return list(set_3)


print('difference')
print(chek_num(list_1, list_2))'''

# N = int(input("write N - "))
# list_random = [int(input('write numbers for list - ')) for _ in range(N)]
# print(list_random)
#
#
# def triangle(list_any):
#     list_over = []
#     for i in range(1, len(list_any) - 1):
#         if list_any[i] > list_any[i - 1] and list_any[i] > list_any[i + 1]:
#             list_over.append(list_any[i])
#     return list_over
#
#
# print(*triangle(list_random))

'''N = int(input("write N - "))
list_random = [int(input('write numbers for list - ')) for _ in range(N)]
print(list_random)
count_dub_num = 0
for letter in list_random:
    if list_random.count(letter) > 1:
        count_dub_num += 1

print(count_dub_num // 2)'''

# some_list = []
# while True:
#     number = int(input())
#     if number == 0:
#         break
#     some_list.append(number)
#
# count_dict = {}  # 2: 2, 3: 3, 4: 1, 5: 1
#
# for el in some_list:
#     if count_dict.get(el):
#         count_dict[el] += 1
#     else:
#         count_dict[el] = 1
#
# count = 0
# for value in count_dict.values():
#     count += value // 2
# print(count)

'''def sum_dif(number):
    summma = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            summma += i
    return summma


sum_dict = {}
k = int(input('write - '))
for number in range(1, k + 1):
    if number in sum_dict:
        if sum_dif(number) == sum_dict[number]:
            print(sum_dict[number], number)
    sum_dict[sum_dif(number)] = number'''

# map use
'''example'''
# some_list = [1, 2, 3, 4, 5]
#
# def square(x):
#     return x ** 2
#
# new_list = list(map(square, some_list))
# print(new_list)
'''map - реализвывает цикл(ко всем итерируемым объектам применяет какую-либо функцию)'''

'''filter - основан на лигике bool(фильтрует)'''
'''example'''
# some_list = [1, 2, 3, 4, 5, 6]
#
#
# def even(x):
#     return x % 2 == 0
#
#
# new_list = list(filter(even, some_list))
# print(new_list)

'''lambda - анонимная функция в одну строчку, применяемая 1 раз'''
'''example'''
some_list = [1, 2, 3, 4, 5, 6]

# new_list = list(map(lambda x: x + 1, some_list))
# print(new_list)
# new_list = list(filter(lambda x: type(x) == int, some_list))
# print(new_list)


'''enumerate - "создает из списка, список, сотсоящих из кортежей, в которых находится индекс объекта и сам объект"'''
'''example'''
# some_list = [10, 20, 30, 40]
# some_dict = {}
# print(list(enumerate(some_list)))
# for ind, value in enumerate(some_list):
#     some_dict[ind] = value
#
# print(some_dict)
# for ind in range(0, len(some_list)):
#     print(ind, some_list[ind])

'''zip - "сшивать", объединяет несколько списков в один список из кортежей, соответсвующий количеству списков'''
'''example'''
# first_list = ['apple', 'orange', 'grape']
# second_list = ['яблоко', 'апельсин', 'виноград']
# print(list(zip(first_list, second_list)))
# for eng, ru in zip(first_list, second_list):
#     print(eng, ru)

'''values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(list(map(lambda x: x, values)))
'''
# import math
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# list_1 = list(filter(lambda x: x[0] != x[1], orbits))
# max_orbit = max(map(lambda x: x[0] * x[1] * math.pi, list_1))
# print(list(filter(lambda a: a[0] * a[1] * math.pi == max_orbit, list_1)))
"""Дан массив с числами, и целевое значение. Нужно проверить найдутся ли в массиве два числа,
чья сумма равна целевому значению?"""
# import time
# import random
#
# start = time.perf_counter()
#
# summa = random.randint(15, 20)
# print(summa)
# some_list = [random.randint(3, 15) for _ in range(1000)]
# print(some_list)
#
# new_list = list(filter(lambda a: a < summa, some_list))
# print(new_list)
#
# new_list = set(new_list)
#
# for el in new_list:
#     if summa - el in new_list:
#         print(el, summa - el)
#         break
# else:
#     print('no')
#
# end = time.perf_counter()
#
# print(end - start)
'''import random

some_list = [random.randint(0, 10) for _ in range(10)]


def some_by(characteristics, object):
    if len(object) == 0:
        return True
    for i in range(1, len(object)):
        if characteristics(object[i]) != characteristics(object[0]):
            return False
    return True


if some_by(lambda a: type(a) == int, some_list):
    print('yes')
else:
    print('no')
'''
'''Напишите программу, 
которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.'''

# def get_exp(number_1, number_2):
#     if number_2 == 0:
#         return 1
#     else:
#         poww = number_1 * get_exp(number_1, number_2 - 1)
#         return poww
#
#
# print(get_exp(2, 3))


# with open('work with file.txt', 'r', encoding='utf-8') as file:
# text = file.read().splitlines()
# print(text)

# while True:
#     line = file.readline()
#     if not line:
#         break
#     print(line)

# with open('filetest.txt', 'a', encoding='utf-8') as file:
#     some_list = ['привет', 'пока']
#     for word in some_list:
#         file.write(word + '\n')

# with open('some_file.txt', 'w', encoding='utf-8') as file:
#     some_list = [input('write - ') for _ in range(5)]
#     for word in some_list:
#         file.write(word)
#
# with open('some_file.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(text.count(input('write_find - ')))


# from random import randint
#
# n = int(input('Введите кол-во элементов в списке: '))
# some_list = [randint(-n, n) for _ in range(n)]
# print(some_list)
# with open('some_file.txt', 'w', encoding='utf-8') as file:
#     for _ in range(randint(1, n)):
#         file.write(str(randint(0, n - 1)) + '\n')
#
# with open('some_file.txt', 'r', encoding='utf-8') as file:
#     mult = 1
#     for ind in file.read().splitlines():
#         mult *= some_list[int(ind)]
# print(mult)
