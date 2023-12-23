# Add Task: створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99
# вивести на екран
# - вивести суму чисел головної діагоналі матриці
# - вивести мінімальне та максимальне значення побічної діагоналі матриці
# - ввести з клавіатури порядковий номер стовпця - вивести цифри з цього стовпця на екран (аналогічно зробити з рядком)
# - ввести з клавіатури порядковий номер одного стовпця і потім іншого стовпця і поміняти їх місцями в матрицю
# (аналогічно зробити з рядком)

import random
NUM_ELEMENTS = 10
MIN_NUMBER = -90
MAX_NUMBER = 90
numbers = [[random.randint(MIN_NUMBER, MAX_NUMBER) for i in range(NUM_ELEMENTS)] for j in range(NUM_ELEMENTS)]

for i in range(NUM_ELEMENTS):
    for j in range(NUM_ELEMENTS):
        print(numbers[i][j], end=' ')
    print("")

mainDiag = []
sumMainDiag = 0
sideDiag = []

for i in range(NUM_ELEMENTS):
    mainDiag.append(numbers[i][i])
    sideDiag.append(numbers[i][NUM_ELEMENTS-1-i])
    sumMainDiag += numbers[i][i]

print("\nГоловна діагональ: ", mainDiag)
print("Допоміжна діагональ: ", sideDiag)
print("Сума елементів головної діагоналі: ", sumMainDiag)
print("Мінімум побічної діагоналі: ", min(sideDiag))
print("Максимум побічної діагоналі: ", max(sideDiag))

