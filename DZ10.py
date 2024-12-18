# -*- coding: windows-1251 -*-
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm
from scipy.stats import pearsonr, spearmanr

# �������� ������
data = pd.read_csv('water.csv')

plt.figure(figsize=(10, 6))
sns.scatterplot(x='hardness', y='mortality', data=data)
plt.title('�������� ������: Ƹ������� ���� vs ������� ������� ����������')
plt.xlabel('Ƹ������� ���� (mg/L)')
plt.ylabel('������� ������� ���������� (����� �������)')
plt.grid()
plt.show()

# ����������� ���������� �������
pearson_corr, _ = pearsonr(data['hardness'], data['mortality'])
print(f'����������� ���������� �������: {pearson_corr:.3f}')

# ����������� ���������� ��������
spearman_corr, _ = spearmanr(data['hardness'], data['mortality'])
print(f'����������� ���������� ��������: {spearman_corr:.3f}')

X = sm.add_constant(data['hardness'])  # ��������� ��������� ��� ���������� �����
model = sm.OLS(data['mortality'], X).fit()
print(model.summary())

residuals = model.resid

plt.figure(figsize=(10, 6))
plt.scatter(model.fittedvalues, residuals)
plt.axhline(0, color='red', linestyle='--')
plt.title('������ ��������')
plt.xlabel('������������� �������� ����������')
plt.ylabel('�������')
plt.grid()
plt.show()

north_data = data[data['location'] == 'North']
south_data = data[data['location'] == 'South']

plt.figure(figsize=(10, 6))
sns.scatterplot(x='hardness', y='mortality', data=north_data)
plt.title('�������� ������: Ƹ������� ���� vs ������� ������� ����������')
plt.xlabel('Ƹ������� ���� (mg/L)')
plt.ylabel('������� ������� ���������� (����� �������)')
plt.grid()
plt.show()

pearson_corr_north, _ = pearsonr(north_data['hardness'], north_data['mortality'])
spearman_corr_north, _ = spearmanr(north_data['hardness'], north_data['mortality'])
print(f'�������� ������ - ����������� ���������� �������: {pearson_corr_north:.3f}')
print(f'�������� ������ - ����������� ���������� ��������: {spearman_corr_north:.3f}')

X_north = sm.add_constant(north_data['hardness'])
model_north = sm.OLS(north_data['mortality'], X_north).fit()
print(model_north.summary())

residuals_north = model_north.resid

plt.figure(figsize=(10, 6))
plt.scatter(model_north.fittedvalues, residuals_north)
plt.axhline(0, color='red', linestyle='--')
plt.title('������ �������� ��� �������� �������')
plt.xlabel('������������� �������� ����������')
plt.ylabel('�������')
plt.grid()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='hardness', y='mortality', data=south_data)
plt.title('����� ������: Ƹ������� ���� vs ������� ������� ����������')
plt.xlabel('Ƹ������� ���� (mg/L)')
plt.ylabel('������� ������� ���������� (����� �������)')
plt.grid()
plt.show()

pearson_corr_south, _ = pearsonr(south_data['hardness'], south_data['mortality'])
spearman_corr_south, _ = spearmanr(south_data['hardness'], south_data['mortality'])
print(f'����� ������ - ����������� ���������� �������: {pearson_corr_south:.3f}')
print(f'����� ������ - ����������� ���������� ��������: {spearman_corr_south:.3f}')

X_south = sm.add_constant(south_data['hardness'])
model_south = sm.OLS(south_data['mortality'], X_south).fit()
print(model_south.summary())

residuals_south = model_south.resid

plt.figure(figsize=(10, 6))
plt.scatter(model_south.fittedvalues, residuals_south)
plt.axhline(0, color='red', linestyle='--')
plt.title('������ �������� ��� ����� �������')
plt.xlabel('������������� �������� ����������')
plt.ylabel('�������')
plt.grid()
plt.show()