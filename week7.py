import os
import sys

filename = None
starting_point = 0

if len(sys.argv) < 2:
    print("Needs at least one argument: <filename>")
    exit()

filename = sys.argv[1]
for idx, arg in enumerate (sys.argv):
    if arg in ("- - start" , "-s") :
        starting_point = int(sys.argv[idx + 1])

print("Filename" , filename)
print("Start:" , starting_point)

if os.path.exists(filename):
    print(filename , "already exists")
else:
    print(filename, "file does not exist")

# Get filename
print ("filename) : " + path.split("/")[-1])

filename = input("Enter file name: ") #User must enter a file name be searched.
def letterFrequency(fileName, letter):

    # open file in read mode
    file = open(fileName, 'rt')

    # store content of the file in a variable
    text = file.read()

    # using count()
    return text.count(letter)

# call the function and display the letter count
print(letterFrequency(filename , 'e'))

