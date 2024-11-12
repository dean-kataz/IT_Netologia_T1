# -*- coding: windows-1251 -*-
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    """��������� ������ �� CSV-�����."""
    return pd.read_csv(file_path)

def preprocess_data(data):
    """����������� ������, ���� ��� ���������� (��������, �������������� �����)."""
    # ����� ����� �������� ��� ��� ��������� ������, ���� ��� �����.
    return data

def plot_scatter(data):
    """������� ��������� �������� ����������� �������� ������� �� ��������."""
    fig = px.scatter(data, x='age', y='bill', title='����������� �������� ������� �� ��������')
    fig.show()

def plot_regression(data):
    """������� ����� ��������� � ��������� ���������."""
    plt.figure(figsize=(10, 6))
    sns.regplot(x='age', y='spending', data=data)
    plt.title('����� ��������� ����������� �������� ������� �� ��������')
    plt.show()

def main():
    # ��������� ���� � �����
    file_path = 'DZ7\\web_clients_correct.csv'
    
    # �������� � ��������� ������
    data = load_data(file_path)
    data = preprocess_data(data)
    
    # ������������ ���������� ����� �� 15
    data = data.head(15)

    # ���������� �������
    plot_scatter(data)
    plot_regression(data)

if __name__ == "__main__":
    main()