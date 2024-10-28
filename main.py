#
# Простые числа
# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# a = int(input("Введите число: "))
# is_prime(a)
#
#
# Задача 1. Степень нечётного числа
# Выведите третью степень каждого нечётного
# числа в диапазоне от единицы до указанного пользователем числа
# включительно. Для этого используйте шаг внутри функции range.
#
# n = int(input("Введите число: "))
# for i in range (1, n + 1, 2):
#     print(i, "** 3 = ", i ** 3)
#
# n = int(input("Введите число: "))
# summ = 0
# for i in range (1, n + 1, 5):
#    print("Номер стула: ", i)
#    summ += i
# print("Сумма: ", summ)
#
# wake_up = int(input("Во сколько проснулся ? "))
# water = 0
# total_calories = 0
# for hour in range (wake_up, 23, 3):
#   water += 1
#    calories = int(input("Сколько калорий съел? "))
#    total_calories += calories
# print("Выпил литров воды: ", water)
# print("Калорий съел: ", total_calories)
#
#
# Задача 1. Прятки
# n = int(input("Введите количество секунд: "))
# for i in range (n, 0, -1):
#     print(i)
# print("Я иду искать! ")
#
# Задача 2. Армия
# soldiers = int(input("Сколько солдат в шеренге? " ))
# rules = int(input("Сколько правил в уставе? "))
# total_pushups = 0
# for i in range (soldiers - 4, 0, -4):
#     print("Номер солдата: ", i)
#     rul = int(input("Сколько правил в уставе? "))
#     if rul != rules:
#         print("Неверно! Упал и отжался ", i * 10)
#         total_pushups += i * 10
# print("Сумма отжиманий", total_pushups)
#
# Задача 3. Прятки 2
#
# n = int(input("Введите количество секунд: "))
# for i in range (n, 0, -2):
#     print(i)
# print("Я иду искать")
#
# Задача 1. Урок литературы
# qwe = 0
# for i in range (5):
#     question = input("Кто написал произведения Евгеиня Онегина? ")
#     if question == "Пушкин":
#         print("Молодец")
#         break
#     else:
#         print("Садись два")
#         qwe += 1
# print("Количество двоек = ", qwe)
#
# Задача 2. Начальник
#
# question = input("Выполнил задание?")
# while question != "да" and question != "Да":
#     question = input("Выполнил задание?")
# print("Молодец")
#
#
#
# text = input("Введите текст: ")
# first_letter = 0
# second_letter = 0
# for i in text:
#     if i == "Ы":
#         first_letter += 1
#     if i == "ы":
#         second_letter += 1
#
#
#
# print("Больших букв Ы: ", first_letter)
# print("Маленьки букв ы: ", second_letter)
#
#
# Задача 1. Доска
# print("_________")
# print("|000000|\n" * 4, end = "" )
# print("_________" )
# Задача 2. Локальная сеть
# number = int(input("Введите число: "))
# step = int(input("Введите шаг: "))
# summ = 0
# for i in range(3):
#     summ += number
#     number += step
#     print(number, end = ".")
# print(summ)
# Задача 3. Табло
# number = int(input("Введите число: "))
# for i in range (number + 1):
#     if i % 10 == 0:
#         print("-=-", i, end = " " )
# print("-=-")
#
#
# Задача 1. Таблица умножения
#
# for row in range (1, 10):
#     for col in range (1, 10):
#
#         print(row * col, end = "\t",)
#     print()
# Задача 2. Таблица суммы
# number = int(input("Введите число: "))
# for row in range(number + 1):
#     for col in range(number + 1):
#         print(row + col, end = "\t")
#     print()
# Задача 3. Анализ данных
#
# for row in range(0, 10):
#     for col in range(0, 10):
#         print(row - col, end= "\t")
#     print()
#
#
# num = int(input("Введите число: "))
# for row in range(1, num + 1):
#     for col in range(1, num + 1):
#         if row % 2 == 0:
#             print(row, end="\t")
#         else:print(col, end="\t")
#     print()
# Задача 2. Чёрный ящик
# num = int(input("Введите размер матриццы: "))
# for row in range(1, num + 1):
#     for col in range(1, num + 1):
#         if col % 3 == 0:
#             print(col, end= "\t")
#         else: print(row, end = "\t")
#     print()
# Задача 2. Дорога
# for row in range(20):
#     for col in range(50):
#         if col == row + 29:
#             print("\\",  end = " " )
#         elif col == -row + 19:
#             print("/", end = " ")
#         elif row == 9:
#             print("-", end=" ")
# #
# #
#         elif col == 24:
#             print("|", end =" ")
#         else: print(" ", end= " ")
#     print()
#
# Задача 1. Врата
# print("_" * 30)
# for row in range(20):
#     print("|" + " " * 28 + "|")
# size = int(input("Введите размер матрицы: "))
# for row in range(size):
#     for col in range(size):
#         if col < -row + size - 1:
#             print(0, end=" ")  # Значения выше диагонали
#         elif col > -row + size - 1:
#             print(2, end=" ")  # Значения ниже диагонали
#         else:
#             print(1, end=" ")  # Значения на диагонали
#     print()
# Задача 1. Электронная очередь
# num = int(input("Введите сколько в очереди: "))
# for hour in range(num):
#     print("Прошло",hour, "Часов", )
#     for people in range(hour, num):
#         print("В очереди: ", people, )
#     print()
# Задача 2. Цифры больше пяти
# # seqnumber = int(input("сколько будет чисел: "))
# num_count = 0
#
# for i in range(seqnumber):
#  num = int(input("Введите число: "))
#  while num != 0:
#    if num % 10 > 5:
#      num_count += 1
#    num //= 10
# print("цифр больше 5 в последовательности  ", num_count)
# Задача 3. Лестница чисел
# num = int(input("Введите число: "))
# for row in range(num + 1):
#  for col in range(row, num + 1):
#
#    print( col, end = "")
#  print()
#
#
# #Задача 1. Пирамидка
# height = int(input("Введите высоту пирамид: "))
# count = 0
# hashtag = "#"
# for row in range(height):
#     for col in range(height * 2 - 1):
#         continue
#     count += 1
#     print(" " * int(height - count), hashtag, " " * int(height - count))
#     hashtag += "##"
#
#
# Задача 1. Пирамидка
#
# height = int(input("Введите высоту пирамид: "))
# count = 0
# digit = 1
# for row in range(1, height + 1):
#     count += 1
#     print("  " * int(height - count), end ="")
#     for col in range(row):
#         print(digit, end = "  ")
#         digit += 2
#     print(" " * int(height - count))
#
#
# # Задача 2. Яма МОДУЛЬ 11 1 видео
# depth = (int(input("Введите глубину ямы: ")))
# count = 0
# for line in range(depth):
#     for left_number in range(depth, depth - line - 1, -1 ):
#          print(left_number, end= " ")
#     for right_number in range(depth - line, depth + 1):
#         print(right_number, end = " ")
#     print()
#
#
#
# Задача 3. Индекс массы тела
# height = float(input("Какой у вас рост: "))
# weight = float(input("Какой у вас вес: "))
# bmi = round(weight / height ** 2, 2)
# print("Ваш индекс массы тела:  ", bmi)
# if bmi < 18.5:
#     print("У вас недостаточное масса тело")
# elif bmi < 25:
#     print("У вас нормальное масса тело")
# elif bmi < 30:
#     print("У вас избыточная масса тело")
# else: print("У вас ожирение")
#
# Задача 1. Ставки на спорт
#
# bit = int(input("Сколько ставим? "))
# coeficcient = float(input("Какой коэффициент? "))
# win = round(bit * coeficcient, 2)
# print("Потенциальный выигрыш: ", win)
#
# Задача 2. День рождения
# age = int(input("Введите возсрат: "))
# temperature = float(input("Температура тело: "))
# gift = round(age * 1.5 * temperature, 2)
# print(gift)
#
#
# Задача 1. Космические рейнджеры
#
# money = int(input("Сколько чатлов? "))
# CR = money / 2200
# rocket = CR / (1/2)
# print("Это ", CR, 'CR')
# print("Можно купить кораблей: ", int(rocket))
# Задача 1. Герон
# import math
# a = int(input("длина первой стороны: "))
# b = int(input("длина второй стороны: "))
# c = int(input("длина третьей стороны: "))
# p = (a + b + c) / 2
# S = math.sqrt(( p* (p - a) * (p - b) * (p - c)))
# print("Площадь = ", S)
# Задача 2. Игра
# import math
# distance = int(input("Введите расситояние: "))
# engle = int(input("Введите угол: "))
#
# x = distance * math.cos(engle)
# y = distance * math.sin(engle)
# print(x, y)
# Задача 3. Мега-калькулятор
# import math
# number = float(input("Введите число: "))
# print(math.floor(number), math.ceil(number), math.sqrt(number), abs(number), math.exp(number), math.log(number, 2), math.log(number, 10),
#       math.sin(number), math.cos(number), end=" ")
# if number > 0:
#     print(math.factorial(int(number)))
#
# Задача 1. Конвертация
# euro = int(input("Стоимость покупки в евро: "))
# dollar = euro * 1.25
# rubles = dollar * 60.87
# print("Стоимость в рублях: ", rubles)
# Задача 2. Грубая математика
# import math
# number = int(input("Введите количество чисел: "))
# for i in range(number):
#     num = float(input("Введите число: "))
#     if num > 0:
#         x = math.ceil(num)
#         print("x = ", math.ceil(num), "log(x) = ", math.log(x))
#     else:
#         x = math.floor(num)
#         print("x = ", math.floor(num), "exp(x) = ", math.exp(x))
#
# file = int(input("Укажите размер файла для скачивания: "))
# internet = int(input("Какова скорость вашего соединения: "))
# speed = 0
# time = 0
# while speed < file:
#     time += 1
#     speed += internet
#     procent = round(speed / file * 100, 0 )
#     if speed > file:
#         speed = file
#         procent = 100
#
#     print("Прошло ", time, "сек.", "Скачано", speed, "из", file, "мб (", int(procent), "%)")
# Задача 4. Первая цифра
# num = float(input("Введите число: "))
# a = (num * 10) % 10
# print("Первая цифра после запятой: ", int(a))
#
# import math
# planet = float(input("Введите радиус случайной планеты: "))
# earth = 1.08321 * 10 ** 12
# V = 4/3 * math.pi * planet ** 3
# if earth > V:
#     times = round(earth / V, 3)
#     print("Объем планеты Земля больше в ", times, "раз")
# else:
#     times = round(V / earth, 3)
#     a = round(earth / V, 3)
#     print("Объем планеты Земля меньше в (1/",a,") = ", times,"раз")
#
# Шаг 1. Шахматная доска и её координаты
# x = float(input("Введите местоположение коня по вертикали: "))
# y = float(input("Введите местоположение коня по горизонтали: "))
# z = float(input("Введите местоположение точки на доске: по вертикали: "))
# c = float(input("Введите местоположение точки на доске: по горизонтали: "))
# xSquare = int(x * 10)
# ySquare = int(y * 10)
# zSquare = int(z * 10)
# cSquare = int(c * 10)
# print("Конь в клетке",xSquare, ySquare, "Точка в клетке",zSquare, cSquare )
# if (zSquare == xSquare + 2 or zSquare == xSquare - 2) and (cSquare == ySquare - 1 or cSquare == ySquare + 1):
#     print("Да, конь может ходить в эту точку.")
# elif (zSquare == xSquare + 1 or zSquare == xSquare - 1) and (cSquare == ySquare - 2 or cSquare == ySquare + 2):
#     print("Да, конь может ходить в эту точку.")
# else: print("Нет, конь не может ходить в эту точку.")
#
#
# Задача 2. Максимальное из двух
# FirstNumber = int(input("Введите первое число: "))
# SecondNumber = int(input("Введите второе число: "))
#
# plus = FirstNumber + SecondNumber
#
# minus = FirstNumber - SecondNumber
# result = (plus + abs(minus)) // 2
# print(result)
#
# Задача 1. Робот
# def greeting():
#     print('Привет!')
#     print('Добро пожаловать!')
#
# while True:
#     a = input('Зайдёте? Да/Нет: ')
#     if a == 'Да':
#         greeting()
#     print('Следующий.\n')
# Задача 2. Провизия
# def AmountFood():
#     a = int(input())
#     b = int(input())
#     print("Всего", a + b, "шт.")
#
# print("Сколько мешков рыбы и мяса?")
# AmountFood()
# print("Сколько буханок белого и чёрного хлеба?")
# AmountFood()
# print("Сколько вёдер воды и молока?")
# AmountFood()
#
#
#
# Задача 3. Почта
# SurName = input("Фамилия: ")
# name = input("Имя: ")
# street = input("Улица: ")
# flat = input("Дом: ",)
# print()
# def biography():
#     print("Фамилия: ",SurName)
#     print("Имя: ",name)
#     print("Улица ",street)
#     print("Дом ",flat)
#     print()
# biography()
# biography()
# biography()
#
# Задача 1. Вода
# def about_water(price):
#     print("Название: КлирВотер")
#     print("Производитель: ВодЗавод")
#     print("Цена", price)
#     print()
# about_water(25)
# about_water(30)
# about_water(40)
#
#
# Задача 2. Вот это объёмы 2
# import math
# radius = float(input("Введите радиус планеты: "))
# def volume_sphere():
#     V = 3/4 * math.pi * radius ** 3
#     print("Объем шара: ",V)
# def area_sphere():
#     S = 4 * math.pi * radius ** 2
#     print("Площадь шара: ",S)
# area_sphere()
# volume_sphere()
#
# Простые числа
# def is_prime():
#     number = int(input("Введите количество чисел: "))
#     for i in range(number):
#         num = int(input("Введите число: "))
#         isPrime = True
#         if num < 2:
#             isPrime = False
#         for e in range(2,num - 1):
#             if num % e == 0:
#                 isPrime = False
#         if isPrime:
#             print("Простое число")
#         else:print("Составное число")
#
#
# is_prime()
#
#
# Задача 3. Почта
#
# def biography(SureName, name,country, city, street, house,number, room_number):
#     print("Фамилия: ",SurName)
#     print("Имя: ",name)
#     print("Страна проживание: ", country)
#     print("Город: ", city)
#     print("Улица ",street)
#     print("Номер дома: ",house_number)
#     print("номер квартиры: ", room_number)
#
#     print()
# biography('Амбашка', 'Амибетель')
# biography()
# biography()
#
#
#
#
#
# Задача 3. GPS-навигатор 2.0
# import math
# def myDistance(x,y):
#     distance = math.sqrt(x ** 2 + y ** 2)
#     print(distance)
# def betweenDistance(x1, y1, x2, y2):
#     distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
#     print(distance)
# choice = int(input("1 - расстояние до точки; 2 - расстояние между двумя точками: "))
# if choice == 1:
#     x = float(input("введите координаты икс: "))
#     y = float(input("Введите координаты игрек: "))
#     myDistance(x,y)
# elif choice == 2:
#     x1 = float(input("введите координаты 1 икс: "))
#     y1 = float(input("введите координаты 1 икс: "))
#     x2 = float(input("введите координаты 2 икс: "))
#     y2 = float(input("введите координаты 2 икс: "))
#     betweenDistance(x1, y1, x2, y2)
# else: print("неверный ввод")
#
#
# def GCD():
#     first_number = int(input("Введите первое число: "))
#     second_number = int(input('Введите второе число: '))
#     max = 0
#     if first_number > second_number:
#         for devider in range(1, second_number + 1):
#             if first_number % devider == 0 and second_number % devider == 0:
#                 if devider > max:
#                  max = devider
#     elif second_number > first_number:
#         for devider in range(1, first_number + 1):
#          if first_number % devider == 0 and second_number % devider == 0:
#              if devider > max:
#                 max = devider
#     print("Наибольший общий делитель: ", max)
# #GCD()
# def gcd(a, b):
#     while a != 0 and b !=0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     print("Наибольший общий делитель: ", a + b)
#
# gcd(18,30)
#
#
# number = int(input("Введите число: "))
#
# def summ_n(num):
#     summ = 0
#     for i in range(num + 1):
#         summ += i
#     return(summ)
#
# first_summ = summ_n(number)
# summa = summ_n(first_summ)
# print("Сумма от 1 до", number, "=", summ_n(number))
# print("Сумма от 1 до ", summ_n(number), "=", summa)
#
# Задача 2. «Назад в будущее»
# import math
# first_number = int(input("Введите первое число: "))
# second_number = int(input("Введите второе число: "))
# def gcd(a, b):
#     print("НОД = ",math.gcd(a, b))
#
# gcd(first_number,second_number)
#
#
# def numeral_count(number):
#    count = 0
#    if number < 0:
#        print("отрицательно число! Обнуляю!")
#        return 0
#
#    while number > 0:
#        number //= 10
#        count += 1
#
#    return count
#
# amount_number = int(input("Введите количество чисел: "))
# for i in range(amount_number):
#     num = int(input("Введите число: "))
#     max = 0
#     temp = num
#     max_number = 0
#     if numeral_count(temp) > max:
#         max = numeral_count(temp)
#         max_number = num
# print(max_number)
#
# Задача 2. Тестирование
# number = float(input("Введите число в эксп. форме: "))
# x = 1
# count = 0
# while x <= 2:
#     x += number
#     count += 1
# print("Количество прибавлений: ", count)
#
#
# x = float(input("Введите число: "))
# count = 0
# while x > 10:
#     x /= 10
#     count += 1
# print("Формат плавающей точки: x = ", x, "*", 10, "**", count )
#
# def eqv(fnum,snum,sumnum):
#     a = fnum + snum
#     return abs(a -sumnum) < 1e-15
#
#
#
#
#
# first_number = float(input("Введите первое число: "))
# second_number = float(input("Введите второе число: "))
# summ = float(input("Введите третье число: "))
#
# print(eqv(first_number,second_number,summ))
#
# def rock_paper_scissors():
#   import random
#   options = ["ножницы", "камень", "бумага"]
#   person_choice = input("Выберите: камень, ножницы или бумага? ")
#   comp_choice = random.choice(options)
#   print("Компьютер выбрал ",comp_choice)
#   if person_choice == comp_choice:
#     print("Ничья")
#   elif person_choice == "камень":
#     if comp_choice == "ножницы":
#         print("Вы победили! Камень бьёт ножницы.")
#     else:
#         print("Вы проиграли! Бумага кроет камень.")
#   elif person_choice == "ножницы":
#     if comp_choice == "бумага":
#         print("Вы победили! Ножницы режут бумагу.")
#     else:
#         print("Вы проиграли! Камень бьёт ножницы.")
#   elif person_choice == "бумага":
#     if comp_choice == "камень":
#         print("Вы победили! Бумага кроет камень.")
#     else:
#         print("Вы проиграли! Ножницы режут бумагу.")
#   else:
#     print("Неверный ввод. Пожалуйста, выберите камень, ножницы или бумага.")
#   choice = int(input("1 - меню; 2 - еще раз"))
#   if choice == 1:
#     main_menu()
#   elif choice == 2:
#     rock_paper_scissors()
#   else: print("Неправильный ввод")
#
# def guess_the_number():
#   import random
#   comp_number = random.randint(1, 10)
#   print("Компьютер загадал число!")
#   seeking_number = int(input("Угдайте число от 1 до 10 "))
#   while seeking_number != comp_number:
#     if seeking_number > comp_number:
#       print("Не угадал! Мое число меньше!")
#     else: print("Не угадал! Мое число больше")
#     seeking_number = int(input("Угдайте число от 1 до 10 "))
#   print("Угадал!")
#   choice = int(input("1 - меню; 2 - еще раз"))
#   if choice == 1:
#     main_menu()
#   elif choice == 2:
#     guess_the_number()
#   else: print("Неправильный ввод")
#
# # guess_the_number()
#
#
#
#
# def main_menu():
#   game = int(input("выберети игру  1 - камень, бумага и ножницы; 2 - Угадай число!:  "))
#   if game == 1:
#     rock_paper_scissors()
#   elif game == 2:
#     guess_the_number()
#   else: print('Неправальный ввод')
#
#
#
# main_menu()
#
#
# first_n = int(input("Введите первое число: "))
# first_num_count = 0
# temp = first_n
#
#
# while temp > 0:
#     first_num_count += 1
#     temp = temp // 10
#
#
# if first_num_count < 3:
#     print("В первом числе меньше трёх цифр.")
# else:
#     last_digit = first_n % 10
#     first_digit = first_n // 10 ** (first_num_count - 1)
#     between_digits = first_n % 10 ** (first_num_count - 1) // 10
#     first_n = last_digit * 10 ** (first_num_count - 1) + between_digits * 10 + first_digit
#     print('Изменённое первое число:', first_n)
#
# danger_zone = float(input("Введите максимально допустимый уровень опасности: "))
# min = 0
# max = 4
# while True:
#     average = (min + max) / 2
#     x = average
#     D = x ** 3 - 3 * x ** 2 - 12 * x + 10
#     if D > 0:
#         min = x
#     else:
#         max = x
#     if abs(D) < danger_zone:
#         print(x)
#         break
#
# MyProfile app
#
# SEPARATOR = '------------------------------------------'
#
# # user profile
# name = ''
# age = 0
# phone_number = ''
# email = ''
# index = ''
# index_adress = ''
# additional_information = ''
# # information of entrepreneur
# ogrnip = ''
# INN = ''
# bank_account = ''
# name_bank = ''
# BIK = ''
# correspondent_account = ''
# def checking_ogrnip():
#     while True:
#         ogrnip = input("Введите ОГРНИП: ")
#         if ogrnip.isdigit():
#             count = 0
#             for digit in ogrnip:
#                 count += 1
#                 if count == 15:
#                     return ogrnip
#         print("ОГРНИП должен содержать 15 цифр.")
# def checking_bank():
#     while True:
#         bank_account = input("Введите Расчётный счёт: ")
#         if bank_account.isdigit():
#             count = 0
#             for digit in bank_account:
#                 count += 1
#                 if count == 15:
#                     return bank_account
#         print("Расчётный счёт должен содержать 20 цифр")
#
#
# def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, information_parameter, index_parameter, index_adress_parameter):
#     print(SEPARATOR)
#     print('Имя:    ', name_parameter)
#     if 11 <= age_parameter % 100 <= 19:
#         years_parameter = 'лет'
#     elif age_parameter % 10 == 1:
#         years_parameter = 'год'
#     elif 2 <= age_parameter % 10 <= 4:
#         years_parameter = 'года'
#     else:
#         years_parameter = 'лет'
#
#     print('Возраст:', age_parameter, years_parameter)
#     print('Телефон:', phone_parameter)
#     print('E-mail: ', email_parameter)
#     print('Индекс: ', index_parameter)
#     print('Адрес: ', index_adress_parameter)
#     if additional_information:
#         print('')
#         print('Дополнительная информация:')
#         print(information_parameter)
#
#
# print('Приложение MyProfile')
# print('Сохраняй информацию о себе и выводи ее в разных форматах')
#
# while True:
#     # main menu
#     print(SEPARATOR)
#     print('ГЛАВНОЕ МЕНЮ')
#     print('1 - Ввести или обновить информацию')
#     print('2 - Вывести информацию')
#     print('0 - Завершить работу')
#
#     option = int(input('Введите номер пункта меню: '))
#     if option == 0:
#         break
#
#     if option == 1:
#         # submenu 1: edit info
#         while True:
#             print(SEPARATOR)
#             print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
#             print('1 - Личная информация')
#             print('2 - Информация о предпринимателе')
#             print('0 - Назад')
#
#             option2 = int(input('Введите номер пункта меню: '))
#             if option2 == 0:
#                 break
#             if option2 == 1:
#                 # input general info
#                 name = input('Введите имя: ')
#                 while 1:
#                     # validate user age
#                     age = int(input('Введите возраст: '))
#                     if age > 0:
#                         break
#                     print('Возраст должен быть положительным')
#
#                 users_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
#                 phone_number = ''
#                 for ch in users_phone:
#                     if ch == '+' or ('0' <= ch <= '9'):
#                         phone_number += ch
#
#                 email = input('Введите адрес электронной почты: ')
#                 numeric_index = input('Введите почтовый индекс: ')
#                 for char in numeric_index:
#                     if char.isdigit():
#                         index += char
#
#
#                 index_adress = input("Введите почтовый адрес (без индекса): ")
#
#
#                 additional_information = input('Введите дополнительную информацию:\n')
#
#             elif option2 == 2:
#                 # input information of entrepreneur
#                 ogrnip = checking_ogrnip()
#                 INN = input("Введите ИНН: ")
#                 bank_account = checking_bank()
#                 name_bank = input("Введите название банка: ")
#                 BIK = input("Введите БИК: ")
#                 correspondent_account = input("Введите корреспондентский счет: ")
#             else:
#                 print('Введите корректный пункт меню')
#     elif option == 2:
#         # submenu 2: print info
#         while True:
#             print(SEPARATOR)
#             print('1 - Общая информация')
#             print('2 - Вся информация')
#             print('0 - Назад')
#
#             option2 = int(input('Введите номер пункта меню: '))
#             if option2 == 0:
#                 break
#             if option2 == 1:
#                 general_info_user(name, age, phone_number, email, additional_information, index, index_adress)
#
#             elif option2 == 2:
#                 general_info_user(name, age, phone_number, email, additional_information, index, index_adress)
#
#                 # print Entrepreneur info
#                 print('')
#                 print('Информация о предпринимателе')
#                 print('ОРГНИП: ', ogrnip)
#                 print('ИНН: ', INN)
#                 print('Банковские реквизиты')
#                 print('Р/c: ', bank_account)
#                 print('Банк: ', name_bank)
#                 print('БИК: ', BIK)
#                 print('К/c: ', correspondent_account)
#             else:
#                 print('Введите корректный пункт меню')
#     else:
#         print('Введите корректный пункт меню')
from itertools import count
from re import search

