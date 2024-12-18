# -*- coding: windows-1251 -*-
import random

def get_winnings(number):
    if number == 777:
        return 200
    elif number == 999:
        return 100
    elif number == 555:
        return 50
    elif number == 333:
        return 15
    elif number == 111:
        return 10
    elif number == 7:
        return 3
    elif number % 100 == 77: # ��� �����, ��������������� �� 77
        return 5
    elif number % 100 == 0 and number != 0: # ��� �����, ��������������� �� 00, ����� ����
        return 2
    elif number % 10 == 0: # ��� �����, ��������������� �� 0
        return 1
    else:
        return 0

def simulate_lottery(num_games):
    total_winnings = 0
    cost_per_game = 1

    for _ in range(num_games):
        number = random.randint(0, 999)
        winnings = get_winnings(number)
        total_winnings += winnings

    total_cost = num_games * cost_per_game
    net_gain = total_winnings - total_cost
    average_gain = net_gain / num_games

    return total_winnings, total_cost, net_gain, average_gain

# ��������� ��������� �� 10000 �����
num_games = 10000
total_winnings, total_cost, net_gain, average_gain = simulate_lottery(num_games)

print(f"����� �������: {total_winnings} ���.")
print(f"����� �������: {total_cost} ���.")
print(f"������ �������/��������: {net_gain} ���.")
print(f"������� ������� �� ����: {average_gain:.2f} ���.")