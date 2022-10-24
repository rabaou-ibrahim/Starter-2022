number = int(input("Taper nombre "))


if (number%5 == 0 & number%3 == 0):       #si je mets "(number%15 == 0)" ça marche aussi
        print("FizzBuzz")                 #un multiple de 3 et 5 est un multiple de 15

elif (number%5 == 0):                     #multiple de 5 <=> n'importe quel nombre modulo 5 = 0 
        print("Buzz")
        
elif (number%3 == 0):
        print("Fizz")