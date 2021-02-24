# Guided Exploration No. 3
# Barron Jager

# imports the random library
import random
# declare an empty list named possible_names
possible_names = []
# open a new file named rap-names-output.txt
outputFile = open('rap-names-output.txt', 'w')
# opens the rap-names.txt for read access, assigning the handle to dataFile
with open('rap-names.txt', 'r') as dataFile:
    # iterate through each line in the rap-names.txt file
    for name in dataFile:
        # adds name to the possible names list
        # strips off the invisible line-feed that’s at the end of each line
        possible_names.append(name.rstrip())
# prompt the user for the number of rap names to generate
count = int(input('How many rap names would you like to create? '))
# prompt user for how many parts should be part of the entire rap name
parts = int(input('How many parts should the name contain? '))
# loop the number of times needed to create the correct number of rap names
for i in range(count):
    # creates an empty list
    name_parts = []
    # loop the number of times needed to create the correct number of parts to the name
    for j in range(parts):
        # pick a random name from the possible names list and append the name to the name parts list
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
    # write the assembled name to the output file followed by a new line
    outputFile.write(f"{' '.join(name_parts)}\n")
    # display the assembled name
    print(f"{' '.join(name_parts)}")
# close the output file
outputFile.close()
