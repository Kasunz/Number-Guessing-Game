import random

# Inspired by a tutorial from Geeks-forGeeks: https://www.geeksforgeeks.org/number-guessing-game-in-python/
class NuberGuessingGame:
    def __init__(self, attempts = 7, number_range=(0,100) ):
        self.attempts = attempts
        self.number_range = number_range
        self.number_to_guess = random.randint(*self.number_range)
        self.current_attempts = 0



if __name__ == "__main__":
    game =  NuberGuessingGame()
