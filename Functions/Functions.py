# Functions do one key task. We make the functions small so we understand what it’s doing as well as make it testable. It makes your code more readable, maintainable and testable

# DRY
# Don’t repeat yourself

# They can take in inputs (optionally), do some work (block of code) runs a block of code when called
# you start off with
def <name>(arguments):
Then block of code
then return

# Also functions need to be defined then called

# Best practises include:
# function does one small task
# generally does not print the inside of a function. you return

# Here’s a function with no arguments

def say_hello():
    return 'hello'

# This returns hello to call the function just use its name

def full_function (f_name,l_name):
    return f_name + ' ' + l_name

# This will give you your first name combined with the last name

def welcome_message(f_name, l_name):
    return 'hello how are you' + full_function(f_name, l_name)

# This calls the function above and uses it in this function ie full function is contained in welcome message. This can be added with many functions calling a function should be separate and we should import the function if we require it
