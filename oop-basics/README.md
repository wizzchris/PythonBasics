# READ ME FILE for OOP

## Topics we will cover
- 4 Pillers: Including
 . Abstraction
 . Inheritance
 . Polymorphism
 . Encapsulation 
 
- Git and github
- Documentation and Markdown Files 
- Best pracitices and organisation
 
 ## Definitions
 - Class - A class is a blue print for objects. Inside we define how objects characteristics and behaviors it can do. With classes you cna create instances of that class.
 - Instance - The occurrence of an object of a specific class 
 - Method - Is like a function that can only run inside a class
 - __init__ method - Is a method to inisilise the class. It runs everytime you creat an object using a class. AKA: it is known as the constructore method 
 - Behaviours - Methods which are like functions that belong to a class will be called on objects on that class 
 - Self refers to the instance. In a method, self is the specific instance of that
 - Pillars:
  - Abstraction
  . This is hidding complexity, and give our user only what they need to make things work.
  . Think of it like a black box
  . Example is shifting gears in a car
  . In code the methods .split() or .append() for strings and lists are abstracted. We only see the documentation
 - Attributes - They are variables or constants that are attached to a object
 - Class Attributes - Are attached to the class and are specific to every instance of that class
 - Inheritance - Ability to inherit all the behavior and characteristics of parent class
 - Super(). - Super allows me to access to parent methods. It is commonely used when you want to use init. 
 

## Inheritance
The ability to inherit all the behavior and characteristics of parent class.
Keeps you DRY and allows you to create systems faster

## Polymorphsim - Inheritance Polymorphism
The ability to change method or characteristics in sub-class
So a methods make_a_sound can have different behaviours in diffrent classes 
Smaller forms of polymorphism include:
- A method that takes in arguments to change output
- A method that has optional arguments is a form of polymorphism 
- A method or a function that can take any number of arguments is a form of polymorphism 

## Encapsultaion
Restricting access / making methods / attributes private 
This allows us to make methods and attributes private. This means making something private means it can only be accessed by methods of its own calss
This can be useful to hide sensitvie information or have behavior that should not be accessed externally.