# Задача 1. Таблица степеней
# numbers = [3, 7, 5]
#
# while True:
#     number = int(input('Новое число: '))
#     numbers.append(number)
#     print('Текущий список чисел:', numbers)
#     for i in numbers:
#         print(i ** 2, i ** 3, i ** 4)
#         print()


# numbers = []
# for i in range(101):
#     numbers.append(i)
# print(numbers)


# Задача 3. Контроль
#
# amount_workers = int(input('Количество работников в офисе: '))
# ID = []
# while amount_workers > 0:
#     amount_workers -= 1
#     worker_id = int(input('Введите ID сотрудника: '))
#     ID.append(worker_id)
# search_ID = int(input('Какой ID ищем: '))
# found = False
# for index in ID:
#     if search_ID == index:
#         print('Сотрудник на месте')
#         found = True
#         break
# if not found:
#     print('Сотрудник не работает')



# Задача 1. Гугл
# nums_list = []
#
# N = int(input('Кол-во чисел в списке: '))
#
# for _ in range(N):
#     num = int(input('Очередное число: '))
#
#     nums_list.append(num)
#
# maximum = nums_list[0]
#
# minimum = nums_list[0]
#
# for index in nums_list:
#     if maximum < index:
#         maximum = index
#
#     elif minimum > index:
#         minimum = index
#
# print('Максимальное число в списке:', maximum)
#
# print('Минимальное число в списке:', minimum)
#
#


