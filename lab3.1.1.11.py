'''
Write a program that utilizes the concept of conditional execution, takes a string as input, and:

prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
'''

plant = input('Enter the word : ')
if plant == 'Spathiphyllum':
    print('Spathiphyllum is the best plant ever')
elif plant == 'spathiphyllum':
    print('No, i want a big Spathiphylum!')
else:
    print('Spathiphyllum! Not' + plant + 'plant!') 
