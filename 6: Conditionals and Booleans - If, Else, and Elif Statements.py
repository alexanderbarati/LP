'''1'''
if True:
    print('Conditional was True')

'''1'''
if False:
    print('Conditional was True')

languge = 'python'
if languge == 'python':
    print('Languge is Python')
elif languge == 'C++':
    print('Languge is C++')

elif languge == 'Java':
    print('Languge is Java')
else:
    print('Languge is not Python')


user = "Admin"
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')


user = "Admin"
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please log in')

'''2'''
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b) # Because these are two different objects in memory, the answer is Fase
print(id(a))
print(id(b))
print(id(a)==id(b))
a = b
print(a == b)
print(a is b) # Because these are two same objects in memory, the answer is True
print(id(a))
print(id(b))
print(id(a)==id(b))

'''3'''
condition = False 
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')


condition = None 
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')


condition = 0 
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')


condition = 10 
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')


condition = [] # or empty: '', (), {}  
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')


condition = 'Test' 
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')