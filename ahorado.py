
import random
from funciones_ahorcado import *

words = {
    0: "programacion",
    1: "computadora",
    2: "monitor"
}

# Get a random word
random_word_index = random.randint(0, len(words) - 1)
final_word = list(words[random_word_index])

# Create a list of dashes to represent the word
word_with_dashes = ["-"] * len(final_word)

# Replace the word with dashes using the replace_word function
replace_word(final_word, word_with_dashes)

