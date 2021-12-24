"""
QUESTION 1: Ask the user for two numbers between 1 an 100. Then count from the lower number
to the higher number. Print the results to the screen.
""" 

number_1 = int(input('Enter a number between 1 an 100: '))
number_2 = int(input('Enter other number between 1 an 100: '))

while number_1<0 or number_1>100 or number_2<0 or number_2>100: 
    number_1 = int(input('Enter a number between 1 an 100: '))
    number_2 = int(input('Enter other number between 1 an 100: '))
    
if number_1<number_2:
    for i in range(number_1, number_2+1):
        print(i, end=' ')
else: 
    for i in range(number_2, number_1+1):
        print(i, end=' ')

""" 
QUESTION 2: Ask the user to input a string and the print out the screen in reverse order (use a for loop)
""" 

string_input = input('Enter any word: ')
reverse_string = ''

for i in reversed(string_input):
    reverse_string = reverse_string + i
    
print(reverse_string)

""" 
QUESTION 3: Ask the user for a number between 1 and 12 and the display a times table for that number
"""       

number = input('Enter a number between 1 and 12: ')

while (not number.isdigit()) or (int(number)>12 or int(number)<1):
    number = input('Enter a number between 1 and 12: ')

for i in range(1, 13):
    print(f'{int(number)} * {i} = {int(number)*i}')
    
"""     
QUESTION 4:  Can you amend the solution to the question 3 so that it just prints out a times table
between 1 and 12? (No need to ask the user for the input)
""" 

for i in range(1, 13):
    print(f'\nTimes table of {i}')
    for j in range(1,13):
        print(f'{j} * {i} = {j*i}')

"""         
QUESTION 5: Ask the user to input a sequence of numbers. Them caculate the mean and print the results
""" 

values = input('Enter space spared some integer values: ').split()

values_int = []

for i in range(len(values)):
    if not values[i].isdigit():
        print(f'{values[i]} is not an integer and it\'ĺl be ignore')
    else:
        values_int.append((int(values[i])))
        
mean = sum(values_int)/len(values_int)

print(mean)

""" 
QUESTION 6: Write the code that will calculate 15 factorial. 
""" 

n = 15
fact = 1
for i in range(1, n+1):
    fact = fact*i
    
    
print(fact)

""" 
QUESTION 7: Write the code to calculate Fibonacci numbers. Create list containing first 20 FIbonnacio numbers.
""" 

a = 0
b = 1
fibonacci_numbers = []

for i in range(20):
    fibonacci_numbers.append(a)
    a, b = b, a+b
    
print(fibonacci_numbers)

""" 
QUESTION 8: Can yout draw and f with * using python?
""" 

start = '*'

for i in range (6):
    for j in range(6):
        if i==0 and j==0:
            print(start * 6)
        if (i==1 and j==0) or (i==3 and j==0) or (i==4 and j==0) or (i==5 and j==0):
            print(start)
        if i==2 and j==0:
            print(start * 5)
"""     
QUESTION 9: Write some code that will determine all odd and even numbers bewtween 1 and 100. Put the odds in a 
list named odd and the evens in a list named even.
""" 

i = 1
even = []
odd = []

while i!=100:
    if not i%2:
        even.append(i)
    else: 
        odd.append(i)
    i += 1
    
print(f'Even numbers: {even}')
print(f'Odd numbers: {odd}')     