# 1.1[2]. Найдите сумму цифр трехзначного числа. Используйте f-строки чтобы оформить красивый вывод
# Например для числа 145 сумма цифр будет 10: 1 + 4 + 5
# Примеры/Тесты:
# 123 >>> Сумма чисел числа 123 равна 6
# 100 >>> Сумма чисел числа 100 равна 1
# (*) Усложнение. Решите для числа произвольной разрядности: произвольное количество цифр в числе.
# (**) Усложнение. Для числа произвольной разрядности добавить в вывод строку с числами, например так:
# 13579 >>> Сумма чисел числа 13579 равна 25(1 + 3 + 5 + 7 + 9)

def calculateSumOfDigits(number):
    sum = 0
    sum_string= ""
    number_string = str(number)
    iterator = 0
    for digit in number_string: 
      sum += int(digit)
      sum_string+=("","(")[iterator==0]+str(digit)+("+",")")[iterator==len(number_string)-1]
      iterator=iterator+1
    out_string = "Сумма цифр числа %d равна %d=%s" % (number,sum,sum_string)
    print(out_string)
    return sum
        


calculateSumOfDigits(13579)