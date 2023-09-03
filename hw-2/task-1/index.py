# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
import random

coinsCount = 10
coinTypes = ['tails-up','emblem-up']

def getCoinList (coinsCount:int):
    coinList = list()

    i = 0
    
    while i + 1 <= coinsCount :
        coinType = coinTypes[random.getrandbits(1)]
        coinList.append(coinType)
        i+=1

    return coinList

coinList = getCoinList(coinsCount)

def getMinNumberOfCoinsToFlip (coinList):
    coinUpTailsCount = 0
    coinUpEmblemCount = 0

    for coin in coinList:
        if(coin == 'tails-up'):
            coinUpTailsCount += 1
        else:
            coinUpEmblemCount += 1

    minCount = min([coinUpTailsCount,coinUpEmblemCount])

    # Если минимальное число == 0, тогда нужно переворачивать
    if(minCount == 0):
        return len(coinList)
    else:
        return minCount


print(
    coinList,
    getMinNumberOfCoinsToFlip(coinList)
)