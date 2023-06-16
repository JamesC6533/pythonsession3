a = []
b = [1, 'string', True, 2.3]

# to add an item to a list
b.append('test')

# to insert an item to a list in a specific place
b.insert(2,"myinsert")

# length of a string
len(b)

# replace an item from a list to swat position 1 and 2
b[1:2] = ["replace1", 2]

# delete items from a list
b[1:2] = []
del (b[1])

c = [a, b]
c[0]
c
c[1]
c[1][1]

# append a list to a list
c.append(c)
c[2]
c[2][1]

# lists can repeat multiple of the same value 