import numpy as np

dice_rolls = np.random.randint(1, 7, 10000)

probability_of_six = np.sum(dice_rolls == 6) / 10000

print(probability_of_six)
