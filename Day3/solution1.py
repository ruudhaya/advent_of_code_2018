#!/usr/bin/python3

#
# In 1000 * 1000 Matrix, how many cells will overlap with given squares
# DataFormat: #123 @ 3,2: 4x4

totalWidth = 1000
totalHeight = 1000

arr = [['.'] * totalWidth for i in range(totalHeight)]

inputfile = open('Day3/input.txt', 'r')

for line in inputfile:
    inputLine = line.rstrip()
    print(inputLine)
    str1 = inputLine.split('@')[1].strip()
    str2 = str1.split(',')
    left = int(str2[0])
    str3 = str2[1].split(':')
    top = int(str3[0])
    str4 = str3[1].strip().split('x')
    rightCorner = int(str4[0]) + left
    bottomCorner = int(str4[1]) + top

    # Fill the area of the rectangle with '#'
    for i in range(rightCorner - left):
        x = left + i
        for j in range(bottomCorner - top):
            y = top + j
            if arr[y][x] == '.':
                arr[y][x] = '@'
            elif arr[y][x] == '@':
                arr[y][x] = '#'

inputfile.close()

count = 0
for i in range(totalWidth):
    for j in range(totalHeight):
        if arr[i][j] == '#':
            count += 1

# for row in arr:
#     print(' '.join([str(elem) for elem in row]))

print("Result:")
print(len(arr))
print(len(arr[3]))
print(count)
