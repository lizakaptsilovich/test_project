import math
#в скобках - аргументы которые передаеются в функцию
# def first_function(a, b):
#     s = a+b
#     print(s)
#
#
# x=int(input())
# y=int(input())
# first_function(x,y)

# def your_name():
#     name=input()
#     return name
# ma_name=your_name()
# print(ma_name)


# def first_function(a, b):
#     s = a+b
#     return s
# rez = first_function(2,3)
# если return - то вывод функции присвоится переменной, если принт - просто принтанет

# def get_sum(*nums): #когда не знаем кол-во аргументов или они одного типа и их слишком много
#     s=0
#     for a in nums:
#         s+=a
#     print(s)
# get_sum(1,2,3,4,5)

# def first(a):
#     return (a+math.sin(a))/3
#
# rez=0
# for i in range(1,7,2):
#      rez+=first(i)
# print(rez)


#факториал 10.17
# def fact(y):
#     s=1
#     for i in range(1,y+1):
#         s*=i
#     return s
# def sec():
#   y=(2*fact(5)+3*fact(8))
#   z=fact(6)+fact(4)
#   return y/z
#
# print(sec())

#рекурсия
# def rec(n):
#         if n>0:
#             return n * rec(n-2)
#         else:
#             return 1
#
# print(rec(8))

