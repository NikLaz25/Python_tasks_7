'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
 для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на практике
работу декоратора @property.'''

'''Первый вариант - простой'''
from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, x):
        self.x = x
    @abstractmethod
    def Result(self):
        self
class Coat(Clothes):
    @ property
    def Result(self):
        a = self.x / 6.5 + 0.5
        print(f' для пальто размером {self.x} потребуется {a} кв.м ткани')

class Suit(Clothes):
    @property
    def Result(self):
        a = self.x * 2 + 0.3
        print(f' для костюма на рост {self.x} м потребуется {a} кв.м ткани')

new_ekz1 = Coat(52)
new_ekz1.Result

new_ekz2 = Suit(1.80)
new_ekz2.Result

'''Второй вариант -   изначально я понял задачу так, что программа должна рассчитывать объём ткани
 для заданного кол-во пальто и костюмов разных размеров. Иначе зачем такая программа,
  когда можно посчитать на калькуляторе? '''
from abc import ABC, abstractmethod

class Clothes:
    def __init__(self):
        self.xx = []

    def __add__(self, other):
        self.xx.append(other)

    @abstractmethod
    def Result(self):
        self
class Coat(Clothes):
    @ property
    def Result(self):
        aa = 0
        for i in self.xx:
            n = int(input(f'Задайте кол-во пальто для размера {i}: '))
            a = (i / 6.5 + 0.5) * n
            aa += round(a, 2)
        return aa

class Suit(Clothes):
    @property
    def Result(self):
        aa = 0
        for i in self.xx:
            n = int(input(f'Задайте кол-во костюмов для роста {i}: '))
            a = (i * 2 + 0.3) * n
            aa += round(a, 2)
        return aa

new_ekz1 = Coat()
new_ekz1 + 52
new_ekz1 + 46
print(f'Для всех пальто необходимо {new_ekz1.Result} кв.м. ткани')

new_ekz2 = Suit()
new_ekz2 + 1.82
new_ekz2 + 1.72
print(f'Для всех костюмов необходимо {new_ekz2.Result} кв.м. ткани')
