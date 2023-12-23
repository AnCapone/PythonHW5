# Task 2: Є список цілих, заповнений випадковими числами.
# На підставі даних цього масиву потрібно:
# ■ Створити список цілих, що містить лише парні числа з першого списку;
# ■ Створити список цілих, що містить лише непарні числа з першого списку;
# ■ Створити список цілих, що містить лише негативні числа з першого списку;
# ■ Створити список цілих, що містить лише позитивні числа з першого списку.

import random

NUM_ELEMENTS = 20
MIN_NUMBER = -50
MAX_NUMBER = 50
numbers = [random.randint(MIN_NUMBER, MAX_NUMBER) for i in range(NUM_ELEMENTS)]

evenList = []
oddList = []
negativeList = []
positiveList = []

for i in numbers:
    if i % 2 == 0:
        evenList.append(i)
    if i % 2 != 0:
        oddList.append(i)
    if i < 0:
        negativeList.append(i)
    if i > 0:
        positiveList.append(i)

print("Початковий список: ", numbers)
print("Список з парними елементами: ", evenList)
print("Список з непарними елементами: ", oddList)
print("Список з негативними елементами: ", negativeList)
print("Список з позитивними елементами: ", positiveList)