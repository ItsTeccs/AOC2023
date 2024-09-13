line_number_data = {}
# maps line number to how many matching numbers are in the line
matching_numbers = {}
total_cards_from_line = {}
copied_card_amounts = {}

copied_scratch_cards = 0 

def parse_line(line):
    winning_nums = list(filter(None, line.split(":")[1].strip().split("|")[0].strip().split(" ")))
    my_nums = list(filter(None, line.split(":")[1].strip().split("|")[1].strip().split(" ")))
    
    return {"winning_nums": winning_nums, "my_nums": my_nums}

with open('input.txt') as f:
    lines = f.readlines()

for i in range(0, len(lines)):
    line_data = parse_line(lines[i])
    line_number_data[i + 1] = line_data 
    
    matching = 0
    for num in line_data["my_nums"]:
        if num in line_data["winning_nums"]:
            matching += 1

    matching_numbers[i + 1] = matching

for i in range(len(lines) - 1, -1, -1):
    print("Processing line: " + str(i+1))
    copied_cards_this_line = 0
    line_num = i + 1
    queue = []

    matching_nums = matching_numbers[line_num]
    copied_scratch_cards += matching_nums
    copied_cards_this_line += matching_nums
    for j in range(0, matching_nums):
        queue.append(line_num + j + 1)

    while len(queue) > 0 and (copied_card_amounts.get(queue[len(queue) - 1])):
        copied_scratch_cards += copied_card_amounts[queue[len(queue) - 1]]
        queue.pop(len(queue))

    while len(queue) > 0:
        line_num = queue[0]
        matching_nums = matching_numbers[line_num]
        copied_scratch_cards += matching_nums
        for j in range(0, matching_nums):
            queue.append(line_num + j + 1)
        queue.pop(0)



print(len(lines))
print(copied_scratch_cards + len(lines))