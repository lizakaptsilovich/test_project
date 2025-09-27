import math

#10.2b
# def first(a,b):
#     return (a+math.sin(a))/(math.sin(b)+b)
# rez=first(2,5)+first(6,3)+first(1,4)
# print(rez)

#10.2c
# def first(a,b):
#     return (b+math.sin(a))/(math.sin(b)+a)
# rez=first(2,5)+first(6,3)+first(1,4)
# print(rez)

#10.2d
# def first(a,b):
#     return (a+math.sin(b))/(math.sin(a)+b)
# rez=first(2,3)+first(1,5)+((math.sin(7)+4)/(math.sin(3)+7))
# print(rez)

#10.5
# def sign(a):
#     if a>0:
#         return 1
#     elif a==0:
#         return 0
#     elif a<0:
#         return -1
# z=sign(int(input()))+sign(int(input()))
# print(z)



#10.14
# def five(a):
#     if a<0:
#         return False
#     while a%5==0:
#         a//=5
#     if a==1:
#         return a==1
# count=0
# l=(5,-1,4,25,6,125,-125)
# for i in l:
#     if five(i):
#         count+=1
# print(count)


#10.45
# def func(a1, d, n):
#     if n == 1:
#         return a1
#     else:
#         return func(a1, d, n-1) + d
#
# # Пример использования:
# a1 = 3  # первый член
# d = 2   # разность
# n = 5   # хотим найти 5-й член
# print(func(a1, d, n))  # Вывод: 11

#10.47


a = 'bitcoin,crypto,trading,exchange,BTC,ETH,XRP,blockchain,cryptocurrency,wallet,buy,sell,trade,invest'
print(len(a))