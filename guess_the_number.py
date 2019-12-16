import random
print('Welcome to GUESS THE NUMBER game! You have 5 attempts to guess the number from 1 to 100 that computer thinks of. Good luck!')
number = random.randint(1,100)
trial = 0
for i in range(0,5,1):
	x = float(input('Please, enter the number...'))
	x = round(x)
	trial = trial + 1 
	if x == number:
		print('Congrats! The number was', number, 'and you guessed it! It took you', trial, 'times to guess it.')
		break
	elif x>100 or x<1:
		print('error, the number you entered is out of range. Try again. You have', 5-trial, 'more chances')
	elif trial==5:
		print('Game over. You tried', trial,  'times and did not guess it. Play again!')
	else: 
		print('Wrong number, try again. You still have', 5-trial, 'more chances ')

