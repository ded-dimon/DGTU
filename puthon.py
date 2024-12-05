# 1
# def stepen(x: float, n: int):
#     total = 1
#     for _ in range(abs(n)):
#         total *= x
#     return total if n > 0 else 1 / total
#
#
# def F(k: int, a: int):
#     return stepen(2.7, k) + stepen((a + 1), -5)
#
#
# try:
#     row, integer = int(input('Введите значение степени для 2.7: ')), float(input('Введите значения а для функции: '))
#     print(F(row, integer))
# except:
#     print('Введено неверное значение')

# 2
# def IsLeapYear(Y):
#     if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
#         return 'TRUE'
#     else:
#         return 'FALSE'
#
#
# for _ in range(5):
#     try:
#         year = int(input('Введите год на проверку нависокосность: '))
#         if year >= 0:
#             print(f'{year} год является {IsLeapYear(year)}')
#         else:
#             print('Введене неверное значение')
#     except:
#         print('Введене неверное значение')

# 3
# def recur(N):
#     if N == 1:
#         return "YES"
#     elif N % 2 != 0:
#         return "NO"
#     return recur(N // 2)
#
#
# try:
#     N = int(input('Введите число для проверки на степень 2: '))
#     if N >= 0:
#         print(recur(N))
#     else:
#         print('Введене ненатуральное значение')
# except:
#     print('Введене неверное значение')
