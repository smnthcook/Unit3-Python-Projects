'''
TotalSales
Samantha Cook
4/18/2023
Python II
'''

file = open("sales.txt", "r")
total_revenue = 0

for sale in file:
    total_revenue += float(sale.strip())
    
print("Total Revenue:", total_revenue)
file.close()