# Задача 2. Кратность

# n= int(input('Кол-во чисел в списке: '))
# num_list = []
# index = 0
# summ = 0
# for _ in range(n):
#     print("Введите", _ + 1 ,"число:", end= "  ")
#     num = int(input())
#     num_list.append(num)
# devider = int(input("Введите делитель: "))
# for i in num_list:
#
#     if num_list[index ] % devider == 0:
#         print("Индекс числа", num_list[index],":", index)
#         summ += index
#     index += 1n = int(input('Кол-во чисел в списке: '))



# n = int(input('Кол-во чисел в списке: '))
# num_list = []
# summ = 0
#
# for _ in range(n):
#     print("Введите", _ + 1, "число:", end="  ")
#     num = int(input())
#     num_list.append(num)
#
# devider = int(input("Введите делитель: "))
#
# for index, num in enumerate(num_list):
#     if num % devider == 0:
#         print("Индекс числа", num, ":", index)
#         summ += index
#
# print("Сумма индексов равна", summ)





# amount_dogs = int(input('Количество собак: '))
# dog_scores = []
#
# for _ in range(amount_dogs):
#     print("Очко", _ + 1,"собаки", end= " ")
#     scores = int(input())
#     dog_scores.append((scores))
# max_score = dog_scores[0]
# max_index = dog_scores[0]
# min_score = dog_scores[0]
# min_index = dog_scores[0]
# for index, scores in enumerate(dog_scores):
#     if scores > max_score:
#         max_score = scores
#         max_index = index
#     elif scores < min_score:
#         min_score = scores
#         min_index = index
#
# dog_scores[max_index] = min_score
# dog_scores[min_index] = max_score
#
# print('макс',max_index + 1, max_score, "мин",min_index + 1,min_score,)
# print(dog_scores)


