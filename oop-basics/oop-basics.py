
# To start a class you specify a class then the name with a coloun


class Animal:
    # Characteristics -attributes
    def __init__(self, name, legs, eyes, claws, tasty):
        self.name = name
        self.legs = legs
        self.eyes = eyes
        self.claws = claws
        self.tasty = tasty

    # Behaviours - methods
    def eat(self, food=''):
        return 'nom nom nom nom' + ' ' + food
    def sleep(self):
        return 'zzzzzzzzz'
    def potty(self):
        return 'O_o ..... Hhhhuuuummmm!!!!! SPLOSH!'
    def hunt(self):
        return 'ATTACK!!'

# Create an instance of an animal


animal1 = Animal('cat',4,2,'yes','no')
animal2 = Animal('pig',4,2,'no','yes')
print(animal1)
print(type(animal1))

print(animal1.name)
# We can get the names of each of the variables by calling the class and doing .asdas
print(animal2.tasty)

# If we dont want to specify certain parts it has to be in order. ie name = name

print(animal1.eat())

# We can make methods on objects
# Above shows this and returns the eat command
# Above we calAled the method on the item and printed the return
# The self refers to the object and is automatically passed.
# Self refers to self

# You can also make an optional, this means that you dont necessarily have to specify it
# for example, above we have food = ''

# We can sperate our class definition from running it provide some documentation on the available methods
# Provide some documentation on the avilable methods. (provide a README with methods and how to use them)

# Dont forget to make a read me file with what it does For example
##Instilation
##Import module to your code
##Usage
##This covers from creating instance to most use methods
####Creating a animal object
#### ''''
#### ringo = Animal()
#### ''''
##Initiating an Animal instance with optional parameters:


#Inheritance
#Inheritance is used to transfer qualities from one class to another

class Reptile(Animal):
    def seek_heat(self):
        return 'Humm where dat sun @'

    def lay_eggs(self):
        return 'pop pop pop pop pop'
    def hibernate(self):
        return self.sleep()


ringo = Reptile('ringo', 4)
print(ringo)
print(ringo.eat())

#A parents class method will be used if the sub class doesnt overwrite the method
#The polymorphism is the idea that the previous method can be used
#However we come into a problem that if we do a __init__ in the subclass, then we cant pass throught the parent class __init__
#To get around it we use super().

class mammal(Animal):
    def __init__(super,tempreature):
        super.__init__(name, legs, eyes, claws, tasty)

#We can also apply the super. as well for class methods to get the parent method first ie eat()... super.eat() will run super eat then eat

#Double underscore of the name self.__ makes it private. It stops anyone accessing it. One underscore tricks people
#Internal methods has access to encapsulated methods ie by setting it


































