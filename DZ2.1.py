# -*- coding: windows-1251 -*-
year = int(input('Введите год: '))
if (year % 4 > 0 and year % 100 == 0) or (year % 400 != 0) > 0:
    print('Обычный год')
else:
    print('Високосный год')