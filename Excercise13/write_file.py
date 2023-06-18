output = open('pelican.txt','w')
output.write("A wonderful bird the pelican")
output.write("\nHis bill holds more than his bellican")
output.write("\n")
output.close()

lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm dammed if I can see how the helican.\n"]

with open("pelican.txt", "a") as file:
    file.writelines(lines)
