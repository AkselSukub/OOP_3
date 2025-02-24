#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Triad:
    """
    Класс, представляющий тройку чисел.
    """

    def __init__(self, a, b, c):
        """
        Конструктор класса.

        :param a: Первое число.
        :param b: Второе число.
        :param c: Третье число.
        """
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        """
        Возвращает строковое представление объекта.

        :return: Строка, представляющая тройку чисел.
        """
        return f"({self.a}, {self.b}, {self.c})"

    def increase_by_one(self):
        """
        Увеличивает каждое число в тройке на 1.
        """
        self.a += 1
        self.b += 1
        self.c += 1


class Date(Triad):
    """
    Класс, представляющий дату (год, месяц, день), наследуется от Triad.
    """

    def __init__(self, year, month, day):
        """
        Конструктор класса.

        :param year: Год.
        :param month: Месяц.
        :param day: День.
        """
        super().__init__(year, month, day)

    def __str__(self):
        """
        Возвращает строковое представление объекта Date.

        :return: Строка, представляющая дату.
        """
        return f"{self.a:04d}-{self.b:02d}-{self.c:02d}"

    def increase_by_one(self):
        """
        Увеличивает год, месяц и день на 1, с учетом допустимых значений.
        """
        self.c += 1  # Сначала увеличиваем день
        self.normalize_date()


    def increase_date_by_n_days(self, n):
        """
        Увеличивает дату на n дней.

        :param n: Количество дней для увеличения.
        """
        self.c += n
        self.normalize_date()

    def is_leap_year(self, year):
        """
        Проверяет, является ли год високосным.

        :param year: Год для проверки.
        :return: True, если год високосный, False в противном случае.
        """
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    def days_in_month(self, year, month):
        """
        Возвращает количество дней в заданном месяце и году.

        :param year: Год.
        :param month: Месяц.
        :return: Количество дней в месяце.
        """
        if month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if self.is_leap_year(year) else 28
        else:
            return 31

    def normalize_date(self):
      """
      Нормализует дату, учитывая количество дней в месяце и високосные годы.
      """
      while self.c > self.days_in_month(self.a, self.b):
          self.c -= self.days_in_month(self.a, self.b)
          self.b += 1
          if self.b > 12:
              self.b = 1
              self.a += 1

if __name__ == '__main__':
    # Демонстрация класса Triad
    triad = Triad(1, 2, 3)
    print("Исходная тройка:", triad)
    triad.increase_by_one()
    print("Тройка после увеличения на 1:", triad)

    # Демонстрация класса Date
    date = Date(2023, 12, 31)
    print("\nИсходная дата:", date)
    date.increase_by_one()
    print("Дата после увеличения на 1 день:", date)

    date.increase_date_by_n_days(30)
    print("Дата после увеличения на 30 дней:", date)

    date2 = Date(2024, 2, 28)
    print("\nИсходная дата:", date2)
    date2.increase_by_one()
    print("Дата после увеличения на 1 день (високосный год):", date2)

    date3 = Date(2023, 1, 1)
    date3.increase_date_by_n_days(365)
    print("\nДата после увеличения на 365 дней:", date3)

    date4 = Date(2024, 1, 1)
    date4.increase_date_by_n_days(365)
    print("Дата после увеличения на 365 дней (високосный год):", date4)