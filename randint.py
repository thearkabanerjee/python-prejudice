# this code is supposed to generate a random number betweeen 1 and 10

import numpy as np

# first we are importing the numpy library
a = np.random.randint(1,6)
# what the function does is generating a random number between 1 and 6

b = np.random.randint(1,7, 10)
# generates a random number between 1 and 6 again but this time, we are asking for 10 guesses 

print("the die roll guess is ", a)

print ("the probable die roll guesses are",b)

