#write functions here, don't add input('') statements here!
import random

def get_random_number():
    return random.randint(1, 5)

while True:
    random_guess = get_random_number()
    print("guessing game!")
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 5 (or 0 to quit): "))
            if guess == 0:
                print("GOODBYE")
                exit()
            elif guess == random_guess:
                print("You guessed correctly.")
                break
            else:
                print("Try another number")
        except ValueError:
            print("Error: Please enter a valid number.")