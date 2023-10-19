"""""
import random
def palabra_Azar():
 num_aleatorio=random.randrange(0,3)
 return num_aleatorio

def replace_word(final_word,palabra_con_signos):

 cont= 0
 while cont != 6:
  for i in final_word:
   letter=str(input("Ingrese la primera letra")).lower()
   letra_encontrada= False  
  if letter in final_word[i]:
   palabra_con_signos[i] = letter
   print(f"Actual palabra{palabra_con_signos}")
   print("la letra esta")
  else:
   cont += 1
   print("la palabra no esta...")
   

words={
 0 :"programacion",
 1 :"computadora",
 2 : "monitor"
}
azar=palabra_Azar()  
final_word = [words.get(azar)]
palabra_con_signos = str(["-"]*len(final_word))

replace_word(final_word,palabra_con_signos)
"""
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

