import random

#1
# try:
#     n, total = int(input('Введите количество элементов: ')), 0
#     if n > 0:
#         result = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
#         print(*result, sep='\n')
#         for i in range(n):
#             for j in range(n):
#                 flag = True
#                 if i > 0 and result[i][j] >= result[i - 1][j]:
#                     flag = False
#                 elif i < n - 1 and result[i][j] >= result[i + 1][j]:
#                     flag = False
#                 elif j > 0 and result[i][j] >= result[i][j - 1]:
#                     flag = False
#                 elif j < n - 1 and result[i][j] >= result[i][j + 1]:
#                     flag = False
#
#                 if flag is True:
#                     total += 1
#         print(f'Количество локальных минимумов: {total}')
#     else:
#         print('ВВЕДЕНА НЕВЕРНАЯ ДЛИНА СПИСКА')
# except:
#     print('ВВЕДЕНО НЕВЕРНОЕ ЗНАЧЕНИЕ')
#
#
# 2
# try:
#     m, count = int(input('Введите количество элементов: ')), 0
#     if m > 1:
#         lst = [[random.randint(-10, 10) for _ in range(m)] for _ in range(m)]
#         print(*lst, sep='\n')
#         for k in range(m):
#             for h in range(m):
#                 if h > k and lst[k][h] < 0:
#                     count += 1
#         print(f'Количество отрицательных чиел выше главной диагонали: {count}')
#     else:
#         print('ЛИБО ЗНАЧЕНИЕ ВВЕДЕНО ОТРИЦАТЕЛЬНОЕ, ЛИБО ГЛАВНАЯ ДИАГОНАЛЬ СОСТОИТ ИЗ 1 ЭЛЕМЕНТА')
# except:
#     print('ВВЕДЕНО НЕВЕРНОЕ ЗНАЧЕНИЕ')
# 3
try:
    n, vocabulary = int(input('Введите число элементов в словаре: ')), {}
    if n > 0:
        for _ in range(n):
            row, country = input('Введите название реки: '), input('Введите страну в которой находится эта река: ')
            if row.isalpha() == True and country.isalpha() == True:
                vocabulary[row] = country

    lst = [input('Введите реку для списка поиска: ') for _ in range(n)]
    print(vocabulary)
    for elem in vocabulary.items():
        if elem[0] in lst:
            print(f'{elem[0]} в {elem[1]}')
    if n <= 0 or len(vocabulary) == 0:
        print('Словарь пуст или его количество отрицательно')
except:
    print('ВВЕДЕНО НЕВЕРНОЕ ЗНАЧЕНИЕ')