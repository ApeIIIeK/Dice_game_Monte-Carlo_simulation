import matplotlib.pyplot as plt
import random

def roll_dice():
    die_1 = random.randint(1,6)
    die_2 = random.randint(1,6)
    
    if die_1 == die_2:
        same_num = True
    else:
        same_num = False
    return same_num

num_simulation = 10000

max_num_rolls = 1000

bet = 1

win_probability = []
end_balance = []

fig = plt.figure()

plt.title("Игра в кости моделирование методом Монте-Карло [" + str(num_simulation) + " simulation]")

plt.xlabel("Номер броска")
plt.ylabel(" Баланс баллов")
plt.xlim([0, max_num_rolls])

for i in range(num_simulation):
    balance = [1000]
    num_rolls = [0]
    num_wins = 0
    while num_rolls[-1] < max_num_rolls:
        same = roll_dice()
        
        if same:
            balance.append(balance[-1] + 4 * bet)
            num_wins += 1
        else:
            balance.append(balance[-1] - bet)
        num_rolls.append(num_rolls[-1] + 1)
    win_probability.append(num_wins/num_rolls[-1])
    end_balance.append(balance[-1])
    plt.plot(num_rolls, balance)
    
plt.show()

overall_win_probability = sum(win_probability)/len(win_probability)
overall_end_balance = sum(end_balance)/len(end_balance)

print("Средняя вероятность выигрышей после " + str(num_simulation) + " розыгрышей " + str(overall_win_probability))

print("Средний конечный баланс после " + str(num_simulation) + " розыгрышей: " + str(overall_end_balance))
