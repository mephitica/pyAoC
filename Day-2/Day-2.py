#First condition of the task
def safe1(numbers: list):
    safe = 0
    for i in range(len(numbers) - 1):
        if (abs(numbers[i] - numbers[i + 1]) >= 1 and abs(numbers[i] - numbers[i + 1]) <= 3 and numbers[i] > numbers[i+1]):
            safe += 1
    if safe == len(numbers) - 1:
        return True

#Second condition of the task
def safe2(numbers: list):
    safe = 0
    for i in range(len(numbers) - 1):
        if (abs(numbers[i] - numbers[i + 1]) >= 1 and abs(numbers[i] - numbers[i + 1]) <= 3 and numbers[i] < numbers[i+1]):
            safe += 1
    if safe == len(numbers) - 1:
        return True

#See if the previous false condition can become true by removing each time an item from the list
def safe3(unsafe_list: list):
    for i in range(len(collect)):
        n = collect.pop(i)
        if safe1(collect) or safe2(collect):
            return True
        collect.insert(i, n)

            

total_safe = 0
unsafe = []
with open('./input.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        numbers = line.split()
        
        #Convert list of strings in a list of int
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        
        if safe1(numbers) or safe2(numbers):
            total_safe += 1
        else:
            unsafe.append(numbers)
        line = reader.readline()

for collect in unsafe:
    if safe3(collect):
        total_safe += 1

print(total_safe)