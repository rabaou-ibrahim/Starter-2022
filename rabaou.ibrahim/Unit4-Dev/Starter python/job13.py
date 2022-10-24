from dataclasses import dataclass


int_number = int(input("Taper nombre entier: "))
number_words = 0

open('data.txt', 'r')

with open('data.txt','r') as data:
    
    data = data.read()
    
    lines = data.split()

    lines = lines.split(" ")

    for word in lines:
        #on vérifie si la longueur de chaque mot est égale à l'input
        if len(word) == int_number:
            number_words+=1           #si oui, on ajoute 1 à int_number

print(number_words)
