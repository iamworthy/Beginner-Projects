# test code to guess random number

import random

 

print('You have 3 attempts to guess the number I am thinking of between 1 and 10')

 

computernumber = random.randint(1, 10) #selects a random number between 1 and 10

guessestaken = 0

 

while guessestaken < 3:

    try:
        guess = int(input('Take a guess: '))
        guessestaken += 1

       
        if guess < computernumber:
            print('Too Low')
   
        elif guess > computernumber:

            print('Too high')


        elif guess == computernumber:
            break

    except ValueError: #entering anything other than a number causes valueerror, this code stops that

        print('This is not a number')

       

if guess == computernumber:

    print('Well done, the random number was: ' +str(computernumber))

 

else:

    print('Unlucky, the random number was: ' +str(computernumber))
