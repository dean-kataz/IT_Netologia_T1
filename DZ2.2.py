# -*- coding: windows-1251 -*-

sum1 = 0
sum2 = 0
ticket = input('������� ����� ������ (6 ����): ')
sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if sum1 == sum2:
    print('���������� �����')
else:
    print('������������ �����')