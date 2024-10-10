import random

# Inspired by a tutorial from Geeks-forGeeks: https://www.geeksforgeeks.org/number-guessing-game-in-python/
class NuberGuessingGame:
    def __init__(self, attempts = 7, number_range=(0,100) ):
        self.attempts = attempts
        self.number_range = number_range
        self.number_to_guess = random.randint(*self.number_range)
        self.current_attempts = 0

    def get_user_guess(self):
        while True:
            try:
                guess = int(input(f"\nEnter your guess (between {self.number_range[0] and self.number_range[1]}: "))

                # Check if guess is within the range
                if guess != self.number_range[0] and self.number_range[0]:
                    print(f"Please enter a number between {self.number_range[0] and self.number_range[1]} ")
                else:
                    # increment guess count if valid
                    self.current_attempts += 1
                    print(f"Attempt {self.current_attempts} / {self.attempts}")
                    return guess
            except ValueError:
                print("Invalid input. Please enter a valid number")





if __name__ == "__main__":
    game =  NuberGuessingGame()
