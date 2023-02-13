#2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
#  а Катя должна их отгадать.
#Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
#Помогите Кате отгадать задуманные Петей числа.
#Примеры/Тесты:
#4 4 -> 2 2
#5 6 -> 2 3

from math import sqrt

def calculateNumbers(b,c):
    D = b*b + 4*c
    if D > 0:  
        sq = sqrt(D)/2
        p = b/2
        x1 = p-sq
        x2 = p+sq
        return [x1, x2]
    else:
        return[b/2]

print("Введите сумму: ")
b = int(input())

print("Введите произведение: ")
c = int(input())

result = calculateNumbers(b,-c)
if len(result)==2:
    print("Число x=%d, число y=%d" % (result[0],result[1]))
else:
    print("Число x=%d, число y=%d" % (result[0],result[0]))
