with open('input.txt') as f:
    lines = f.readlines()

sum = 0
for line in lines:
    winning_nums = list(filter(None, line.split(":")[1].strip().split("|")[0].strip().split(" ")))
    my_nums = list(filter(None, line.split(":")[1].strip().split("|")[1].strip().split(" ")))
    points = 0

    for num in my_nums:
        if num in winning_nums:
            if points == 0:
                points = 1
            else:
              points *= 2
    sum += points

print(sum)