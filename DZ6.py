# -*- coding: windows-1251 -*-
import os 
import pandas as pd

def load_data(file_path):
    """��������� ������ �� CSV �����."""
    return pd.read_csv(file_path)

def analyze_age(df):
    """����������� ������� � ��������� ����� ������� � ������������."""
    def age_category(age):
        return "������ 25" if age > 25 else "������ ��� ����� 25"
    
    df['age_category'] = df['age'].apply(age_category)
    return df

def filter_data(df):
    """�������� ������ �� ��������: ��� - �������, ������� - ������ 30."""
    filtered_df = df[(df['sex'] == 'male') & (df['age'] > 30)]
    return filtered_df

def main():
    # ������� ���� � ������ CSV �����
    file_path = 'DZ6\\web_clients.csv'
    
    # �������� ������
    data = load_data(file_path)
    
    # ������� 1: ������ ��������
    analyzed_data = analyze_age(data)
    print("������ ��������:")
    print(analyzed_data[['age_category']].head(15))  # ������� ������ 15 �����
    
    # ������� 2: ���������� ������
    filtered_data = filter_data(data)
    print("\n��������������� ������ (��� - �������, ������� - ������ 30):")
    print(filtered_data.head(15))  # ������� ������ 15 ����� ��������������� ������

if __name__ == "__main__":
    main()