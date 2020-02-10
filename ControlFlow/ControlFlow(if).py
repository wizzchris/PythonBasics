# This is if statements. Control where the code will execute depending on assertions
# An assertion is something that returns true or false

# Block of code refers to a consecutive lines of code that is indented and will run together. Blocks exist inside if statements and while loops and other functions, in simple words it is a specific piece of code that will run in a specific time
# Start an if with If. There must be a : at the end of the condition
if <assertion/condition>:
    block of code with indentation
    second line of code
elif <condition>
    block of code with indentation
else
    block of code with indentation

weather = 'Rainy'

if weather == 'Rainy':
    print 'Get an unbrella'
elif weather == 'sunny':
    print ('what a nice day')
else:
    print ('A normal day')

# You can use the in function to make it more forgiving

elif 'stormy' in weather
