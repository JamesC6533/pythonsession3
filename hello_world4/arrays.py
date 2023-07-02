fruits = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig']
name = "James Cotterill"
knight = 'king', 'James', 'England'

print(fruits[3])
print(name[0])
print(knight[1])

list1 = list()
list2 = ['apple', 'banana', 'mango']
list3 = []
list4 = 'apple banana mango'.split()

print("list1", list1)
print("list2", list2)
print("list3", list3)
print("list4", list4)


print("list2[0]:", list2[0])
print("list4[4]:", list4[2])

print("list4[-1]:", list4[-1])

###TUPLES

birth_date = 1965, 17, 11
server_info = 'linux', 'RHEL', 5.3, "James Cotterill"
latlon = 35.99, -72.390

print("birth_date", birth_date)
print("server_info", server_info)
print("latlon", latlon)

# slicing
print(fruits[1])
print(fruits[2:5])
print(fruits[-1])

mylist = ['apple', 'cherry', 'orange', 'kiwi', 'banana', 'pear', 'fig']
mytup = ("James Cotterill", "Jeremy Cook", "Eric Idle", "John Cleese")
mystr = "Eric is the funny one"

for p in mylist:
    print(p)
print()

for r in mytup:
    print(r)
print()

for ch in mystr:
    print(ch, end='-')
print()



