with open("input.txt") as f:
    lines = f.readlines()

def part1(input):
    bag_contents = {"red": 12, "green": 13, "blue": 14}
    answer = 0 
    for i in range(0, len(lines)):
        line = lines[i]
        id = i + 1
        rounds = line.strip().split(":")[1].strip().split(";")
        possible = True
        for round in rounds:
            moves = round.strip().split(",")
            for move in moves:
                num_cubes = int(move.strip().split(" ")[0])
                color = move.strip().split(" ")[1]
                if num_cubes > bag_contents[color]:
                    possible = False
        if possible:
            answer += id
    print(answer)
                    
def part2(input):
    answer = 0 
    for i in range(0, len(lines)):
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        line = lines[i]
        rounds = line.strip().split(":")[1].strip().split(";")
        for round in rounds:
            moves = round.strip().split(",")
            for move in moves:
                num_cubes = int(move.strip().split(" ")[0])
                color = move.strip().split(" ")[1]
                max_cubes[color] = max(num_cubes, max_cubes[color])
        answer += max_cubes["blue"] * max_cubes["red"] * max_cubes["green"]
    print(answer)
    
part1(lines)
part2(lines)