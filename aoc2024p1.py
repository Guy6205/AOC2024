# AOC 2024 Day 1 P1
column1 = []
column2 = []

with open('data.txt', 'r') as file:
    for line in file:
        col1, col2 = map(int, line.split())  
        column1.append(col1)     
        column2.append(col2)

column1.sort(reverse=True)
column2.sort(reverse=True)

total_difference = sum(abs(a - b) for a, b in zip(column1, column2))

print(total_difference)