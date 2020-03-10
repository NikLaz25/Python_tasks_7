'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
(метод init()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
первой строки первой матрицы складываем с первым элементом первой строки
второй матрицы и т.д.'''
# class Matrix:
#     def __init__(self):
#         self.m1 = []
#         self.m2 = []
#     def __add__(self, other):
#         self.m1.append(other)
#         self.m2.append(other)
#     def __str__(self):
#         # print(self.m1, self.m2)
#         return f'Печать из _str_: {self.m1}, {self.m2}'
# new_ekz1 = Matrix()
# x1 = ((1, 2, 3), (2, 3, 4))
# x2 = ((3, 4, 5), (4, 5, 6))
# new_ekz1 + x1
# new_ekz1 + x2
# print(new_ekz1.m1)
# print(new_ekz1)

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __str__(self):
        return '\n'.join([' '.join([str(i) for i in line]) for line in self.mat])
    def __add__(self, other):
        result = ''
        if len(self.mat) == len(other.mat):
            for line_1, line_2 in zip(self.mat, other.mat):
                if len(line_1) != len(line_2):
                    return 'Неверные данные'
                else:
                    sum_line = [x + y for x, y in zip(line_1, line_2)]
                    result += ' '.join([str(j) for j in sum_line]) +'\n'
        else:
            return 'Неверные данные'
        return result
m1 = [[1, 2, 3], [2, 3, 4]]

m2 = ((3, 4, 5), (4, 5, 6)) # Какие скобки правильные?

new_ekz1 = Matrix(m1)
new_ekz2 = Matrix(m2)
print(new_ekz1.mat)
print(new_ekz2.mat)
print(new_ekz1, '\n')
print(new_ekz2, '\n')
print(new_ekz1 + new_ekz2)

