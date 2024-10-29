# -*- coding: windows-1251 -*-
import os 
import pandas as pd

def load_data(file_path):
    """Загружает данные из CSV файла."""
    return pd.read_csv(file_path)

def analyze_age(df):
    """Анализирует возраст и добавляет новый столбец с результатами."""
    def age_category(age):
        return "Старше 25" if age > 25 else "Младше или равен 25"
    
    df['age_category'] = df['age'].apply(age_category)
    return df

def filter_data(df):
    """Отбирает данные по условиям: пол - мужской, возраст - больше 30."""
    filtered_df = df[(df['sex'] == 'male') & (df['age'] > 30)]
    return filtered_df

def main():
    # Укажите путь к вашему CSV файлу
    file_path = 'DZ6\\web_clients.csv'
    
    # Загрузка данных
    data = load_data(file_path)
    
    # Задание 1: Анализ возраста
    analyzed_data = analyze_age(data)
    print("Анализ возраста:")
    print(analyzed_data[['age_category']].head(15))  # Выводим первые 15 строк
    
    # Задание 2: Фильтрация данных
    filtered_data = filter_data(data)
    print("\nОтфильтрованные данные (пол - мужской, возраст - больше 30):")
    print(filtered_data.head(15))  # Выводим первые 15 строк отфильтрованных данных

if __name__ == "__main__":
    main()