import random

while True:  # keeps the game alive
    secretNumber = random.randint(1, 20)

    for guessesTaken in range(1, 7):
        guess = int(input("I'm thinking of a number from 1 to 20: "))

        if guess > secretNumber:
            print("The number you guessed is too high.")
        elif guess < secretNumber:
            print("The number you guessed is too low.")
        else:
            print(f"Congratulations! You guessed it in {guessesTaken} guess(es). The number was {secretNumber}.")
            break  # correct guess, exit the for loop

    if guess != secretNumber:
        print(f"Sorry, the number I was thinking of was {secretNumber}.")

    playAgain = input("Play again? (yes/no): ").lower()
    if playAgain != "yes":
        print("Thanks for playing!")
        break  # exits the while True loop