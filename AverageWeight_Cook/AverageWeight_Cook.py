'''
AverageWeight
Samantha Cook
4/18/2023
Python II
'''

file = open("weights.txt", "r")
total_weight = 0
count = 0
for weight in file:
    total_weight += int(weight.strip())
    count += 1
average = total_weight / count
print("Average Weight:", average)
file.close()