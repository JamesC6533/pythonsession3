colors = "red blue green yellow brown black".split()
months = " Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

for i, color in enumerate(colors):
    print(i,color)

print()

for num, month in enumerate( months, 1):
    print("{} {}".format( num, month))

    print("yellow in colors: ", ("yellow" in colors))
    print("pink in colors: ", ("pink" in colors))

print("colors: ", ",".join(colors))

del colors[4]

print("removed 'brown':",",".join(colors))

colors.remove('green')

print("removed 'green':", ",".join(colors))

sum_of_lists = [True] + [True] + [False]

print("sum of lists:", sum_of_lists)

product = [True] * 5
print("product of lists:", product)