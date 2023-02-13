#3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число 
# не обязательно содержится в списке.
#Примеры/Тесты:
#Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
#Output: 2
#Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

import math

def findNearest(x,input):
    min=1000
    result=0
    for elem in input:
        next_min = abs(x-elem)
        if next_min<min:
            min = next_min
            result = elem

    return result

inputList = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
print(',',input)
print("Введите число: ")
n = int(input())
result = findNearest(n,inputList)
print("Самый близкий элемент: %d" % result)
