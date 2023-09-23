""" 'Guess number' game
Computer will uess the number by itself"""

import numpy as np

def half_cut_predict(number:int=1) -> int:
    """Guessing the number going closer to it with each iteration
    For example:
    We need to guess number 30, we keep jumping from our current number
    in direction of the number we need to guess.
    For this example our way will be: 50 - 25 - 37 - 31 - 28 - 29 - 30
    
    Args:
        number (int, optional): Number we need to guess. Defaults to 1.

    Returns:
        int: number of tries
    """
    count = 0
    number = 30
    Current_num = 50
    Right_Border = 100
    Left_Border = 1
    
    while True:
        if Current_num < number:
            Left_Border = Current_num
            Current_num = (Right_Border + Left_Border) // 2
            count += 1
        elif Current_num > number:
            Right_Border = Current_num
            Current_num = (Right_Border + Left_Border) // 2
            count += 1
        else:
            return(count)
    
    

def score_game(half_cut_predict) -> int:
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
        count_lst.append(half_cut_predict(number))
        
    score = int(np.mean(count_lst))
    print(f"Average amount of tries for algorithm to guess the number - {score}")
    
    return(score)

if __name__ == '__main__':
    score_game(half_cut_predict)