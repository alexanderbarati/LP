'''1'''
#message = "Bob's World"
message = 'Bob\'s World'

print(message)

'''2'''
payam = '''Bob's world was a good
cartoon in the 1980s'''
print(payam)

'''3'''
print(len(payam))

'''4-slicing[https://www.youtube.com/watch?v=ajrtAuDg3yw]'''
'''4-1'''
print(payam[0])

'''4-2'''
print(message[0:5]) # first index is inclusive but the second one is not

'''4-3'''

print(message[0:11])

'''4-4'''
print(message[5:])

'''5: str methods'''
print(message.lower())

'''5-1:count method'''
print(message.count('l'))

'''5-2:find'''
print(message.find('World'))

'''5-3:replace(want to replace, replace with)'''
print(message.replace("Bob's", 'Hello'))

'''5-4: String formating [https://www.youtube.com/watch?v=vTX3IwquFkc]'''
greeting = "Hello"
name = "Alex"
message = greeting+", "+name
print(message)
message = '{}, {}. Welcome!'.format(greeting, name) 
print(message)

'''5-5:f.(this is a new way of formating)'''
message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

'''6'''

print(dir(name))# 'dir()' Will show us all of the attribute and methods that we have access 

'''6-1'''
print(help(str))# more information in details

'''6-2'''
print(help(str.lower))

