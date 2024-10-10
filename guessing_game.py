import random

class NuberGuessingGame:
    def __init__(self, attempts = 7, number_range=(0,100) ):
        self.attempts = attempts
        self.number_range = number_range
        self.number_to_guess = random.randint(*self.number_range)
        self.current_attempts = 0
        self.round_number = 1

    def get_user_guess(self):
        """Prompt user for a guess and return the value."""
        while True:
            try:
                guess = int(input(f"\nEnter your guess (between {self.number_range[0]} and {self.number_range[1]}): "))
                return guess
            except ValueError:
                print("Invalid input. Please enter a valid number")

    def check_guess(self, guess):
        """Check if the guess is correct, too high, or too low."""
        if guess == self.number_to_guess:
            print(f'\ncongratulations! you guess the correct number {self.number_to_guess} in {self.current_attempts} attempts!')
            return True
        elif guess > self.number_to_guess:
            print("Your guess is too high!")
        else:
            print("your guess is too low!")
        return False


    def play_game(self):
        """Run the game loop."""
        if self.round_number == 1:
            print("\nWelcome to the Number Guessing Game!")
        else:
            print(f"\nWelcome to round {self.round_number}!")

        while self.current_attempts < self.attempts:
            guess = self.get_user_guess()
            self.current_attempts += 1

            if self.check_guess(guess):
                break

            if self.current_attempts == self.attempts:
                print(f"\nSorry, you've used all {self.attempts} attempts. The correct number was {self.number_to_guess}.")

        self.ask_play_again()

    def ask_play_again(self):
        """Ask the user if they want to play again"""

        while True:
            play_game = input("\nDo you want to play again?(Yes/No): ").strip().lower()
            if play_game in ['yes', 'y']:
                self.reset_game()
                break
            elif play_game in ['no', 'n']:
                print("Thank you playing!")
                break
            else:
                print("Please Enter Yes(Y/y) or No(N/n) !")

    def reset_game(self):
        """Reset the game state for a new round."""
        self.number_to_guess = random.randint(*self.number_range)
        self.current_attempts = 0
        self.play_game()

if __name__ == "__main__":
    game =  NuberGuessingGame()
    game.play_game()

# Inspired by a tutorial from Geeks-forGeeks: https://www.geeksforgeeks.org/number-guessing-game-in-python/