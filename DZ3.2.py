# -*- coding: windows-1251 -*-

def pairs_rotegoshatal(boys, girls):       
    boys.sort()
    girls.sort()
    pairs = list(zip(boys, girls))
    rukablud = min(len(boys), len(girls))
    print("Идеальные пары:")
    for boy, girl in pairs:
        print(f"{boy} и {girl}")
    if len(boys) > len(girls):
        rukablud_boy = boys[rukablud:]
        print("\nБойсы без пары:")
        for boy in rukablud_boy:
            print(boy)
    elif len(girls) > len(boys):
        rukablud_girl = girls[rukablud:]
        print("\nГёрлсы без пары:")
        for girl in rukablud_girl:
            print(girl)

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
pairs_rotegoshatal(boys, girls)
