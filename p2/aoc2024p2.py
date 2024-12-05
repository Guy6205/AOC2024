# AOC 2024 Day 1 P2
column1 = []
column2 = []

with open('p2/data.txt', 'r') as file:
    for line in file:
        col1, col2 = map(int, line.split())  
        column1.append(col1)     
        column2.append(col2)

similarity_score = sum((number * column2.count(number)) for number in column1)

print(similarity_score)