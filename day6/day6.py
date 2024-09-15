with open ("input.txt") as f:
    lines = f.readlines()

def calc_ways(time, distance):
    ways = 0 
    for i in range(1, time):        
        time_remaining = time - i
        if (time_remaining * i) > distance:
            ways += 1
    return ways

def part2(input):
    time = int("".join(list(filter(None, lines[0].split(":")[1].strip().split(" ")))))
    distance = int("".join(list(filter(None, lines[1].split(":")[1].strip().split(" ")))))

    print(calc_ways(time, distance))

def part1(input):
    times = list(filter(None, lines[0].split(":")[1].strip().split(" ")))
    distances = list(filter(None, lines[1].split(":")[1].strip().split(" ")))

    answer = 0 
    for time in times:
        for distance in distances:
            if answer == 0:
                answer = calc_ways(int(time), int(distance))
            else:
                answer *= calc_ways(int(time), int(distance))

    print(answer)

part1(lines)
part2(lines)