import random

#Create a list of words
word_list = ["aardvark", "baboon", "camel", "duck", "elephant", "fish", "giraffe", "hippo", "iguana", "jellyfish", "koala", "lion", "monkey", "ostrich", "penguin", "quetzal", "rhinoceros", "sloth", "tiger", "unicorn", "vulture", "wombat", "xerus", "yak", "zebra"]

#Chose a random word
chosen_word = random.choice(word_list)
guessed_letters = []
tries = 0

#Display as underscores
display = [ '_' for _ in chosen_word]

print("Welcome to Hangman! You have 6 tries to guess the word.")
print ("".join(display))

#Main game loop
while True:
    guess = input("Guess a letter: ").lower()
    guessed_letters.append(guess)
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("".join(display))
    else:
        print("Wrong guess. Try again.\n--------------------------------------")
        tries += 1
    if tries == 6:
        print("You lost! The word was", chosen_word)
        break
    if "_" not in display:
        print("You won! The word was", chosen_word)
        break
    
    #Validations
    while True:
        guess = input("\nGuess a letter: ").lower()
        if not guess.isalpha():
            print("Invalid input. Please enter a letter (A-Z).")
        continue
        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        break   

    #End of game
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Tries left:", 6 - tries)
    
