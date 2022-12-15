import random
import numpy


def roll_dice(sides: int, tries: int = 1, adv: bool = False) -> float:
    rolls = []
    for i in range(tries):
        res = random.randrange(1, sides + 1)
        if adv:
            res = max(random.randrange(1, sides + 1), res)
        rolls.append(res)

    # return numpy.mean(rolls)
    return sum(rolls) / len(rolls)


print("without :", roll_dice(20, 1000000))
print("with :", roll_dice(20, 1000000, True))
