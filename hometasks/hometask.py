#5.13
# for a in range(1,10):
#     b = 7*a
#     print(a, '* 7 =',b)
import math

#5.37
# sum = 1
# x = 2
# a = 1
# b = 2
# for i in range(1, 11):
#     if i%2==1:
#         sum -= ((a/b)*(x**i))
#     elif i%2==0:
#         sum += ((a/b)*(x**i))
#     a += 1
#     b += 1
# print(sum)


#5,38 а
# sum = 0
# for i in  range (1, 101):
#     if i%2==0:
#         sum -= 1/i
#     elif i%2==1:
#         sum +=1/i
# m = sum*1000
# print(f'муж отошел от дома на {round(m, 0)} метров')
#
# #5,38 б
# k = 0
# for i in  range (1, 101):
#     k += (1/i)*1000
# print(round(k, 0))


#5.92
# sum=0.0
# for i in range(50, 0, -1):
#     sum = math.sqrt(i + sum)
# print(sum)


#6.31
# n = int(input) #56425
# min = 9
# count = 0
# while n > 0:
#     digit = n//10
#     if digit < min:
#         min=digit
#         count = 1
#     elif digit == min:
#         count +=1
# print(count)