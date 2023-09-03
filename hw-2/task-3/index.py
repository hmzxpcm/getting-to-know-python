# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import random
import math

n = random.randint(0,100000)

def getPowerList (maxNumber:int):
    power = 1
    powerList = []

    while math.pow(2,power) <= maxNumber:
        powerList.append(int(math.pow(2,power)))

        power += 1

    return powerList

print(f"Максимальное число N: {n}")
print(f"Числа в виде 2k: {getPowerList(n)}")