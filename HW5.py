# Урок 5. Рекурсия и алгоритмы
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def involve(number, degree):
#     if degree == 1:
#         return number
#     else:
#         return number * involve(number, degree - 1)


# print("\n======== ВОЗВЕДЕНИЕ В СТЕПЕНЬ ========")
# userNumber = int(input("Введите число  ... "))
# userDegree  = int(input("Введите степень... "))

# print(f"{userNumber} в степени {userDegree} (рекурсия) = ", end="")
# print('{:,}'.format(involve(userNumber, userDegree)).replace(',', ' '))
# print(f"Проверка встроенной функцией:", end="")
# print('{:,}'.format(userNumber**userDegree).replace(',', ' ') + "\n")

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
# целых неотрицательных чисел. Из всех арифметических операций допускаются только 
# +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

# def sum (num1, num2):
#     if num2 == 0:
#         return num1
#     else:
#         return sum(num1, num2 - 1) + 1

# print("\n===== СЛОЖЕНИЕ ЦЕЛЫХ НЕОТРИЦАТАЛЬНЫХ ЧИСЕЛ (рекурсия) =====")
# number1 = int(input("Введите ПЕРВОЕ число ... "))
# number2 = int(input("Введите ВТОРОЕ число ... "))

# print(f"Сумма указанных чисел {number1} + {number2} = {sum(number1, number2)}\n")

