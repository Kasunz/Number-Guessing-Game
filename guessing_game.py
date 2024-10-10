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
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number")

    # Check if the guess is correct, too high, or too low.
    def check_guess(self, guess):
        if guess == self.number_to_guess:
            print(f'congratulations! you guess the correct number {self.number_to_guess} in {self.current_attempts} attempts!')
            return True
        elif guess > self.number_to_guess:
            print("Your guess is too high!")
        else:
            print("your guess is too low!")
        return False

    # Run the main loop and print outputs
    def play_game(self, guess):
        print("Welcome to the Number Guessing Game!")


        while self.current_attempts < self.attempts:
            guess = self.get_user_guess()

            if self.check_guess(guess):
                break

            if self.current_attempts == self.attempts:
                print(f"Sorry, you've used all {self.attempts} attempts. The correct number was {self.number_to_guess}.")


    def ask_play_again(self):
        pass

    def reset_game(self):
        pass


if __name__ == "__main__":
    game =  NuberGuessingGame()
