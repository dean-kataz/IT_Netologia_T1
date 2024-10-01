# -*- coding: windows-1251 -*-

word = input('Введите слово: ')
temp_1 = len(word)
temp_2 = temp_1 / 2
if temp_1 % 2 > 0:
    print(word[int(temp_2)])
else:
    print(word[int(temp_2)], word[int(temp_2) - 1])