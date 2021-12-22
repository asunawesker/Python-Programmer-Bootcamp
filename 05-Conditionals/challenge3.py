"""
QUESTION 1: Write code that ask the user to input a number between 1 and 5 inclusive.
The code will take the integer value and print out the string value. So for example if the 
user inputs 2 the code will print two. Reject any input that is not a number in that range
""" 

user_input = int(input('Enter an integer between 1 to 5: '))

if user_input == 1:
    print('one')
elif user_input == 2:
    print('two')
elif user_input == 3:
    print('three')
elif user_input == 4:
    print('four')
elif user_input == 5:
    print('five')
else:
    print('Invalid input, just numbers between 1-5')
    
""" 
QUESTION 2: Repeat the previus task but this time the user will input a string 
and the code will output the integer value. COnvert the string to lowercase first.
""" 

user_input = input('Enter a word between one to five: ')
user_input = user_input.lower()

if user_input == 'one':
    print(1)
elif user_input == 'two':
    print(2)
elif user_input == 'three':
    print(3)
elif user_input == 'four':
    print(4)
elif user_input == 'five':
    print(5)
else:
    print('Invalid input, just strings between number one and five')

""" 
QUESTION 3: Create a variable containing an integer between 1 and 10 inclusive. Ask the
user to guess the nunber. If the guess too high or too low, tell them they have not won. 
Tell them they win if they guess the correct number.
""" 

secret_number = 5
guess_number = input('Enter a number between 1 to 10: ')

if guess_number.isdigit():
    guess_number = int(guess_number)
    if(secret_number == guess_number):
        print('You won')
    else:
        print('You did not work')
        if(secret_number > guess_number):
            print('secret number is lower than the number you enter')
        if(secret_number < guess_number):
            print('secret number is higher than the number you enter')
else:
    print('That\'s not a digit')
      
""" 
QUESTION 4: Ask the user to input their name. Check the length of the name. If it is
greater than 5 characters long, write a message telling them how many characters
otherwise write a message saying the length of their name is a secret
""" 

name = input('Enter your name: ')
name_length = len(name)

if name_length > 5:
    print(f'The length of your name is: {name_length}')
else:
    print('The length of your name is a secret')

""" 
QUESTION 5: Ask the user for two integers between 1 and 20. If they are both greater 
than 15 return their product. If only one is greater than 15 return their sum, if neither 
are greater than 15 return zero.
""" 

number_1 = int(input('Number 1 between 1 and 20: '))
number_2 = int(input('Number 2 between 1 and 20: '))

if number_1>15 and number_2>15:
    print(f'Product: {number_1*number_2}')
elif number_1>15 or number_2>15:
    print(f'Sum: {number_1+number_2}')
else: 
    print(0)

""" 
QUESTION 6: Ask the user for two integers, the swap the contents of the variables. So if var_1 = 1 
and var_2 = 2 initially, once the code has run var_1 should equal 2 and var_2 should equal 1.
""" 

var_1 = int(input('Number 1: '))
var_2 = int(input('Number 2: '))

var_1, var_2 = var_2, var_1

print(f'NNumber 1 now is equal to {var_1}')
print(f'Number 2 now is equal to {var_2}')