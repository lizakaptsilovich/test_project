# class Car:
#     marka: Marka
#     model: Model
#     price: Price
#     def __init__(self, marka, model, price):
#         self.__marka=marka
#         self.__model=model
#         self.__price=price
# #композиция - когда поля являются аттрибутами других классов (марка - Марка)
# mers=Car(Marka(), Model(), Price())
from abc import abstractmethod


class Figure:
    """документирование для класса, будет отображаться в магическом методе doc"""
    @abstractmethod
    def square(self, a,b):
        pass
class Tr(Figure):

    def Tr(self, a, b):
        """документирование для функции"""
        return a*b/2
tr=Tr()