from ast import Try
from secrets import choice

hidden_word = ''
chosen_word = ''
data = ''
len = len(chosen_word)
i = 0


def beginner_mode():
    global len
    global i
    global hidden_word
    global chosen_word
    lives = 10
    
    print("Vous avez choisi le niveau débutant, vous avez donc droit à 10 vies.\n")

    open('dico_france.txt', 'r')
    
    with open('dico_france.txt') as dico_france:
        data = dico_france.readlines()
        chosen_word = choice(data)
        chosen_word = chosen_word[:-1]                            #Pour enlever le retour à la ligne ('\n')
    print("Voici le mot à trouver: ")
    
    for letter in chosen_word:
        hidden_word = hidden_word + '_'
    print(hidden_word)
    
    while hidden_word != chosen_word:                       #Ce code fonctionne uniquement si on n'a pas deux fois la même lettre dans un mot
        typed_letter = str(input("Tapez une lettre: "))
        for i in range(0,len):
            if typed_letter == chosen_word[i]:
                hidden_word = hidden_word[:i] + typed_letter + hidden_word[i:]
                hidden_word = hidden_word[:-1]
        print("Bien joué !")
        print(hidden_word)
  
    print("Bravo !")
           

def intermediate_mode():
    global len
    global i
    global hidden_word
    global chosen_word
    lives = 10
    
    print("Vous avez choisi le niveau débutant, vous avez donc droit à 10 vies.\n")

    open('dico_france.txt', 'r')
    
    with open('dico_france.txt') as dico_france:
        data = dico_france.readlines()
        chosen_word = choice(data)
        chosen_word = chosen_word[:-1]                            #Pour enlever le retour à la ligne ('\n')
    print("Voici le mot à trouver: ")
    
    for letter in chosen_word:
        hidden_word = hidden_word + '_'
    print(hidden_word)
    
    while hidden_word != chosen_word:                       #Ce code fonctionne uniquement si on n'a pas deux fois la même lettre dans un mot
        typed_letter = str(input("Tapez une lettre: "))
        for i in range(0,len):
            if typed_letter == chosen_word[i]:
                hidden_word = hidden_word[:i] + typed_letter + hidden_word[i:]
                hidden_word = hidden_word[:-1]
        print("Bien joué !")
        print(hidden_word)
  
    print("Bravo !")

def expert_mode():
    global len
    global i
    global hidden_word
    global chosen_word
    lives = 10
    
    print("Vous avez choisi le niveau débutant, vous avez donc droit à 10 vies.\n")

    open('dico_france.txt', 'r')
    
    with open('dico_france.txt') as dico_france:
        data = dico_france.readlines()
        chosen_word = choice(data)
        chosen_word = chosen_word[:-1]                            #Pour enlever le retour à la ligne ('\n')
    print("Voici le mot à trouver: ")
    
    for letter in chosen_word:
        hidden_word = hidden_word + '_'
    print(hidden_word)
    
    while hidden_word != chosen_word:                       #Ce code fonctionne uniquement si on n'a pas deux fois la même lettre dans un mot
        typed_letter = str(input("Tapez une lettre: "))
        for i in range(0,len):
            if typed_letter == chosen_word[i]:
                hidden_word = hidden_word[:i] + typed_letter + hidden_word[i:]
                hidden_word = hidden_word[:-1]
        print("Bien joué !")
  
    print("Bravo !")


def error_pick():   

    picked_level = str(input("Choisissez votre niveau: "))
    if picked_level != "Débutant" or "Intermédiaire" or "Expert":
        print("Veuillez taper correctement le niveau que vous souhaitez choisir (Débutant, Intermédiaire ou Expert.)")

def proceed():

    proceed = input("Appuyez sur une touche puis -Entrée- pour poursuivre: \n")

def display_Lets_Go():

    print("C'est parti !\n")


def Display_Lives():

    lives = 0
    print("Il vous reste", lives,  "vies")

def game_start():

    hidden_word = ''
    chosen_word = ''
    data = ''

    print(" BIENVENUE :D ")
    print("Dans ce jeu 3 niveaux sont disponibles: Débutant, Intermédiaire, Expert")

    picked_level = str(input("Choisissez votre niveau: "))
    if picked_level == "Débutant":
        beginner_mode()
    elif picked_level == "Intermédiaire":
        intermediate_mode()
    elif picked_level == "Expert":
        expert_mode()

game_start()

