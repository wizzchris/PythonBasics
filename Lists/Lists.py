# Defining a list by using a square bracket []
crazy_landlords = []
print(type(crazy_landlords)) # this is a list
# We can dynamically define a list
# or redefine a list
crazy_landlords = ['Mr Richards', 'Raj', 'Mr Shirik', 'Zmem', 'Zemmuen']
# To access an object in a list
# To do that we use indexes. They are organised by an index
name_list_index = [0,1,2,3,4,5....]

# To access landlord raj we need index number 1 between square brackets
crazy_landlords[1]

# To redefine a list at a particular index by selecting the index and adding =
crazy_landlords[1] = 'eggs'
# This changes raj to eggs

# Print all of the list is just print list

# Printing the last record is just -1
# Another way is to get the length and make it into an index -1
length_list = len(crazy_landlords)
last_index = length_list -1
print(crazy_landlords[last_index])

# Adding a record to the list
# Get the list and .append()

crazy_landlords.append('Lana')
# This adds lana at the end

# What if we need to insert of place a record at a specific index we use .insert()
crazy_landlords.insert(1, 'James')
# .Removes the first item and removes that particular value. Returns the list without the value
# .remove('Alice')
# .pop() will delete the index version of the vlaue or the last entry

crazy_landlords.pop()

# There are other things about lists, we can have mixed lists
hybrid_list = ['json', 'Jason', 13, [1,2]]

# Each thing is an instance of the string
