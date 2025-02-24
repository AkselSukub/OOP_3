#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class Series(ABC):
    """
    Абстрактный базовый класс для прогрессий.
    """

    @abstractmethod
    def __init__(self, a0):
        """
        Конструктор абстрактного класса.
        :param a0: Первый элемент прогрессии.
        """
        self._a0 = a0

    @abstractmethod
    def get_element(self, j):
        """
        Абстрактный метод для вычисления j-го элемента прогрессии.
        :param j: Индекс элемента (начиная с 0).
        :return: Значение j-го элемента.
        """
        pass

    @abstractmethod
    def get_sum(self, n):
        """
        Абстрактный метод для вычисления суммы первых n+1 элементов прогрессии (от 0 до n).
        :param n: Количество элементов для суммирования (сумма до n-го элемента включительно).
        :return: Сумма первых n+1 элементов.
        """
        pass

    @abstractmethod
    def input_data(self):
         """
         Абстрактный метод для ввода данных прогрессии.
         """
         pass

    @abstractmethod
    def output_data(self):
        """
        Абстрактный метод для вывода данных прогрессии.
        """
        pass

    @property
    def a0(self):
        """
        Свойство для доступа к первому элементу прогрессии.
        """
        return self._a0

    @a0.setter
    def a0(self, value):
        """
        Свойство для установки первого элемента прогрессии.
        """
        self._a0 = value


class Linear(Series):
    """
    Класс для арифметической прогрессии.
    """

    def __init__(self, a0, d):
        """
        Конструктор класса.
        :param a0: Первый элемент прогрессии.
        :param d: Разность арифметической прогрессии.
        """
        super().__init__(a0)
        self._d = d

    def get_element(self, j):
        """
        Вычисляет j-й элемент арифметической прогрессии.
        :param j: Индекс элемента.
        :return: Значение j-го элемента.
        """
        return self._a0 + j * self._d

    def get_sum(self, n):
        """
        Вычисляет сумму первых n+1 элементов арифметической прогрессии.
        :param n: Количество элементов для суммирования (сумма до n-го элемента включительно).
        :return: Сумма первых n+1 элементов.
        """
        an = self.get_element(n)
        return (n + 1) * (self._a0 + an) / 2

    def input_data(self):
        """
        Ввод данных для арифметической прогрессии.
        """
        try:
            self._a0 = float(input("Введите первый элемент (a0): "))
            self._d = float(input("Введите разность (d): "))
        except ValueError:
            print("Ошибка: Некорректный ввод. Введите числовые значения.")

    def output_data(self):
        """
        Вывод данных об арифметической прогрессии.
        """
        print("Арифметическая прогрессия:")
        print(f"  a0 = {self._a0}")
        print(f"  d = {self._d}")

    @property
    def d(self):
        """
        Свойство для доступа к разности арифметической прогрессии.
        """
        return self._d

    @d.setter
    def d(self, value):
        """
        Свойство для установки разности арифметической прогрессии.
        """
        self._d = value


class Exponential(Series):
    """
    Класс для геометрической прогрессии.
    """

    def __init__(self, a0, r):
        """
        Конструктор класса.
        :param a0: Первый элемент прогрессии.
        :param r: Знаменатель геометрической прогрессии.
        """
        super().__init__(a0)
        self._r = r

    def get_element(self, j):
        """
        Вычисляет j-й элемент геометрической прогрессии.
        :param j: Индекс элемента.
        :return: Значение j-го элемента.
        """
        return self._a0 * (self._r ** j)

    def get_sum(self, n):
        """
        Вычисляет сумму первых n+1 элементов геометрической прогрессии.
        :param n: Количество элементов для суммирования (сумма до n-го элемента включительно).
        :return: Сумма первых n+1 элементов.
        """
        an = self.get_element(n)
        if self._r == 1:
          return (n + 1) * self._a0
        return (self._a0 - an * self._r) / (1 - self._r)


    def input_data(self):
        """
        Ввод данных для геометрической прогрессии.
        """
        try:
            self._a0 = float(input("Введите первый элемент (a0): "))
            self._r = float(input("Введите знаменатель (r): "))
        except ValueError:
            print("Ошибка: Некорректный ввод. Введите числовые значения.")


    def output_data(self):
        """
        Вывод данных о геометрической прогрессии.
        """
        print("Геометрическая прогрессия:")
        print(f"  a0 = {self._a0}")
        print(f"  r = {self._r}")

    @property
    def r(self):
        """
        Свойство для доступа к знаменателю геометрической прогрессии.
        """
        return self._r

    @r.setter
    def r(self, value):
        """
        Свойство для установки знаменателя геометрической прогрессии.
        """
        self._r = value


def print_series_info(series, n):
    """
    Функция для вывода информации о прогрессии, используя виртуальные вызовы.
    :param series: Объект класса Series (или его потомка).
    :param n: Количество элементов для суммирования.
    """
    print("\nИнформация о прогрессии:")
    series.output_data()  # Виртуальный вызов output_data
    print(f"  {n}-й элемент: {series.get_element(n)}") # Виртуальный вызов get_element
    print(f"  Сумма первых {n+1} элементов: {series.get_sum(n)}") # Виртуальный вызов get_sum


if __name__ == '__main__':
    # Демонстрация работы классов
    linear = Linear(1, 2)
    exponential = Exponential(2, 3)

    # Демонстрация виртуального вызова через функцию print_series_info
    print_series_info(linear, 5)
    print_series_info(exponential, 5)

    # Демонстрация ввода данных
    print("\nВвод данных для арифметической прогрессии:")
    linear.input_data()
    print_series_info(linear, 5)

    print("\nВвод данных для геометрической прогрессии:")
    exponential.input_data()
    print_series_info(exponential, 5)

    # Демонстрация изменения свойств
    linear.a0 = 5
    linear.d = 3
    print("\nАрифметическая прогрессия после изменения a0 и d:")
    print_series_info(linear, 5)

    exponential.a0 = 1
    exponential.r = 2
    print("\nГеометрическая прогрессия после изменения a0 и r:")
    print_series_info(exponential, 5)