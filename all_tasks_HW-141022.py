# №1 Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list_mult = [2, 3, 5, 9, 3]
sum = 0
for i in range(len(list_mult)):
    if i % 2 != 0:
        sum += list_mult[i]

print('Список:', list_mult)
print('Сумма элементов на нечетных нечетных позициях =', sum)



# №2 Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]
new_list = []
count = len(list)
for i in range(len(list)):
    while i < len(list)/2 and count > len(list)/2:
        count -= 1
        new_list.append(list[i] * list[count])
        i += 1
print(new_list)



# №3 Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
new_list = []
for i in range(len(list)):
    new_list.append(list[i] % 1)
min_el = 1
max_el = 0

for i in new_list:
    if i < min_el and i != 0:
        min_el = i

for i in new_list:
    if i > max_el:
        max_el = i

print(int((max_el - min_el) * 100) / 100)

# 2й вариант с использованием готовых функий max и min:

print(int((max(new_list) - min(new_list)) * 100) / 100)



# № 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input('Введите число: '))
res =''
while n != 0:
    res = str(n % 2) + str(res)
    n //= 2
print(res)



# №5 Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
# Пример:
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n - 2)

def nego_fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        x1 = 1
        x2 = -1
        for i in range (2, n):
            x1, x2 = x2, x1 - x2
        return x2

list = []
for el in range(1, n+1):
    list.append(fib(el))
    list.insert(0, nego_fib(el))

print(list)

