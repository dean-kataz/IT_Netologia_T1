# -*- coding: windows-1251 -*-
year = int(input('������� ���: '))
if (year % 4 > 0 and year % 100 == 0) or (year % 400 != 0) > 0:
    print('������� ���')
else:
    print('���������� ���')