#!/usr/bin/python3

# Finding the nearest matching String

# Compare each and every code(word) with all the other word
# Find the best rank, skip the comparision if it is worse than the existing solution


def compareCodesWithRank(singleCode, existingCode, bestRank):
    diffCount = 0
    i = 0
    while i < singleCode.__len__():
        char1 = singleCode[i]
        char2 = existingCode[i]
        i += 1
        if char1 != char2:
            diffCount += 1
        if diffCount > bestRank:
            return diffCount

    return diffCount


def getCommonChars(string1, string2):
    commonChars = ""
    i = 0
    while i < string1.__len__():
        if string1[i] == string2[i]:
            commonChars += string1[i]
        i += 1
    return commonChars


inputfile = open('Day2/input1.txt', 'r')

bestMatch = []
bestRank = -1

allCodes = []

for line in inputfile:
    singleCode = line.rstrip()

    if bestMatch.__len__() < 2:
        bestMatch.append(singleCode)
        bestRank = singleCode.__len__()
        allCodes.append(singleCode)
        continue

    for existingCode in allCodes:
        compareRank = compareCodesWithRank(singleCode, existingCode, bestRank)

        if compareRank < bestRank:
            bestMatch.clear()
            bestMatch.append(existingCode)
            bestMatch.append(singleCode)
            bestRank = compareRank

    allCodes.append(singleCode)

inputfile.close()

commonCode = getCommonChars(bestMatch[0], bestMatch[1])

print(bestMatch)
print(bestRank)
print(commonCode)
