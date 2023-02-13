# 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних 
#трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая
# проверяет счастливость билета.
#Примеры/Тесты:
#385916 >>> yes
#123456 >>> no


def calculateLuckyNumber(number):
    string_number = str(number)
    iterator = 0
    left_side = 0
    right_side = 0
    for digit in string_number:
        if (iterator<=2):
            left_side+=int(digit)
        else:
            right_side+=int(digit)
        iterator+=1
    return left_side==right_side

result = calculateLuckyNumber(123456)
print(("no","yes")[result])