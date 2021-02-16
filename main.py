#The Number Guessing Game
from random import randint

logo = """ 
 $$$$$$\                                          $$\                            $$$$$$\                                    
$$  __$$\                                         \__|                          $$  __$$\                                   
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\ $$\ $$$$$$$\   $$$$$$\        $$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|$$ |$$  __$$\ $$  __$$\       $$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ 
$$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\  $$ |$$ |  $$ |$$ /  $$ |      $$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\ $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |      \$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ 
 \______/  \______/  \_______|\_______/ \_______/ \__|\__|  \__| \____$$ |       \______/  \_______|\__| \__| \__| \_______|
                                                                $$\   $$ |                                                  
                                                                \$$$$$$  |                                                  
                                                                 \______/                                                   
"""

EASY_DIFFICULTY = 10
HARD_DIFFICULTY = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too High!")
        return turns -1
    elif guess < answer:
        print("Too Low!")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}")

def set_difficulty():
    choosing_difficulty = input("Choose difficulty. Type 'easy' or 'hard'.")
    if choosing_difficulty == "easy":
        return EASY_DIFFICULTY
    else:
        return HARD_DIFFICULTY

def game():
    print (logo)
    print("Welcome to The Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    answer = randint (1,100)

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print (f"You have {turns} attempts remaining to guess the number!")

        guess = int(input("Guess a number: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You have run out of guesses. You lose!")
            print (f"The answer was {answer}")
            return
        elif guess != answer:
            print("Guess again!")

game()