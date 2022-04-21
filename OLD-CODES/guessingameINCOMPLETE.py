from random import randint

guessNumber = 0
numberOfGuesses = 0

#get the random number
randomNumber = randint(0, 20)

print("\nThis ia guessing game")
print("\nI have already chosen a number between 1 to 20")
print("\nYou must guess the number now!")

guessNumber = int (input("\nEnter your guess"))

if guessNumber < 0 or guessNumber > 20:
    print("\nYou must enter the number between 1 to 20")

else:
    if guessNumber == randomNumber:
        print("\nYou have won")           
    elif guessNumber < randomNumber:
        print("\nMy guess is greater than that")
    elif guessNumber > randomNumber:
        print("\nMy guess is less than that")
