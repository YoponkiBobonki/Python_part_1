# Задача 3. Квадраты нечётных чисел

n = int(input("Введите число : "))
for i in range(1, n // 2 + n%2 + 1):
    summ = i * 2 - 1
    square = summ ** 2
    print(summ, "** 2 = ", square)