with open ("input.txt") as f:
    lines = f.readlines()

def part1(input):
    answer = 0
    for line in lines:
        cal_num = 0
        digits = []
        for char in line:
            if char.isdigit():
                digits.append(char)
        cal_num = int(digits[0] + digits[-1])
        answer += cal_num
    print(answer)

def part2(input):
    answer = 0
    nums = {"one": '1', "two": '2', "three": '3', "four": '4', "five": '5', "six": '6', "seven": '7', "eight": '8', "nine": '9'}
    for line in lines:
        cal_num = 0
        digits = []
        for i in range(0, len(line)):
            char = line[i]
            if char.isdigit():
                digits.append(char)
            for strnum in nums.keys():
                if line[i:].startswith(strnum):
                    digits.append(nums[strnum])
        cal_num = int(digits[0] + digits[-1])
        answer += cal_num
    print(answer)

part1(lines)
part2(lines)
