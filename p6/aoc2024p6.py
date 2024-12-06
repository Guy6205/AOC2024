import re

pattern = r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)"

mul_enabled = True
total = 0

with open('p6/data.txt', 'r') as file:
    text = file.read()

    for match in re.finditer(pattern, text):
        if match.group() == "do()":
            mul_enabled = True  
        elif match.group() == "don't()":
            mul_enabled = False  
        elif match.group(1) and match.group(2) and mul_enabled:
            a, b = int(match.group(1)), int(match.group(2))
            total += a * b

print(total)