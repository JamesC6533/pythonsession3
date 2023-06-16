b = {1, "String", 2.3, 1, 1, True}
#OUTPUT: 1, 2.3, "String" As you can multiple of the same values in a list

# finds if the value is within the list
"String" in b
# true
"String" in c[1]

a = {}

b = {'a': 1, 'b' : 2, 'c' : 3}

b['a']
#OUTPUT 1

b['a'] = "anything"
#OUTPUT {'a': "Anything", 'b' : 2, 'c' : 3}

b[15] = 5
#OUTPUT {'a': 1, 'b' : 2, 'c' : 3, 15: 5}

list(b)
#OUTPUT ['a', 'b', 'c', 15]

# delete an item from a dictionary
del(b[15])
#OUTPUT {'a': "Anything", 'b' : 2, 'c' : 3}

# how to check if an item is in a dictionary 
"c" in b
"d" in b

