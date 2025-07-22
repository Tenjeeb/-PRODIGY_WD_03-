import random

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1,100)
    attempts = 0

    print ("*** Welcome to the Number Guessing Game! ***")
    print (" *** I am thinking of a number between 1 and 100. ***")

    while True:
        try:
            # Get user's guessed number
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print (f"Congratulations! You guess the number {secret_number} correctly.")
                print (f"It took you {attempts} attempts.")
                break
        except ValueError:
            print ("Please enter a valid integer.")

# Run the program
guess_the_number()
