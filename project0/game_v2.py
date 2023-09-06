""" 'Guess number' game
Computer will uess the number by itself"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Gues the number using random

    Args:
        number (int, optional): Number we need to guess. Defaults to 1.

    Returns:
        int: number of tries
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1,100)
        if number == predict_number:
            break # exiting "while" if computer guessed the number
        
    return(count)

def score_game(random_predict) -> int:
    """Average amount of tries we need to guess the number (we have 1000 nubers to guess)

    Args:
        random_predict (_type_): The guessing function

    Returns:
        int: average amount of tries
    """
    count_lst = []
    np.random.seed(1) # making seed for rewriting the same number
    random_array = np.random.randint(1, 100, size=(1000)) # making a list of number we need to guess

    for number in random_array:
        count_lst.append(random_predict(number))
        
    score = int(np.mean(count_lst))
    print(f"Average amount of tries for algorithm to guess the number - {score}")
    return(score)

if __name__ == '__main__':
    score_game(random_predict)