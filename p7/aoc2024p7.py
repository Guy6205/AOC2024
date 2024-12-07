def count_word_in_grid(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1)
    ]
    
    count = 0

    for row in range(rows):
        for col in range(cols):
            for row_offset, column_offset in directions:
                found = True
                for i in range(word_length):
                    row_offset_n, column_offset_n = row + row_offset * i, col + column_offset * i
                    if not (0 <= row_offset_n < rows and 0 <= column_offset_n < cols) or grid[row_offset_n][column_offset_n] != word[i]:
                        found = False
                        break
                if found:
                    count += 1

    return count

grid = []
word = "XMAS"

with open('p7/data.txt', 'r') as file:
    for line in file:
        grid.append(line.strip()) 
    result = count_word_in_grid(grid, word)
    print(result)
