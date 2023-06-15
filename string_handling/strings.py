import re
# name = " fred " " bloggs " " peter "
# testvar = 'test'
# print(name + testvar)

# print("The answer is ", 42, "always", sep='\n', end='')

# html="""
#
# <tr>
#
# </tr>
#
# """

name = ' Sky Glass '

print(name.lower())

print(name.upper())

name1=name.replace('y','e')
print(name1)

# find a string

print(name.find('s'))

print(name.endswith('k'))

if name.endswith(''):
    print("No results found")

#length of string
print(len(name))

#slicing start: end-1
print(name[0:9])

#Strip empty space
print(name)
print(name.strip())

#string format
age = 20
message = 'Hello my age is '+str(age)
print(message)

newmessage = 'Hello my age is {} '
print(newmessage.format(age))

newmessage1 = 'My age is {1} and I work for {0}'
print(newmessage1.format(20,'Sky'))

#string split
line = 'root::0:0:superuser:/root:/bin/sh'
elems = line.split(':')

print(elems[0])
print(elems[1])
print(elems[2])
print(elems[3])
print(elems[4])

line1 = 'Hello world, This is GOD.'
elems1 = line1.split(',')
elems2 = line1.split(',')

print(elems1[0])
print(elems1[1])
print(elems2[0])
print(elems2[0])

#Regex regular expressions
message = 'Sky Glass'
newMessage = re.search('^Sky.*Glass$',message)
print(newMessage)
if newMessage:
    print('text, found')
else:
    print("text not found")

text='hello world'
if re.match(r'^hello',text):
    print('Its hell in here')

# [0-9 A-Z a-z] returns items based on what you are searching
if re.match(r'^[A-Z a-z]+$',text):
    print('string is all alpha')
