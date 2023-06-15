## Conditionals
import sys
##Initialise lists
lista = ['tin', 'eggs', 'flour']
listb = []

if lista == listb:
    print("Same!")
elif lista != listb:
    print('not same')

if 'eggs' in lista:
    print("eggs are found")
else:
    print('no eggs found')

num1 = 5
num2 = 3
distance = 10

if num1 > num2:
    print('number 1 is greater than 2')

else:
    print('num1 isn noy greater than num2')

if 0 < num1 < 42 < num2 and distance != 20:
    print('my conditions are met')

else:
    print("my conditions are not met")

#passwd = input('Enter your password')
passwd = ""
if passwd == "pass1234":
    print("Password is correct")
elif len(passwd)<8:
    print("Length of the password is less than 8")
elif '%' not in passwd and len(passwd)<8:
    print("Password contains special characters")
else:
    print("Password is wrong")

##testing if lists are empty oir has values
mylist = [0, 1, 2, 3]
if mylist:
    print('list is true or contains values')
else:
    print("list is empty")
##are all items on the list true
if not all(mylist):
    print('Not all items are true')
else:
    print("All items are true")

if any(mylist):
    print('Atleast one item is true')
else:
    print('No item is true')


num = 42
txt = '3'


# if txt<num:
#     print('txt<num')

# if int(txt) <num:
#     print("txt converted to int <num")


# line = None

# while line != 'done':
#     line = input('Type  "done" to complete :')
#     print('<', line, '>')


# my1 =[23, 67, 32, 9, 77, 100]
#
# while my1:
#     print(my1.pop() * 2)


# i = 1
# j = 120
#
# while i < 65:
#     i = i * 2
#     print(i)
#     if j > j: break
# else:
#     print("Loop expired", i)
# print("Final Value", i)

# for arg in sys.argv:
#     print("cmd line argument:", arg)
#
# for i in range(0, 50):
#     print(i)
#     if i > 42:
#         print('I is greater than 42')

some_list = [0, 1, 2, 3, 4, 5, 6]
for i in range(0, len(some_list)):
    if some_list[i]> 3:
        some_list[i]+=1
        print(some_list[i])

fruits = ['mango', 'pear', 'pineapple']
for i in range(0, len(fruits)):
    print(fruits[i])
    if fruits[i]=="mango":
        print('my fav fruit is '+fruits[i])
        print(fruits[i])
