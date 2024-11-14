import random

# 1


# print(f'Количество букв А: {len([i for i in input('Введите ваш текст: ') if i == 'А' or i == 'A'])}')

# 2

# ascii = 'АБВГДЕËЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмеопрстуфхцчшщъыьэюя0123456789'
# words, total = input('Введите ваш текст: '), 0
# if words == '':
#     print("Ошибка")
# else:

#     for elem in range(len(words)):
#         if words[elem - 1] in ascii and words[elem] == ' ':
#             total += 1
#     if words[len(words) - 1] == ' ':
#         total -= 1
#     print(f'Количесвто слов в тексте: {total + 1}')

# 3
try:
    digits, count = [random.randint(-10, 10) for _ in range(int(input('Введите количество чисел: ')))], 0
    a, b = float(input('Введите левую грницу: ')), float(input('Введите правую границу: '))
    if a > b:
        print('Неверно указаны границы')
    else:
        print(digits)
        for el in digits:
            if el >= 0:
                count += el
            else:
                break
        print(f'Сумма элементов до первого отрицательного элемента: {count}')

        result = []
        for h in digits:
            if h < 0:
                h *= -1
            if h < a or h > b:
                result += [h]

        while len(result) < len(digits):
            result += [0]

        print(f"Сжатый список: {result}")
except:
    print('ВВЕДЕНО НЕВЕРНОЕ ЗНАЧЕНИЙЕ')
