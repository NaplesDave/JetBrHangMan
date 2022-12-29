import random
# JetBrains Basic Python Course
# Dec 29, 2022
# Hangman Game challenge - SOLUTION stage 8 / FINAL SOlution
# David A. King

win = 0
lost = 0

print("H A N G M A N")
# menu is here
def userMenu():
    global  win, lost

    user_choice = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:').lower()
    if user_choice == "play":
        print()
        game()
    elif user_choice == "results":
        print(f"You won: {win} times.")
        print(f"You lost: {lost} times.")
        userMenu()
    elif user_choice == "exit":
        exit()
    else:
        userMenu()

def game():
    global win, lost
    lives = 8
    words = ["python", "java", "swift", "javascript"]
    word = random.choice(words)
    wordlist = list(word)
    wordlen = len(word)
    guessedltrs = list("-" * wordlen)
    ltrs_in = set()
    print(''.join(guessedltrs))

    while lives > 0:
        guess = input("Input a letter: ")

        if len(guess) > 1 or not guess:
            print("Please, input a single letter.")
            print()
            print(''.join(guessedltrs))
            continue
        elif guess.isalpha() is False or guess.isupper() is True:
            print("Please, enter a lowercase letter from the English alphabet.")
            print()
            print(''.join(guessedltrs))
            continue
        elif guess in ltrs_in:
            print("You've already guessed this letter.")
            print()
            print(''.join(guessedltrs))
            continue

        ltrs_in.add(guess)
        #print(ltrs_in)

        if guess in word:

            print()
            for x in range(wordlen):

                if guess == wordlist[x]:
                    guessedltrs[x] = guess
                    print(''.join(guessedltrs))
                    if "-" not in guessedltrs:
                        print(f"You guessed the word {word}!")
                        print("You survived!")
                        win += 1
                        userMenu()
        else:

            print("That letter doesn't appear in the word.")
            print()
            print(''.join(guessedltrs))
            lives -= 1
            if lives == 0:
                lost += 1
                print("You lost!")
                userMenu()

if __name__ == "__main__":
    userMenu()