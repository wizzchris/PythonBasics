guess = 1
while guess < 100:
    if guess % 3 == 0:
        print ('Fizz')
        guess += 1
    elif guess % 5 == 0:
        print ('Buzz')
        guess += 1
    else:
        print (guess)
        guess += 1
while True:
    guess = input('What number do you want to check?')
    if guess == 'BREAK':
        break
    elif int(guess) % 3 == 0:
        print ('Fizz')
    elif int(guess) % 5 == 0:
        print ('Buzz')
    else:
        print (guess)


while True:
    num = input('What do you want it to count up to?')
    x=0
    if num.isnumeric() == True:
        num = int(num)
        while x < num:
            if x % 3 == 0:
                print('Fizz')
                x += 1
            elif x % 5 == 0:
                print('Buzz')
                x += 1
            else:
                print(x)
                x += 1
    elif num == 'Break':
        break
    else:
        print('Not valid')
