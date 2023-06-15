
# # Open file for read only
myFILE = open('sample.txt','r')
# # read entire file
# print(myFILE.read())

# read line
line = myFILE.readline()
print(line)

#Read and split file
lines = myFILE.read().splitlines()
print(lines)

#
for line in open("sample.txt").readlines():
    print(line, end="")

# safe way of opening files
with open('sample.txt','r') as infile:
    for line in infile:
        print(line, end="")

#open for writing
output = open('sample.txt','w')
output.write("anything")
output.close()

#Open for writing and creating a new file
output = open('sample2.txt','w')
output.write("Test")
output.write("\n")
output.close()

#Open for appending
output = open('sample.txt','a')
output.write("\nTime to change the text ;)")
output.close()

#open for writing, fails if the file exists - x
output = open('sample.txt','x')
output.write("some text")
