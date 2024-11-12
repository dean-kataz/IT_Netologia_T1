# -*- coding: windows-1251 -*-
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    """Загружает данные из CSV-файла."""
    return pd.read_csv(file_path)

def preprocess_data(data):
    """Преобразует данные, если это необходимо (например, преобразование типов)."""
    # Здесь можно добавить код для обработки данных, если это нужно.
    return data

def plot_scatter(data):
    """Создает диаграмму разброса зависимости возраста клиента от расходов."""
    fig = px.scatter(data, x='age', y='bill', title='Зависимость возраста клиента от расходов')
    fig.show()

def plot_regression(data):
    """Создает линию регрессии к диаграмме рассеяния."""
    plt.figure(figsize=(10, 6))
    sns.regplot(x='age', y='spending', data=data)
    plt.title('Линия регрессии зависимости возраста клиента от расходов')
    plt.show()

def main():
    # Указываем путь к файлу
    file_path = 'DZ7\\web_clients_correct.csv'
    
    # Загрузка и обработка данных
    data = load_data(file_path)
    data = preprocess_data(data)
    
    # Ограничиваем количество строк до 15
    data = data.head(15)

    # Выполнение заданий
    plot_scatter(data)
    plot_regression(data)

if __name__ == "__main__":
    main()