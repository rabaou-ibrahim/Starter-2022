from re import I
from secrets import choice

hidden_word = ''
chosen_word = ''
lives = 0

open('dico_france.txt', 'r')

with open('dico_france.txt') as dico_france:
    data = dico_france.readlines()
    word = choice(data)
    word = word[:-1]                            #Pour enlever le retour à la ligne ('\n')
print(word)

for letter in chosen_word:
        hidden_word + '_'
print("Voici le mot à trouver: ")
print(hidden_word)

typed_letter = (input("Taper une lettre: "))
len = len(chosen_word)
i = 0

for i in len:
     if typed_letter == chosen_word[i]:
        hidden_word[i] = typed_letter  
     print(hidden_word)

        
        