# Задача 1. Текстовый редактор: возвращение
#
# text = input("Введите строку: ")
# replace_count = 0
# sym_list = list(text)
# for index, sym in enumerate(sym_list):
#     if sym == ':':
#         sym_list[index] = ';'
#         replace_count += 1
# print('исправление строка: ',end = "")
# for char in sym_list:
#     print( char, end="")
# print('\n','Количество замен: ', replace_count)

# Задача 2. Соседи
# text = input("Введите строку: ")
# i_text = int(input("Введите номер символа: "))
# symbol = ''
# sym_text = list(text)
# count = -1
# for index, char in enumerate(sym_text):
#     if i_text == index + 1:
#         print('Символ слева: ', sym_text[index - 1])
#         print('Символ справа: ', sym_text[index + 1])
#         symbol = char
# for char in sym_text:
#     if symbol == char:
#         count += 1
# if count == 0:
#     print("Таких же символов больше нет!")
#
# elif count == 1:
#     print("Есть ровно один такой же символ.")
#
# elif count > 1:
#     print('есть два и более таких же.')

# Задача 3. Улучшенная лингвистика
# word_list = []
# count = [0, 0, 0]
# for _ in range(3):
#     print('Введите', _ + 1, 'слово: ', end="")
#     word = input()
#     word_list.append(word)
#
# text = input('Введите слово из текста: ')
# while text != 'end':
#    for i in range(3):
#        if word_list[i] == text:
#            count[i] += 1
#    text = input('Введите слово из текста: ')
#
# print('Подсчёт слов в тексте')
# for i in range(3):
#     print(word_list[i], ':', count[i])