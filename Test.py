import csv

num = int(input()) - 1
with open('deniro.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file)
    result = sorted(rows, key=lambda x: int(x[num]) if x[num].isdigit() else x[num])
    for elem in result:
        print(*elem)