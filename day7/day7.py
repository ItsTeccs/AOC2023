with open("input.txt") as f:
    lines = f.readlines()

def sort_hands(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and compare_hands(key[0], arr[j][0]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def get_card_strength(ch):
    card_strengths = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    return card_strengths.index(ch)

def compare_hands(a, b):
    type_a = get_hand_type(get_cards(a))
    type_b = get_hand_type(get_cards(b))
    # returns true if a < b
    hand_strengths = {
        "fivekind": 7,
        "fourkind": 6,
        "fullhouse": 5,
        "threekind": 4,
        "twopair": 3,
        "pair": 2,
        "highcard": 1
    }
    card_strengths = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    
    # check hand types for strengths
    if hand_strengths[type_a] < hand_strengths[type_b]:
        return True
    elif hand_strengths[type_a] > hand_strengths[type_b]:
        return False

    for i in range (0, 5):
        if card_strengths.index(a[i]) < card_strengths.index(b[i]):
            return True
        elif card_strengths.index(a[i]) > card_strengths.index(b[i]):
            return False

def get_hand_type(cards):
    pairs = 0
    three_kind = 0
    for key in cards.keys():
        if cards[key] == 2:
            pairs += 1
        elif cards[key] == 3:
            three_kind += 1
        elif cards[key] == 4:
            return "fourkind"
        elif cards[key] == 5:
            return "fivekind"
    if pairs == 2:
        return "twopair"
    elif pairs == 1 and three_kind == 1:
        return "fullhouse"
    elif three_kind == 1:
        return "threekind"
    elif pairs == 1:
        return "pair"
    else:
        return "highcard"

def get_cards(hand):
    occurs = {}
    for char in hand:
        if char in occurs:
            occurs[char] += 1
        else:
            occurs[char] = 1
    return occurs

def part1(lines):
    answer = 0 
    # store all of the hands of the different types
    hands = {
        "fivekind": [],
        "fourkind": [],
        "fullhouse": [],
        "threekind": [],
        "twopair": [],
        "pair": [],
        "highcard": [],
    }

    for line in lines:
        hand = line.strip().split(" ")[0]
        bet = line.strip().split(" ")[1]
        hand_data = (hand, bet, get_hand_type(get_cards(hand)))
        hands[hand_data[2]].append(hand_data)

    for hand_type in hands.keys():
        hand_type_data = hands[hand_type]
        if hand_type_data:
            hand_type_data = sort_hands(hand_type_data)
            hands[hand_type] = hand_type_data
    
    # compose hands into main list
    hand_data_list = []
    for hand in hands["highcard"]:
        hand_data_list.append(hand)
    for hand in hands["pair"]:
        hand_data_list.append(hand)
    for hand in hands["twopair"]:
        hand_data_list.append(hand)
    for hand in hands["threekind"]:
        hand_data_list.append(hand)
    for hand in hands["fullhouse"]:
        hand_data_list.append(hand)
    for hand in hands["fourkind"]:
        hand_data_list.append(hand)
    for hand in hands["fivekind"]:
        hand_data_list.append(hand)

    for i in range(0, len(hand_data_list)):
        data = hand_data_list[i]
        answer += int(data[1]) * (i + 1)
    print(answer)

def calc_jokers(hand):
    print("----")
    print(hand)
    cards = get_cards(hand)
    highest = 0
    highest_strength = 0 
    most_frequent_card = ''
    for key in cards.keys():
        if cards[key] >= highest and get_card_strength(key) > highest_strength and cards[key] != 'J':
            highest_strength = get_card_strength(key)
            highest = cards[key]
            most_frequent_card = key

    hand = hand.replace("J", most_frequent_card)

    print(hand)
    print("----")
    return hand

def part2(lines):
    answer = 0 
    # store all of the hands of the different types
    hands = {
        "fivekind": [],
        "fourkind": [],
        "fullhouse": [],
        "threekind": [],
        "twopair": [],
        "pair": [],
        "highcard": [],
    }

    for line in lines:
        hand = line.strip().split(" ")[0]
        bet = line.strip().split(" ")[1]
        calced_hand = calc_jokers(hand)
        hand_data = (calced_hand, bet, get_hand_type((get_cards(calced_hand))))
        hands[hand_data[2]].append(hand_data)

    for hand_type in hands.keys():
        hand_type_data = hands[hand_type]
        if hand_type_data:
            hand_type_data = sort_hands(hand_type_data)
            hands[hand_type] = hand_type_data
    
    # compose hands into main list
    hand_data_list = []
    for hand in hands["highcard"]:
        hand_data_list.append(hand)
    for hand in hands["pair"]:
        hand_data_list.append(hand)
    for hand in hands["twopair"]:
        hand_data_list.append(hand)
    for hand in hands["threekind"]:
        hand_data_list.append(hand)
    for hand in hands["fullhouse"]:
        hand_data_list.append(hand)
    for hand in hands["fourkind"]:
        hand_data_list.append(hand)
    for hand in hands["fivekind"]:
        hand_data_list.append(hand)

    for i in range(0, len(hand_data_list)):
        data = hand_data_list[i]
        answer += int(data[1]) * (i + 1)
    print(answer)
part1(lines)
part2(lines)
