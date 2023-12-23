# Task 1. У списку цілих, заповненому випадковими числами обчислити:
# ■ Суму негативних чисел;
# ■ Суму парних чисел;
# ■ Суму непарних чисел;
# ■ Добуток елементів з кратними індексами 3;
# ■ Добуток елементів між мінімальним та максимальним елементом;
# ■ Суму елементів, що знаходяться між першим та останнім позитивними елементами.

import random

NUM_ELEMENTS = 10
MIN_NUMBER = -50
MAX_NUMBER = 50
numbers = [random.randint(MIN_NUMBER, MAX_NUMBER) for i in range(NUM_ELEMENTS)]

# for i in range(NUM_ELEMENTS):
#     numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))
print(numbers)

sumEven = 0
sumNegative = 0
sumOdd = 0
ProdIndexMultThree = 1


for i in numbers:
    if i < 0:
        sumNegative += i
    if i % 2 == 0:
        sumEven += i
    else:
        sumOdd += i

print("Сума негативних чисел: ", sumNegative)
print("Сума парних чисел: ", sumEven)
print("Сума непарних чисел: ", sumOdd)

del i  # видалимо змінну і, щоб запобігти накладання попередніх значень, які були в змінній

for i in range(3, len(numbers)):
    if i % 3 == 0:
        ProdIndexMultThree *= numbers[i]

del i

# визначимо одразу індекси мінімального та максимального значення. Якщо індекс мінімального значення більше
# індекса максимального, то для початкового індексу цикла присвоїмо індекс максимального значення і навпаки
minValueIndex = numbers.index(min(numbers))
maxValueIndex = numbers.index(max(numbers))
if minValueIndex < maxValueIndex:
     startIndex = minValueIndex
     endIndex = maxValueIndex
else:
     startIndex = maxValueIndex
     endIndex = minValueIndex

ProdBetweenMinMax = 1
for i in numbers[startIndex:endIndex]:
    ProdBetweenMinMax *= i
del i

for i in numbers[len(numbers):0:-1]:
    if i > 0:
        indexLastPositive = numbers.index(i)
        break
del i

for i in numbers[0:len(numbers)]:
    if i > 0:
        indexFirstPositive = numbers.index(i)
        break
del i

sumBetweenFirstLastPositive = 0
for i in numbers[indexFirstPositive:indexLastPositive]:
    sumBetweenFirstLastPositive += i

print("Добуток елементів з індексами, кратними 3: ", ProdIndexMultThree)
print("Добуток елементів між мінімальним та максимальним елементом: ", ProdBetweenMinMax)
print("Сума елементів між першим та останнім позитивним елементом: ", sumBetweenFirstLastPositive)