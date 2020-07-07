'''1'''
courses =['History', 'Math', 'Physic', 'Computer']
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1]) # This print always the last item of list
print(courses[0:2]) # first index is inclusive but the second one is not
print(courses[:2])
print(courses[2:])
'''[Slicing Lists and Strings]
(ttps://www.youtube.com/watch?v=ajrtAuDg3yw)'''

'''2: adding'''
courses.append('Art')
print(courses)
courses.insert(0, 'Sport')
print(courses)

#courses_2 = ['sketch', 'education']
#courses.insert(0, courses_2)# Add entire list to the list
print(courses)
print(courses[0])

#courses.extend(courses_2)
print(courses)# extend add the just the items to the list

'''3: Removing'''
courses.remove('Math')
print(courses)

courses.pop() #Delet the last value of the list
print(courses)

popped = courses.pop() #Delet the last value of the list
print(popped) # it remove the last value also shows the deleted value


'''4 : sorting'''
courses.reverse()
print(courses)

courses.sort()
print("Sorted:",courses)

numbers = [1,5, 4, 3]
numbers.sort()
print(numbers)

courses.sort(reverse=True)
print(courses)

numbers.sort(reverse=True)
print(numbers)
# This commands change the orginal list(sort them)
# There is also a way that we sort the list without altering the original 

sorted(courses)# This two doesnt change the orginal list
sorted(numbers)

'''[Sorting Lists, Tuples, and Objects](
    https://www.youtube.com/watch?v=D3JvDWO-BY4)'''

'''5'''
print("Min:", min(numbers))
print("sum:", sum(numbers))

'''6: find'''

print(courses.index('Physic')) # Finding the index of a value of list

print('Art' in courses) # Checking if a value is in the list

for item in enumerate(courses): # 'enumerate' give back the value and index
    print(item)


for index ,course in enumerate(courses): # 'enumerate' give back the value and index
    print(index, course)


for index ,course in enumerate(courses, start=1): # We costumize the start value
    print(index, course)

'''7'''
course_str = ', '.join(courses)
print(course_str)

course_str = ' - '.join(courses) # Make a str of a list
print(course_str)

new_list = course_str.split(' - ') # Making a list of a string
print(new_list)


'''8: TUples'''

'''[Mutable vs Immutable](https://www.youtube.com/watch?v=5qQQ3yzbKp8)'''

min : 20