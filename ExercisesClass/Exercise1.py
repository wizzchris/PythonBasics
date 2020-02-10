#Create a little program that asks the user for the following details
#name, height,favourite colour,a secret
#Capture these inputs
#Print a tailored welcome message to the user
#print other details it gethered , except the secret of course

name_of_person=input('Hello, What is your name?    ')
print('Thank you')
height_of_person=input('What is your height?    ')
print('Thank you')
favourite_colour=input('What is your favourite colour?      ')
print('Thank you')
secret=input('Please tell me a secret?      ')
print('Thank you')
Welcome='Hello ' + name_of_person + '. Hope you are well. You are {}'.format(height_of_person) + ' ' + 'your favourite colour is ' + favourite_colour + 'and dont worry i wont tell your secret' + ' ' + secret

print(Welcome)
