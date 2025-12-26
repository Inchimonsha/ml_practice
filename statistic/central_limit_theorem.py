# population distribution: normal: M = 0, сигма = 20 | n - кол-во вычислений / xi(mean) ... xn(mean)
# Sampling distribution: (стандартное отклонение) стандартная ошибка среднего:
# se = сигма / sqrt(n) = sdx / sqrt(n)
# n > 30

from random import randint
import matplotlib.pyplot as plt

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def throw(self, number_of_throws=100, number_of_dices=10):
        dice_values = [0] * number_of_throws
        for i in range(number_of_throws):
            for j in range(number_of_dices):
                dice_values[i] += randint(1, self.sides)
        values_range = range(min(dice_values), max(dice_values)+1)
        return {i: dice_values.count(i) for i in values_range}


def gist_plot(data):
    sort = sorted(data)
    y = tuple(data[i] for i in sort)
    x = range(sort[0], sort[-1]+1)
    ax = plt.gca()
    ax.bar(x, y, align='center')
    ax.set_xticks(x)
    ax.set_xticklabels(x)
    plt.show()

dice = Dice()
gist_plot(dice.throw())