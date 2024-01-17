# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# На вход подается 2 числа через пробел: n m
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

# import random
# list=[4,5]
# n=list[0]
# m=list[1]

# randomSet1=[]
# randomSet2=[]
randomSet3=[]

# randomSet1=[random.randint(0, 10) for i in range(n)]
# randomSet2=[random.randint(0, 10) for i in range(m)]
randomSet1='10 20 30 40 50'
randomSet2='10 20 30 40 50'

print(randomSet1)
print(randomSet2)
for j in randomSet1.split():
    print(f"j: {j}")
    for i in randomSet2.split():
        if j==i:
            randomSet3.append(i)
print(randomSet3)
randomSet3=sorted(set(randomSet3))  
print(*randomSet3, sep=' ')

# mol = [int(x) for x in var1.split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in var2.split()]
# k = set(a)
# for i in k:
#    set_1.add(i)
# b = [int(x) for x in var3.split()]
# k1 = set(b)
# for i in k1:
#    set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#    print(i, end=' ')