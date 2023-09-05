# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random
import math

maxNumber = 1000

firstNumber = random.randint(0,maxNumber)
secondNumber = random.randint(0,maxNumber)

p = firstNumber * secondNumber
s = firstNumber + secondNumber

def calculateNumbers(P:int, S:int):
    discriminant = math.sqrt(S ** 2 - 4 * P)

    x1 = (S + discriminant) / 2
    x2 = (S - discriminant) / 2

    return [int(x1),int(x2)]

calculatedNumbers = calculateNumbers(p,s)

print("Вводные числа: {}, {}".format(firstNumber,secondNumber))

print("Вычисленные числа: {}, {}".format(*calculatedNumbers))