import random

# Word lists by difficulty
easy_words = ["duck", "fish", "lion", "yak", "camel", "koala"]
medium_words = ["baboon", "iguana", "monkey", "ostrich", "penguin", "sloth", "tiger", "zebra"]
hard_words = ["aardvark", "elephant", "giraffe", "jellyfish", "quetzal", "rhinoceros", "unicorn", "vulture", "wombat", "xerus"]

# Ask for difficulty

def play_game():
    print("Choose a difficulty level:") 
    print("1. Easy   (shorter words, 8 tries)")
    print("2. Medium (medium words, 6 tries)")
    print("3. Hard   (longer words, 4 tries)")

while True:
    choice = input("Enter 1, 2, or 3: ").strip()
    if choice == "1":
        word_list = easy_words
        max_tries = 8
        break
    elif choice == "2":
        word_list = medium_words
        max_tries = 6
        break
    elif choice == "3":
        word_list = hard_words
        max_tries = 4
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

chosen_word = random.choice(word_list)
guessed_letters = []
tries = 0
display = ['_' for _ in chosen_word]

print(f"\nWelcome to Hangman! You have {max_tries} tries to guess the word.")
print("".join(display))

while True:
    guess = input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single letter (A-Z).")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("".join(display))
    else:
        print("Wrong guess. Try again.\n--------------------------------------")
        tries += 1

    if tries == max_tries:
        print("You lost! The word was", chosen_word)
        break
    if "_" not in display:
        print("You won! The word was", chosen_word)
        break

    print("Guessed letters:", ", ".join(guessed_letters))
    print("Tries left:", max_tries - tries)
    
# Main program with replay option
while True:
    play_game()

    while True:
        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again in ("y", "n"):
            break
        print("Invalid input. Please enter 'y' or 'n'.")

    if play_again == "n":
        print("Thanks for playing! Goodbye.")
        break   