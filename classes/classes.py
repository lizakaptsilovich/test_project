class Car:
    def __init__(self, marka, model, power, price):
        self.marka = marka
        self.model = model
        self.power = power
        self.price = price
    def get_marka(self):
        return self.marka
    def set_marka(self, marka):
        self.marka = marka
    def get_model(self):
        return self.model
    def set_model(self, model):
        self.model = model
    def get_power(self):
        return self.power
    def set_power(self, power):
        self.power = power
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def tuning(self, power_plus):
        self.power += power_plus
        self.price += 7000
        self.marka = "Brabus"


    def __str__(self):
        return f"{self.model} {self.marka} {self.price} {self.power}"
    def __int__(self):
        return self.power
mers = Car("Mercedes", "E224", 220, 4500)
bmw = Car("bmw", "s5", 230, 30000)
audi = Car("audi", "a6", 3000, 50000)
cars = []
#print(Car.get_model(bmw)) = bmw.get_model() #два варианта одного действия

for a in (mers,bmw,audi):
    cars.append(a)
for a in cars:
    print(a)
while True:
    marka=input('marka:')
    if marka.lower() =='stop':
        break
    model=input('model:')
    power=int(input('power:'))
    price=int(input('price:'))
    new_car=Car(marka,model,power,price)
    cars.append(new_car)
for i in cars:
    print(i)

# for i in (mers, bmw, audi):
#     cars.append(i)
# for i in cars:
#     print(i)

# print(mers.power)
# mers.tuning(50)
# print(mers) #ссылка на область в памяти
# print(mers.power, mers.marka)
# mers.set_marka("you")
# print(mers.marka)
# print(mers) #есть есть __str__ то можно так
# x=int(mers)#
# print(x)#или так


class Customer:
    def __init__(self, bio, age, sex, money):
        self.bio = bio
        self.age = age
        self.sex = sex
        self.money = money
    def get_bio(self):
        return self.bio
    def set_bio(self, bio):
        self.bio = bio
    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age
    def get_sex(self):
        return self.sex
    def set_sex(self, sex):
        self.sex = sex
    def get_money(self):
        return self.money
    def set_money(self, money):
        self.money = money
    def __str__(self):
        return f"{self.bio} {self.age} {self.sex} {self.money}"
Liza = Customer("Liza", 28, "F", 50000)
Ann = Customer("Ann", 22, "F", 20000)
Mom = Customer("Mom", 54, "M", 40000)
customers = []
for i in (Liza, Ann, Mom):
    customers.append(i)
# for i in customers:
#     print(i)

#добавление новых кастомеров с клавиатуры пока не напишешь stop
# while True:
#     name = input("имя: ")
#     if name.lower() == "stop":
#         break
#     age = int(input("возраст: "))
#     sex = input("пол: ")
#     money = int(input("деньги: "))
#     new_customer = Customer(name, age, sex, money)
#     customers.append(new_customer)
#     print(f"Клиент {name} добавлен!\n")

# второй по кол-ву денег кастомер
# customers.sort(key=lambda x: x.money, reverse=True)
# second_richest=customers[1]
# print(second_richest.bio, second_richest.money)

# for i in customers:
#     print(i.bio)
#     for j in cars:
#         if i.get_money()>=j.get_price():
#             print(j, "YES")
#         else:
#             print(j, "NO")

