# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

list_1 = [4,3,5,2,4,1]
list_2 = [2,4,6,6,3,1]



print(
    sorted(
        set.union(
            set(list_1),
            set(list_2)
        )
    )
)

# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
set_1 = set()
set_2 = set()

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

print("Введите элементы первого множества:")
for _ in range(n):
    num = int(input())
    set_1.add(num)

print("Введите элементы второго множества:")
for _ in range(m):
    num = int(input())
    set_2.add(num)

print(
    sorted(set_1.intersection(set_2))
)