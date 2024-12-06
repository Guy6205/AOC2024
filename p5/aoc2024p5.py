import re

pattern = r'mul\((\d+),(\d+)\)'

with open('p5/data.txt', 'r') as file:
    text = file.read()
    matches = re.findall(pattern, text)

    total = 0
    for a, b in matches:
        total += int(a) * int(b)

print(total)