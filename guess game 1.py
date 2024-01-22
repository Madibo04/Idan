import random

def guess_the_number():
    print("Set the lower limit and the upper limit")
    
    # Set the range for the random number
    lower_limit = int(input())
    upper_limit = int(input())
    target_number = random.randint(lower_limit, upper_limit)
    
    attempts = 0

    while True:
        user_guess = int(input(f"Guess the number between {lower_limit} and {upper_limit}: "))
        attempts += 1

        if user_guess == target_number:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            break
        elif user_guess < target_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

# Example usage:
guess_the_number()
