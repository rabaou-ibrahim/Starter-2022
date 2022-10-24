open('data.txt', 'r')

number_of_words = 0

with open('data.txt') as data:
    data = data.read()

    lines = data.split()

    number_of_words = len(lines)

    print(number_of_words)
 


         