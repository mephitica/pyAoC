left_list = []
right_list = []

with open('./input.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        x, y = line.split()
        left_list.append(int(x))
        right_list.append(int(y))
        line = reader.readline()

left_list.sort()
right_list.sort()

total_distance = 0

for i in range(len(left_list)):
    if left_list[i] >= right_list[i]:
        total_distance += (left_list[i] - right_list[i])
    else:
        total_distance += (right_list[i] - left_list[i])
print(total_distance)

sim_score = 0
for i in left_list:
    count = right_list.count(i)
    sim_score += i * count
print(sim_score)
