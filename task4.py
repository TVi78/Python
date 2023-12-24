# Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть 
# разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.

a = 3
b = 2
c = 1

# Введите ваше решение ниже
# if(c%a==0):
#     ost=c//a
#     if(ost<=b):
#         otvet="yes"
#     else:
#         otvet="no"
# if(c%b==0):        
#     ost=c//b
#     if(ost<=a):
#         otvet="yes"
#     else:
#         otvet="no"
# if(c%a!=0 and c%b!=0): 
#     otvet="no"
# print(otvet)

if c <= b * a and (c % a == 0 or c % b == 0):
    print('yes')
else:
    print('no')