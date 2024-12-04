import re

with open("./input.txt", 'r') as reader:
    total = 0
    line = reader.readline()
    while line != '':
        matches = []
        matches = re.findall('mul\\(\\d+,\\d+\\)', line)
        for i in range(len(matches)):
            #Remove "mul" substring in each string
            matches[i] = matches[i][3:len(matches[i])]
            #Remove parenthesis so i can work on each pair
            matches[i] = matches[i][1:len(matches[i]) - 1]
    
            a, b = matches[i].split(',')
            total += (int(a) * int(b))
        line = reader.readline()

print(total)



