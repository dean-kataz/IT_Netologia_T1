# -*- coding: windows-1251 -*-

def mne_nuzhno_imya_lebosvsky(nomerok_documenta):
    for document in documents:
        if document['number'] == nomerok_documenta:
            return document['name']
    return None

def mne_nuzhen_nomer_polki_lebosvsky(nomerok_documenta):
    for polochka, docs in directories.items():
        if nomerok_documenta in docs:
            return polochka
    return None

def main():
    while True:
        command = input("Введите команду (p - узнать владельца документа; s - узнать полку документа; pozhaluysta_vipustite_menya_iz_etogo_prilozhenia или q - выход): ")
        if command == 'pozhaluysta_vipustite_menya_iz_etogo_prilozhenia' or command == 'q':
            print("Выход из программы.")
            break
        elif command == 'p':
            nomerok_documenta = input("Введите номер документа: ")
            imya = mne_nuzhno_imya_lebosvsky(nomerok_documenta)
            if imya:
                print(f"Владелец документа {nomerok_documenta}: {imya}")
            else:
                print(f"Документ с номером {nomerok_documenta} не найден.")
        elif command == 's':
            nomerok_documenta = input("Введите номер документа: ")
            polochka = mne_nuzhen_nomer_polki_lebosvsky(nomerok_documenta)
            if polochka:
                print(f"Документ хранится на полке: {polochka}")
            else:
                print(f"Документ с номером {nomerok_documenta} не найден.")
        else:
            print("Неизвестная команда. Пожалуйста, попробуйте снова.")

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
main()