#5.2[28]: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
#Примеры/Тесты:
#<function_name>(0,0) -> 0
#<function_name>(0,2) -> 2
#<function_name>(3,0) -> 3

def recursive_sum(a,b):
    return a if b==0 else recursive_sum(a+1,b-1)


result = recursive_sum(3,4)
print(result)
