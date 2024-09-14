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

def nums_adjacent(row, col):
    # checking above and below
    adj_nums = []
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
                val = part_num_positions.get((row + offset, i))
                if val and val not in adj_nums:
                    adj_nums.append(val)
                char_at = grid[row + offset][i]
    
    return adj_nums

with open('input.txt') as f:
    lines = f.readlines()

grid = []
part_num_positions = {}

for line in lines:
    grid.append(list(line))

parsing_number = False
is_part_number = False
cur_parsing_num = ""
cur_part_positions = []
gear_ratio_sum = 0
for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        char_at = grid[row][col]
        if char_at.isnumeric() and not parsing_number:
            parsing_number = True
        elif not char_at.isnumeric() and parsing_number:
            if is_part_number:
                for pos in cur_part_positions:
                    part_num_positions[pos] = int(cur_parsing_num)
            cur_part_positions.clear()
            is_part_number = False
            parsing_number = False
            cur_parsing_num = ""

        if parsing_number:
            cur_part_positions.append((row, col))
            cur_parsing_num += char_at
            if not is_part_number:
                is_part_number = symbol_adjacent(row, col)

for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        char_at = grid[row][col]
        if is_symbol(char_at):
            nums = nums_adjacent(row, col)
            if char_at == '*' and len(nums) == 2:
                # print("Gear Ratio found at:\nrow: " + str(row) + "\ncol: " + str(col))
                gear_ratio_sum += (nums[0] * nums[1])
    
    print(gear_ratio_sum)
