'''
GradePercentages
Samantha Cook
4/19/2023
Python II
'''

file = open("scores.txt", "w")
max_points = int(input("Enter the maximum points possible on the assessment >> "))

for points_earned in range(max_points, -1, -1):
    percentage = (points_earned / max_points) * 100
    file.write(str(points_earned) + "/" + str(max_points) + " = " + str(percentage) + "\n")
file.close()