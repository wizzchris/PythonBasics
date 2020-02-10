# Iterations
for <placeholder> in <iteratable>:
    block of code
    indented lines are part of this block

cars = ['Skota Felecia Fun', 'Mustangs Boss 429','Fiet 500','Jaguar 420g', 'Aston Martin vanquish']

for x in cars:
    print(x)

# This prints all the cars in the list
# Iterating over a list.
# You can also iterate over a dictionary

student1={
    'name':'Arya Stark',
    'stream':'Many faces',
    'grade': 10,
}

for key in student1:
    print(key)
    print(student1[key])
# This prints both the key and the values of each key


# Nested loops

normal_list = [1,2,3,4,5]

for num in normal_list:
    print(num * 3.5)

embeded_list = [[1,2,3],[5,1,2,4,1],[1,1,34,5,32,1],[1,2,4,2,1]]

for num in embeded_list:
    for num2 in num:
        print(num2)
# This prints each individual number in the embedded list

dict_data ={1:{1:'a'},
            2:{2:'b'},
            3:{3:'c'},
            4:{4:'d'}}
for key in dict_data:
    for key2 in dict_data[key]:
        print(dict_data[key][key2])
# This prints each of the letters

# While loops
# You put while at the start
while <condtion>:
     Block of code
x = 0
while x<10:
    print(x)
    x += 1

# Used when something alters the condition
# Other functions can be combined, such as a for loop
# Syntax and patterns for while loops
while True:
   block of code
   control flow
   break
