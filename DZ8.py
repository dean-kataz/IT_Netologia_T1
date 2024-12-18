# -*- coding: windows-1251 -*-

import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/obulygin/pyda_homeworks/master/statistics_basics/horse_data.csv')
print(data.head())

columns = ['age', 'weight', 'height', 'temp', 'pulse', 'respiration', 'surgery', 'outcome']
for column in columns:
    print(f'�������: {column}')
    print(f'�������: {data[column].median()}')
    print(f'����: {data[column].mode()[0]}')
    print(f'������� ��������: {data[column].mean()}')
    print(f'����������� ��������: {data[column].min()}')
    print(f'������������ ��������: {data[column].max()}')
    print('-------------------------')

for column in ['age', 'weight', 'height', 'temp', 'pulse', 'respiration']:
    q1 = data[column].quantile(0.25)
    q3 = data[column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = data[(data[column] < lower_bound) | (data[column] > upper_bound)]
    print(f'�������: {column}')
    print(f'���������� ��������: {len(outliers)}')
    print('-------------------------')

missing_values = data.isnull().sum()
print(missing_values)

data.fillna(data.mean(), inplace=True)

data.dropna(inplace=True)