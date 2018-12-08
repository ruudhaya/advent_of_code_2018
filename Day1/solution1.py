#!/usr/bin/python3

inputfile = open('input1.txt', 'r')
total = 0
for line in inputfile:
    num = line.rstrip()
    print(num)
    total = total + int(num)

print(total)
