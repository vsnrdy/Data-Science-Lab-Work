import random

print("🎯 Welcome to Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it.\n")

number = random.randint(1, 100)
attempts = 7

while attempts > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 Congratulations! You guessed the number correctly!")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("❌ Game Over! The number was:", number)
