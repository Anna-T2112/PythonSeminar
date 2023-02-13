#2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k),
# не превосходящие числа N.
#Примеры/Тесты:
#10 ->
#1
#2
#4
#8

import math
def pow2(number):
    index = 0
    pow2 = 0 
    result = []
    while pow2<number:
        pow2 = pow(2,index)
        if (pow2<number):
            result.append(pow2)
        index+=1
    return result

print("Введите число: ")
n = int(input())
result = pow2(n)
print(','.join(str(e) for e in result))