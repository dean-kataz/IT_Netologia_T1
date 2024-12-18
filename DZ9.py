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
    elif number % 100 == 77: # Все числа, заканчивающиеся на 77
        return 5
    elif number % 100 == 0 and number != 0: # Все числа, заканчивающиеся на 00, кроме нуля
        return 2
    elif number % 10 == 0: # Все числа, заканчивающиеся на 0
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

# Запускаем симуляцию на 10000 играх
num_games = 10000
total_winnings, total_cost, net_gain, average_gain = simulate_lottery(num_games)

print(f"Общий выигрыш: {total_winnings} руб.")
print(f"Общие затраты: {total_cost} руб.")
print(f"Чистый выигрыш/проигрыш: {net_gain} руб.")
print(f"Средний выигрыш за игру: {average_gain:.2f} руб.")