
#Iterate over the sudent 1
#I want the output to be
#name is arya stark
#stream is many faces



student1={
    'name':'Arya Stark',
    'stream':'Many faces',
    'grade': 10,
}



for key in student1:
    value = str(student1[key])
    print(key.capitalize() + ' is ' + value + '.')

dict_data ={1:{1:'a'},
            2:{2:'b'},
            3:{3:'c'},
            4:{4:'d'}}
for key in dict_data:
    for key2 in dict_data[key]:
        print(dict_data[key][key2])
#This prints each of the letters