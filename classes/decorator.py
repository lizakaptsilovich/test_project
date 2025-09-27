# class Car:
#     def __init__(self, marka, model, power, price):
#         self.marka = marka
#         self.model = model
#         self.power = power
#         self.price = price
#
#     # вызовы через декораторы
#     @property
#     def marka(self):
#         return self.marka
#     @marka.setter
#     def marka(self,marka):
#         self.marka=marka
#
# mers = Car("Mercedes", "E224", 220, 4500)
# bmw = Car("bmw", "s5", 230, 30000)
# audi = Car("audi", "a6", 3000, 50000)
# print(mers.marka) #marka вместо marka()
# mers.marka = 'Brabus' #сразу перезаписывается значение как в сеттере


def decorator_func(f):
    def abc():
        print('text before hello')
        f()
        print('text after hello')
    return abc

def hello():
    print('hello')

hello=decorator_func(hello)
hello()
