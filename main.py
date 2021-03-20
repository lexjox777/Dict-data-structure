#  Dictionary items are key value pairs enclosed in Curly bracket
# Dict is ordered
# Dict is mutable
# Dict keys are unique, cannot have duploicates
# Elements can be of different data types

# '''
# Dict attributes
# '''
# print(dir(dict))
# print(help(dict.pop))

'''
# Creating Python Dictionary
# '''
# dict_example={}
# dict_example={'name':'Kingsley', 'age': 30}
# dict_example= dict([(1,'car'),(2,'bicycle')])
# print(dict_example)

'''
Access Dictionary values
# '''

# student={'name':'Kingsley', 'age': 35}
# print(student['age'])
# print(student.get('age'))
# print(student.keys())
# print(student.values())


# students={'name':'Kingsley', 'age': 35}, {'name':'John', 'age': 37}
# print(students[1]['name'])
# for i in range(len(students)):
#   print(students[i]['age'])

# '''
# Changing Dictionary elements
# '''
# student={'name':'Kingsley', 'age': 35}
# student['age']=37
# print(student)

# ---------------

# student={'name':'Kingsley', 'age': 35}
# student.update({'name': 'Jennifer', 'age': 38})
# print(student)

# ----------------

# student={'name':'Kingsley', 'age': 35}
# # student.setdefault('name', 'Steve')
# # print(student)
# # set.default doesnt change the 'key' i.e 'name' because it already exist
# student.setdefault('Subject', 'Mathematics')
# print(student)
# in this case above set.default injects the 'key' i.e 'Subject' in the argument because it doesnt exit in the arguement


'''
Remove Element From Dictionary
'''
# student={'name':'Kingsley', 'age': 35}
# student.pop('name')
# print(student)

# ================
# student={'name':'Kingsley', 'age': 35}
# student.popitem()
# # this remove the last item i.e 'age':35
# print(student)

# =============

# student={'name':'Kingsley', 'age': 35}
# student.clear()
# # this clear all the items inside student 
# print(student)


# student={'name':'Kingsley', 'age': 35}
# del student
# print(student)


'''
Dictionary Membership Test
'''

student={'name':'Kingsley', 'age': 35}

print( 'age' in student)
print( 'age' not in student)
