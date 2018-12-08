#!/usr/bin/python3

# Finding the first repeating frequency
currentFrequency = 0
frequencyList = []
recurrenceFound = False

frequencyList.append(currentFrequency)

while recurrenceFound == False:
    inputfile = open('input1.txt', 'r')

    for line in inputfile:
        num = int(line.rstrip())
        currentFrequency = currentFrequency + num
        if(frequencyList.count(currentFrequency) == 1):
            recurrenceFound = True
            print()
            break
        else:
            frequencyList.append(currentFrequency)
            print(currentFrequency)

    inputfile.close()

print(currentFrequency)
