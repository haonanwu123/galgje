import getpass


def choose_word():
    word = getpass.getpass(
        "Player 1, please enter a word:"
    )  # No effect in environments like Jupyter Notebook
    return word.lower()


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def Galgje():
    print("Welcome to the word guessing game!")

    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_guesses = 0

    while True:
        current_display_word = display_word(word_to_guess, guessed_letters)
        print("\nword:", current_display_word)
        guess = input("Player 2, please guess a letter:").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed this letter, please try other letters.")
            continue

        guessed_letters.append(guess)

        current_display_word = display_word(word_to_guess, guessed_letters)

        if "_" not in current_display_word:
            print(
                "Congratulations! You guessed the entire word. The correct word is:",
                word_to_guess,
            )
            break
        elif guess in word_to_guess:
            print("Guessed it!")
        else:
            print("Guessed wrong!")
            incorrect_guesses += 1

        if incorrect_guesses == 9:
            print(
                "Sorry, you have guessed wrong 9 times in a row. The game is over. The correct word is:",
                word_to_guess,
            )
            break


if __name__ == "__main__":
    Galgje()
