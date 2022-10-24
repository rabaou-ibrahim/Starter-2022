hauteur = int(input("Taper hauteur "))
left = "/"
right = "\\"
base = "__"

userinput = 10

for i in range(userinput):
    print((userinput -i) * " " + left + ((i * 2 ) * " ") + right)
    if i == userinput - 1:
        print(left + base * userinput + right) 