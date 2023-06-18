# myn = [45, 66, 12, 3, 99, 3.142, 42]
# print("min:", min(myn), "Max:", max(myn))
# print(str(min(myn))+" "+str(max(myn)))
# print("sum:", sum(myn))
# print('length', len(myn))

# a = 10
# b = 11
#
# c = "John"
# d = "Peter"
#
# a,b = b,a
# c,d = d,c
#
# print(a)
# print(b)
#
# print(c)
# print(d)

# Gouda, Edam, Brie = range(3)
#
# print(Gouda)
# print(Edam)
# print(Brie)

# thing = ('Hello')
# print(type(thing))

# myd = {'fred':3, 'jim':8, 'dave':42}
# print("min:", min(myd), "max:", max(myd))
#
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
print(cheese[0])
print(cheese[1])
print(cheese[2])
cheese[-1] = 'Red Leicester'
print(cheese)
#
# mytuple = ('eggs', 'bacon', 'spam', 'tea', 'beans')
# print(mytuple[2:4])
# print(mytuple[-4])
#
# # convert tuple to list
# mylist = list(mytuple)
# print(mylist[1:])
# print(mylist[:2])
#
# # remove item from a list
# cheese = ['Cheddar', 'Stilton', 'Brie', 'Camembert', 'Cornish Yarg']
# del cheese[0]
# print(cheese)
#
# add item to the left or right
cheese[:0] = ['Cheshire', 'Chester']
cheese += ['Oak', 'Devon Blue']
print(cheese)
#
# # pop
# saved=cheese.pop(1)
# print("My deleted item is ", saved)
# print("my new list is ", cheese)
#
# cheese.remove('Oak')
# print("List after removing oak is ", cheese)
#
# # sort
# cheese.sort(key=str.upper)
# cheese.sort(key=len)
# print("my sorted cheese is ", cheese)
#
# # list methods
# print(cheese.count("Stilton"))
#
# # return index of item
# print(cheese.index("Stilton"))

# dictionary
mydict ={"Australia":"Canberra", "Eire":"Dublin", "France":"Paris", "Finland":"Helsinki", "UK":"London"}
print(mydict['UK'])

mydictCity = {'UK': ['London', 'Wigan', 'Bolton'], 'US': ['Miami', 'Springfield', 'New York']}
print(mydictCity['UK'][2])

# Iterate over a dictionary
for county in mydict.keys():
    print("Country, :",mydict[county])

print(mydict.keys())



