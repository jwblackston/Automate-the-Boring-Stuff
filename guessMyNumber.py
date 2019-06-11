#Number guessing game from Al Sweigart's Automate the Boring Stuff in Python:
#It takes your name, your guess, and gives feedback compared to your number
import random
print('Hello, what is your name?')
name = input()

print('Oh, hi' + name 'I am thinking of a number between 1 and 20')
secret_num = random.randint(1, 20)

for guesses_taken in range(1, 7):
    print("Take a guess: ")
    player_guess = int(input())

    if player_guess < secret_num:
        print("Your guess is too low. Guess again, mate.")
    elif player_guess > secret_num:
        print("Your guess is too high. Guess again, mate.")
    else:
        break

if player_guess == secret_num:
    print("Nice!" + name + "You guessed my number in " + guesses_taken "guesses.")
else:
    print("Nope. You exceeded the numbner of guesses taken.")
print("You took" + guesses_taken + "guesses.")
