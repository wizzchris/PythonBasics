


print('Welcome to the game of fizz buzz.')
number = 1
while True:
    guess = input('What number is next? Type HELP for rules. EXIT to end. RESTART to restart. ----------').strip().upper()
    if guess == '0':
     print('The number starts at 1')

    elif guess.isnumeric() == True:
        if (int(guess) % 3) == 0:
            print('Sorry, you lost, try again')
        elif (int(guess) % 5) == 0:
            print('Sorry, you lost, try again')
        elif guess == str(number):
            number += 1

    elif guess.isnumeric() == False:
        if guess == 'HELP':
            print('Add 1 to the previous number, and if the number is a multiple of 3 say FIZZ\n and if it is a multible of 5 type BUZZ.\n The number starts at 0')
        elif guess == 'EXIT':
            break
        elif guess == 'RESTART':
            guess = 1
        elif guess == 'FIZZ':
            if (int(number) % 3) > 0:
                print('Sorry thats wrong, guess again')
            else:
                number += 1
        elif guess == 'BUZZ':
            if (int(number) % 5) > 0:
                print('Sorry thats wrong, guess again')
            else:
                number += 1
        else:
            print('Sorry that is not a valid guess')