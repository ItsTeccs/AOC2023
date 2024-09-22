with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    hand = line.strip().split(" ")[0]
    bet = line.strip().split(" ")[1]
    print(hand)
    print(bet)

