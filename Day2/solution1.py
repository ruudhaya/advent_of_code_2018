#!/usr/bin/python3

# Finding the checksum
# Number of instances characters repeating twice * repeating thrice

repeatingTwiceCount = 0
repeatingThriceCount = 0
charMap = {}
inputfile = open('Day2/input1.txt', 'r')

for line in inputfile:
    singleCode = line.rstrip()
    # print(singleCode)
    for singleChar in singleCode:
        if singleChar not in charMap:
            charMap[singleChar] = 1
        else:
            charMap[singleChar] += 1

    twiceExists = False
    thriceExists = False

    for k, v in charMap.items():
        if v == 2:
            # print("Twice : " + str(k))
            if not twiceExists:
                repeatingTwiceCount += 1
            twiceExists = True

        elif v == 3:
            # print("Thrice : " + str(k))
            if not thriceExists:
                repeatingThriceCount += 1
            thriceExists = True

    charMap.clear()

inputfile.close()

print("Result:")
print(repeatingTwiceCount * repeatingThriceCount)
