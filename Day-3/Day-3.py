import re

matches = []
quote = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
matches = re.findall('mul\\(\\d+,\\d+\\)', quote)
total = 0
for i in range(len(matches)):
    matches[i] = matches[i][3:len(matches[i])]
    #print(matches[i])
    matches[i] = matches[i][1:len(matches[i]) - 1]
    #print(matches[i])
    a, b = matches[i].split(',')
    total += int(a) * int(b)
    
print(total)



