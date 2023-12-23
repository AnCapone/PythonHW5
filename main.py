# Task 1. У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;
# ■ Суму парних чисел;
# ■ Суму непарних чисел;
# ■ Добуток елементів з кратними індексами 3;
# ■ Добуток елементів між мінімальним та максимальним елементом;
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.

import random

NUM_ELEMENTS = 30
MIN_NUMBER = -50
MAX_NUMBER = 50
numbers = []

for i in range(NUM_ELEMENTS):
    numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))

sumEven = 0
sumNegative = 0

for i in numbers:
    if