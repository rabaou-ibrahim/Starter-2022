largeur = int(input("Taper largeur "))
hauteur = int(input("Taper hauteur "))

for j in range(0,hauteur):
    print("|", end = '')
    if j == 0 or j == hauteur -1:
        for i in range(0,largeur):
            print("-", end = '')
    else: 
        for i in range(0,largeur):
            print(" ", end = '')
           
    print('|')

