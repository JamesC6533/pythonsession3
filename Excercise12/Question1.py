cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
# append an item to the end of the list
cheese[-1:] += ['Oke']
# addd two new cheeses to the list with a single line
cheese += ['Brie', 'Chester']
print(cheese)

cheese.append('Oke')
cheese.extend('Brie', 'Chester')
