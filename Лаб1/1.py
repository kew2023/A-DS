from timeit import default_timer
from metods import *

line = "".join(fibonacci(500))
#Далее все задачи будут однотипно заполнять массив, а потом искать подстроки
#Наивный - хорош для поиска малых подстрок (используется в F3 в браузере/блокноте)
arr = []
t1 = default_timer()
for i in range (10,99+1):
    arr += [naive(line, str(i))]
t2 = default_timer()
print('')
print(t2-t1)
print(max(arr),arr.index(max(arr))+10)

#Рабина-Карпа - время сильно зависит от хэш-функции
arr = []
t1 = default_timer()
for i in range (10,99+1):
    arr += [RabinCarp(line, str(i))]
t2 = default_timer()
print('')
print(t2-t1)
print(max(arr),arr.index(max(arr))+10)

#Бойера-Мура - ну я вроде закодил)
arr = []
t1 = default_timer()
for i in range (10,99+1):
    arr += [BoyerMoore(line, str(i))]
t2 = default_timer()
print('')
print(t2-t1)
print(max(arr),arr.index(max(arr))+10)

#Кнута-Мориса-Прата
arr = []
t1 = default_timer()
for i in range (10,99+1):
    arr += [KMP(line, str(i))]
t2 = default_timer()
print('')
print(t2-t1)
print(max(arr),arr.index(max(arr))+10)