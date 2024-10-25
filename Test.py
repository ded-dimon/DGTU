from math import factorial

# 1
# try:
#     days, p, nach, total_distance = 1, float(
#         input("Введите процентное значение от 0 до 50 если хотетите решить задачу: ")), 10, 0
#     if 0 < p < 50:
#         while total_distance <= 200:
#             total_distance += nach
#             nach *= (1 + p / 100)
#             days += 1
#         print(f"Кол-во дней: {days}\nСуммарынй пробег: {total_distance}")
#     else:
#         print("НЕВЕРНО ВВЕДЕНО ЗНАЧЕНИЕ")
# except:
#     print("НЕВЕРНО ВВЕДЕНО ЗНАЧЕНИЕ")

# 2
# print("Найти НОД а и b")
# try:
#     a, b = int(input("Введите значение а: ")), int(input("Введите значение b: "))
#     while b != 0:
#         a, b = b, a % b
#     print("НОД а и b:", a)
# except:
#     print("НЕВЕРНО ВВЕДЕНО ЗНАЧЕНИЕ")


# 3
# try:
#     x, n = float(input("Введите значение х: ")), int(input("Введите знасение n: "))
#     result = sum([x ** i / factorial(i) for i in range(1, n + 1)])
#     print(f"Сумма равна: {result}")
# except:
#     print("НЕВЕРНО ВВЕДЕНО ЗНАЧЕНИЕ")
