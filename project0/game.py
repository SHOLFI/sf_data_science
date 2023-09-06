"""Guess number game"""

import numpy as np

number = np.random.randint(1, 101) # we make a number

# number of tries
count = 0

while True:
    count+=1
    predict_number = int(input("Choose number from 1 to 100\n"))
    
    if predict_number > number:
        print("Wrong! Number is smaller")
    elif predict_number < number:
        print("Wrong! Number is bigger")
    else:
        print(f"You guessed the number. Number - {number} guessed in {count} tries ")
        break #end of the game. Exiting "while"        
        