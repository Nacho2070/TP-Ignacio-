import random

def random_Word():
    random_number = random.randrange(0, 3)  
    return random_number

def replace_word(final_word,  word_with_dashes):
    attemps = 0
    incorrect_letters=[]   
    while attemps != 6:  # we limit to 6 attempts
        letter = str(input("Ingrese una letra: ")).lower()
        letter_found = False
    #the word is searched for the letter entered
        for i in range(len(final_word)):
           if letter == final_word[i]:
                word_with_dashes[i] = letter
                letter_found = True
                print(f"Palabra actual: {' '.join(word_with_dashes)}")
    #if not found we show the entered letters
        if not letter_found:
            attemps += 1
            incorrect_letters.append(letter)
            print("La letra no está en la palabra.")
            print("Las letras incorrectas son: " + ' '.join(incorrect_letters))
        
        if ''.join( word_with_dashes) == ''.join(final_word):
            print("¡Has adivinado la palabra!")
            break
    
        if attemps == 6:
           print("Has alcanzado el límite de intentos. La palabra era:",final_word)
           break
