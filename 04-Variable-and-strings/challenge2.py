import math

"""
QUESTION 1: Ask the user for the radius of a circle and the print the area
"""
radius = float(input('Radius: '))
area = math.pi*(radius**2)
print(f'Area: {area}')

"""
QUESTION 2: Convert fahrenheit to celsius
"""
fahrenheit = float(input('Temperature in Fahrenheit: '))
celsius = ((fahrenheit-32)*5)/9
print(f'Temperature in Celsius: {celsius}')

"""
QUESTION 3: Obtain the product of two integers
"""
number_1 = int(input('Number 1: '))
number_2 = int(input('Number 2: '))
print(f'\nProduct: {number_1*number_2}')

"""
QUESTION 4: Bob, Ann, Jane and Ashwin want to order pizza - they know they will each 
eat 4 slices of pizza. The local pizza shop sells pizzas of only 6 slices
What is the minimum number of pizzas needed - Use floor division
"""

total_slices = 4*4
total_pizzas = (total_slices+5)//6
print(f'Pizzas: {total_pizzas}')
