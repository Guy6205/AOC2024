def count_x_patterns(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    pattern_count = 0

    diagonals = [
        [(-1, -1), (1, 1)],
        [(-1, 1), (1, -1)]
    ]

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'A':
                valid_pattern = True

                for diagonal in diagonals:
                    diagonal_chars = []
                    for row_offset, column_offset in diagonal:
                        row_offset_n, column_offset_n = row + row_offset, col + column_offset
                        if 0 <= row_offset_n < rows and 0 <= column_offset_n < cols:
                            diagonal_chars.append(grid[row_offset_n][column_offset_n])
                        else:
                            diagonal_chars.append(None)

                    if diagonal_chars != ['M', 'S'] and diagonal_chars != ['S', 'M']:
                        valid_pattern = False
                        break

                if valid_pattern:
                    pattern_count += 1

    return pattern_count

grid = []

with open('p8/data.txt', 'r') as file:
    for line in file:
        grid.append(line.strip()) 
    result = count_x_patterns(grid)
    print(result)
