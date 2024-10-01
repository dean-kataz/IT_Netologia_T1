# -*- coding: windows-1251 -*-

def pairs_rotegoshatal(boys, girls):       
    boys.sort()
    girls.sort()
    pairs = list(zip(boys, girls))
    rukablud = min(len(boys), len(girls))
    print("��������� ����:")
    for boy, girl in pairs:
        print(f"{boy} � {girl}")
    if len(boys) > len(girls):
        rukablud_boy = boys[rukablud:]
        print("\n����� ��� ����:")
        for boy in rukablud_boy:
            print(boy)
    elif len(girls) > len(boys):
        rukablud_girl = girls[rukablud:]
        print("\nø���� ��� ����:")
        for girl in rukablud_girl:
            print(girl)

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
pairs_rotegoshatal(boys, girls)
