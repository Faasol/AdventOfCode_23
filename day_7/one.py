five_of_a_kind = 0
four_of_a_kind = 1
full_house = 2
three_of_a_kind = 3
two_pair = 4
one_pair = 5
high_card = 6

def parse_line(line):
    line.strip()
    partial_result = line.split(" ")
    return partial_result[0], int(partial_result[1])

def get_list_of_hand(hand):
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for char in hand:
        if char == 'A':
            values[0] += 1
        elif char == 'K':
            values[1] += 1
        elif char == 'Q':
            values[2] += 1
        elif char == 'J':
            values[3] += 1
        elif char == 'T':
            values[4] += 1
        else:
            values[len(values) - int(char) + 1] += 1
        
    return values

def check_hand(hand):
    max_value = max(hand)
    match max_value:
        case 5:
            return five_of_a_kind
        case 4:
            return four_of_a_kind
        case 3:
            return full_house if hand.count(2) == 1 else three_of_a_kind
        case 2:
            return two_pair if hand.count(2) == 2 else one_pair
        case _:
            return high_card
        
def get_best_comb(first, second):
    for i in range(len(first)):
        if first[i] == second[i]:   continue
        if first[i] == 'A' and second[i] != 'A':
            return 1
        elif second[i] == 'A' and first[i] != 'A':
            return -1
        elif first[i] == 'K' and second[i] != 'K':
            return 1
        elif second[i] == 'K' and first[i] != 'K':
            return -1
        elif first[i] == 'Q' and second[i] != 'Q':
            return 1
        elif second[i] == 'Q' and first[i] != 'Q':
            return -1
        elif first[i] == 'J' and second[i] != 'J':
            return 1
        elif second[i] == 'J' and first[i] != 'J':
            return -1
        elif first[i] == 'T' and second[i] != 'T':
            return 1
        elif second[i] == 'T' and first[i] != 'T':
            return -1
        elif first[i].isdigit() and second[i].isdigit():
            if int(first[i]) > int(second[i]):
                return 1
            elif int(second[i]) > int(first[i]):
                return -1

def sort_hands(hands, bids):
    for i in range(len(hands)):
        smallIdx = i
        hand = hands[i]
        priority = check_hand(get_list_of_hand(hands[i]))
        for j in range(i+1, len(hands)):
            second_hand = hands[j]
            second_priority = check_hand(get_list_of_hand(hands[j]))
            if (second_priority > priority) or (second_priority == priority and get_best_comb(hand, second_hand) == 1):
                priority = second_priority
                hand = second_hand
                smallIdx = j
        if smallIdx != i:
            tmp = hands[i]
            hands[i] = hands[smallIdx]
            hands[smallIdx] = tmp
            tmp = bids[i]
            bids[i] = bids[smallIdx]
            bids[smallIdx] = tmp

def get_result(hands, bids):
    result = 0
    sort_hands(hands, bids)
    
    for i, bid in enumerate(bids):
        result += bid * (i+1)
    
        
    return result

def main():
    
    hands = []
    bids = []
   
    file = open('input.txt', 'r')
    lines = file.readlines()
    for line in lines:
        hand, bid = parse_line(line)
        hands.append(hand)
        bids.append(bid)

       
    print("\n * \t -> \t" + str(get_result(hands, bids)) + "\n")
    
if __name__ == '__main__':    
    main()