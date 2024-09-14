with open('input.txt') as f:
    lines = f.readlines()

grid = []

def is_symbol(symbol):
    return symbol not in "\n.01234567890"

def symbol_adjacent(row, col):
    # checking above and below
    row_check_offsets = [0]
    if row == 0:
        row_check_offsets.append(1)
    elif row == len(grid) - 1:
        row_check_offsets.append(-1)
    else:
        row_check_offsets.append(1)
        row_check_offsets.append(-1)

    for offset in row_check_offsets:
        for i in range(col - 1, col + 2):
            if col >= 0 and col <= len(grid[row]) - 1:
                char_at = grid[row + offset][i]
                if(is_symbol(char_at)):
                    return True
    
    return False
            
def part1(grid):
    parsing_number = False
    is_part_number = False
    cur_parsing_num = ""
    part_number_sum = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            char_at = grid[row][col]
            if char_at.isnumeric() and not parsing_number:
                parsing_number = True
            elif not char_at.isnumeric() and parsing_number:
                if is_part_number:
                    part_number_sum += int(cur_parsing_num)
                is_part_number = False
                parsing_number = False
                cur_parsing_num = ""
            
            if parsing_number:
                cur_parsing_num += char_at
                if not is_part_number:
                    is_part_number = symbol_adjacent(row, col)
    print(part_number_sum)
for line in lines:
    grid.append(list(line))

part1()
