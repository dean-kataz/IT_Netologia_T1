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
        command = input("������� ������� (p - ������ ��������� ���������; s - ������ ����� ���������; pozhaluysta_vipustite_menya_iz_etogo_prilozhenia ��� q - �����): ")
        if command == 'pozhaluysta_vipustite_menya_iz_etogo_prilozhenia' or command == 'q':
            print("����� �� ���������.")
            break
        elif command == 'p':
            nomerok_documenta = input("������� ����� ���������: ")
            imya = mne_nuzhno_imya_lebosvsky(nomerok_documenta)
            if imya:
                print(f"�������� ��������� {nomerok_documenta}: {imya}")
            else:
                print(f"�������� � ������� {nomerok_documenta} �� ������.")
        elif command == 's':
            nomerok_documenta = input("������� ����� ���������: ")
            polochka = mne_nuzhen_nomer_polki_lebosvsky(nomerok_documenta)
            if polochka:
                print(f"�������� �������� �� �����: {polochka}")
            else:
                print(f"�������� � ������� {nomerok_documenta} �� ������.")
        else:
            print("����������� �������. ����������, ���������� �����.")

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': '������� ������'},
    {'type': 'invoice', 'number': '11-2', 'name': '�������� ���������'},
    {'type': 'insurance', 'number': '10006', 'name': '�������� ������'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
main()