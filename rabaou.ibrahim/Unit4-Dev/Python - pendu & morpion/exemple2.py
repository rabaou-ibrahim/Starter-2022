from secrets import choice


hidden_word = ''
chosen_word = ''
lives = 10

open('dico_france.txt', 'r')

with open('dico_france.txt') as dico_france:
    data = dico_france.readlines()
    chosen_word = choice(data)
    chosen_word = chosen_word[:-1]                            #Pour enlever le retour à la ligne ('\n')
print(chosen_word)

len = len(chosen_word)
i = 0

def guess_letter():

    print("Voici le mot à trouver: ")

for letter in chosen_word:
    hidden_word = hidden_word + '_'
print(hidden_word)

while hidden_word != chosen_word:
    typed_letter = (input("Taper une lettre: "))
    for i in range(0,len):
        if typed_letter == chosen_word[i]:
            hidden_word = hidden_word[:i] + typed_letter + hidden_word[i:]
            hidden_word = hidden_word[-1]
    print("Bien joué !") 
    print(hidden_word)
    for i in range(0,len):
        if typed_letter == chosen_word[i]:
            hidden_word = hidden_word[:i] + typed_letter + hidden_word[:i]    

guess_letter()