# -*- coding: windows-1251 -*-
import csv
import json

# Путь к файлам
visit_log_path = 'visit_log.csv'
categories_path = 'categories.txt'
funnel_output_path = 'funnel.csv'

# Загрузка категорий покупок из файла categories.txt
purchase_categories = {}
with open(categories_path, 'r', encoding='utf-8') as categories_file:
    for line in categories_file:
        category_data = json.loads(line.strip())
        user_id = category_data['user_id']
        category = category_data['category']
        purchase_categories[user_id] = category

# Открытие файла visit_log.csv и создание funnel.csv
with open(visit_log_path, 'r', encoding='utf-8') as visit_log_file:
    with open(funnel_output_path, 'w', encoding='utf-8', newline='') as funnel_file:
        # Создаем объект для записи в CSV
        funnel_writer = csv.writer(funnel_file)
        
        # Записываем заголовок в funnel.csv
        funnel_writer.writerow(['user_id', 'source', 'category'])

        # Читаем файл построчно
        csv_reader = csv.reader(visit_log_file)
        
        # Пропускаем заголовок visit_log.csv
        next(csv_reader)
        
        for row in csv_reader:
            user_id = row[0]
            source = row[1]
            
            # Проверяем, есть ли категория для данного user_id
            if user_id in purchase_categories:
                category = purchase_categories[user_id]
                # Записываем данные в funnel.csv
                funnel_writer.writerow([user_id, source, category])

print("Файл funnel.csv успешно создан.")