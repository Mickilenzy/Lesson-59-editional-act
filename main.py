import random
def guess_game():
    print(" Welcome to the Number Guessing Game")
    print("I'm thinking of a number betwen 1 and 10")

    number = random.randint(1,10)

    while True:
        guess = input(" Take a guess")
         
        if not guess.isdigit():
            print(" Please enter a number\n")
            continue

        guess = int(guess)

        if guess < 1 or guess > 10:
            print(" Pick a number from 1 to 10\n")
        elif guess < number:
            print(" Too low! Try again\n")    

        elif guess > number:
            print(" Too high! Try again\n")       

        else: 
            print(" You got it! Great job\n") 

# Start the game
guess_game()                  