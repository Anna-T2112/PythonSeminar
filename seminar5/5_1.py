#5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b.
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
#
#Примеры/Тесты:
#<function_name>(2,0) -> 1
#<function_name>(2,1) -> 2
#<function_name>(2,3) -> 8
#<function_name>(2,4) -> 16

def recursive_pow(value,pow):
    if pow>0:
        return value * recursive_pow(value,pow-1)
    elif pow==0:
        return 1
    else:
        return 1/(value*recursive_pow(value,-pow-1))


result = recursive_pow(2,-3)
print(result)
