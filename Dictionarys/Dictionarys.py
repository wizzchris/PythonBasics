# What happens if we extra info per each subject
# ie say we have a number for each thing

# This allows us to separate the information up into key value pairs. Like a dictionary
# To start a dictionary you use curly brackets {}
my_dictionary = {}
'key' : 'value' # is in each curly bracket
my_dictionary = {'egg':1, 'ham':2, 'friends':3}

# CRUD create read update delete

# Read all the data of dictionary
print (my_dictionary)
# Read one entry in a dicitonary
print(my_dictionary['eg'])
# Update the value in a key
my_dictionary['egg'] = 5
# Destroy one key value pair
my_dictionary.pop('egg')

# Create a value pair
my_dictionary['cheese'] = 8

# Getting all the keys
print(my_dictionary.keys())
# Getting all the values out
print(my_dictionary.values())

# Nested data

student_1 = {'name':'Morty', 'Stream':'Universal Quest', 'Grade':12,}
student_2 = {'name':'Summer', 'Stream':'Terrestial quest', 'Grade':20}
students_list = [student_1,student_2]

print(students_list[1])


students_dict = {'student_1':student_1, 'student_2': student_2}


students_dict = {'student_1':student_1, 'student_2': student_2}

# Use the list to print the individual student names
print(students_list[0]['name'])
print(students_list[1]['name'])
# Use the dictionary to print individual student names
print(students_dict['student_1']['name'])
print(students_dict['student_2']['name'])
