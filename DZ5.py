# -*- coding: windows-1251 -*-
import csv
import json

# ���� � ������
visit_log_path = 'visit_log.csv'
categories_path = 'categories.txt'
funnel_output_path = 'funnel.csv'

# �������� ��������� ������� �� ����� categories.txt
purchase_categories = {}
with open(categories_path, 'r', encoding='utf-8') as categories_file:
    for line in categories_file:
        category_data = json.loads(line.strip())
        user_id = category_data['user_id']
        category = category_data['category']
        purchase_categories[user_id] = category

# �������� ����� visit_log.csv � �������� funnel.csv
with open(visit_log_path, 'r', encoding='utf-8') as visit_log_file:
    with open(funnel_output_path, 'w', encoding='utf-8', newline='') as funnel_file:
        # ������� ������ ��� ������ � CSV
        funnel_writer = csv.writer(funnel_file)
        
        # ���������� ��������� � funnel.csv
        funnel_writer.writerow(['user_id', 'source', 'category'])

        # ������ ���� ���������
        csv_reader = csv.reader(visit_log_file)
        
        # ���������� ��������� visit_log.csv
        next(csv_reader)
        
        for row in csv_reader:
            user_id = row[0]
            source = row[1]
            
            # ���������, ���� �� ��������� ��� ������� user_id
            if user_id in purchase_categories:
                category = purchase_categories[user_id]
                # ���������� ������ � funnel.csv
                funnel_writer.writerow([user_id, source, category])

print("���� funnel.csv ������� ������.")