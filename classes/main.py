import math

# x = int(input("введите число"))
# y = int(input("введите число"))
# if -4 < x < 5 and -4 < y < 3:
#     print('zone2')
# else:
#     print('zone1');

#4.1
# x=int(input())
# if x>0:
#     y=math.sin(x)**2
# else:
#     y=1-2*math.sin(x**2)
# print(y)

#4.2
# x=int(input())
# if x>0:
#     y=math.sin(x**2)
# else:
#     y=1+2*math.sin(x)**2
# print(y)

#4.5
# x=int(input())
# if 0 <= x <= 2:
#     y=x
#     print(y)
# elif x>2:
#     y=2
#     print(y)
# else:
#     print('y is unknown')

#4.10
# r=int(input('введите радиус: '))
# l=int(input('введите длину стороны квардрата: '))
# circle_area=math.pi*r**2
# square_area=l**2
# if circle_area>square_area:
#     print('площадь круга больше площади квардрата')
# elif circle_area<square_area:
#     print('площадь квадрата больше площади круга')
# else:
#     print('площади обеих фигур равны')

#4.17
#a-сторона треугольника, r-радиус окружности
# a=int(input())
# r=int(input())
# R=a/math.sqrt(3)
# A=a/(2*math.sqrt(3))
# if R>r:
#     print('треугольник не поместится в круг')
# else:
#     print('треугольник поместится в круг')
# if A>r:
#     print('круг не поместится в треугольник')
# else:
#     print('круг поместится в треугольник')

#4.29
# a=str(input('введите трехзначное число'))
# b=int(a)**2
# c=(int(a[0])**3)+(int(a[1])**3)+(int(a[2])**3)
# if b==c:
#     print('равен')
# else:
#     print('не равен')

#4.36 - моя версия
# t=str(input())
# if int(t[-1]) in (0,1, 2) or int(t[-1]) in (5,6,7):
#     print('зеленый')
# else:
#     print('красный')
#
# #4.36 - openai
# t = float(input("Введите время в минутах: "))
# period = t % 5  # остаток от деления на 5
# if period < 3:
#     print("зеленый")
# else:
#     print("красный")

#4.91
# x=float(input())
# if x<=-1:
#     y=0
# elif -1<x<1:
#     y=x
# else:
#     y=1
# print(y)



#4.115
n = int(input("Введите год: "))
delta = n - 1984  # смещение от года Зеленой Крысы

# Определение животного
animal_cycle = delta % 12
if animal_cycle == 0:
    y = 'Крыса'
elif animal_cycle == 1:
    y = 'Корова'
elif animal_cycle == 2:
    y = 'Тигр'
elif animal_cycle == 3:
    y = 'Заяц'
elif animal_cycle == 4:
    y = 'Дракон'
elif animal_cycle == 5:
    y = 'Змея'
elif animal_cycle == 6:
    y = 'Лошадь'
elif animal_cycle == 7:
    y = 'Овца'
elif animal_cycle == 8:
    y = 'Обезьяна'
elif animal_cycle == 9:
    y = 'Петух'
elif animal_cycle == 10:
    y = 'Собака'
elif animal_cycle == 11:
    y = 'Свинья'
else:
    y = 'Неизвестно'

# Определение цвета
color_cycle = (delta % 10) // 2
if color_cycle == 0:
    y1 = 'Зеленый'
elif color_cycle == 1:
    y1 = 'Красный'
elif color_cycle == 2:
    y1 = 'Желтый'
elif color_cycle == 3:
    y1 = 'Белый'
elif color_cycle == 4:
    y1 = 'Черный'
else:
    y1 = 'неизвестно'

print(y, y1)

