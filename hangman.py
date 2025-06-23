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

