'''1'''
student ={'name' : 'Alex', 'age':27, 'Courses':['Math', 'CompSci']}
print(student)

print(student['name'])

print(student['Courses'])

print(student.get('name'))

print(student.get('home')) # With .get method output shows NOne
#instead of error when there is not any Value with this name

print(student.get('home', 'NOT Found')) # We can Pass a value to shows instead of None



'''2 : adding'''

student['Phone'] = '015771222'
print(student['Phone'])


student['name'] = 'John'# Updating a value
print(student)

student.update({'name': 'Sani', 'age': '30', 'addres':'Germany'})# with .update method we can update several values
print(student)

'''3: delet'''
del student['age']
print(student)

Phone = student.pop('Phone') # Whit .pop method you can delet a key and also add it to a variable
print(Phone)
print(student)


'''4:loop'''
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# For looping throw the dic you must use .itemو Otherwise just shows the keys
for key, value in student.items():
    print(key,":", value)