input_file_name = 'puzzle7_input.txt'

card_ranking = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}


card_ranking_p2 = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,
    'Q': 12,
    'K': 13,
    'A': 14
}

type_ranking = {
    'highCard': 1,
    'onePair': 2,
    'twoPair': 3,
    'threeOfAKind': 4,
    'fullHouse': 5,
    'fourOfAKind': 6,
    'fiveOfAKind': 7
}

# < returns true
# > returns false
# key < arr[j]
# first_hand < second_hand
def compare_hands(first_hand, second_hand, p2 = False):
    if p2 == True:
        card_ranking = card_ranking_p2

    if first_hand['typeStrength'] < second_hand['typeStrength']:
        return True
    elif first_hand['typeStrength'] > second_hand['typeStrength']:
        return False
    elif first_hand['typeStrength'] == second_hand['typeStrength']:

        for i in range(len(first_hand['hand'])):
            if 'J' not in first_hand['hand'] and 'J' not in second_hand['hand']:
                if card_ranking[first_hand['hand'][i]] < card_ranking[second_hand['hand'][i]]:
                    return True
                elif card_ranking[first_hand['hand'][i]] > card_ranking[second_hand['hand'][i]]:
                    return False
            if card_ranking[first_hand['hand'][i]] < card_ranking[second_hand['hand'][i]]:
                return True
            elif card_ranking[first_hand['hand'][i]] > card_ranking[second_hand['hand'][i]]:
                return False


def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        hands = []
        for l in lines:
            l = l.strip()

            parts = l.split()
            hands.append({ 'hand': parts[0], 'bid': parts[1]})

        for h in hands:
            h['typeStrength'] = -1
            all_c = {}
            for c in h['hand']:
                if c not in all_c:
                    all_c[c] = 1
                else:
                    all_c[c] += 1
            
            if len(all_c.keys()) == 1:
                h['typeStrength'] = type_ranking['fiveOfAKind']

            if len(all_c.keys()) == 2:
                for v in all_c.values():
                    if v == 1 or v == 4:
                        h['typeStrength'] = type_ranking['fourOfAKind']
                    elif v == 2 or v == 3:
                        h['typeStrength'] = type_ranking['fullHouse']
            
            if len(all_c.keys()) == 3:
                if 3 in all_c.values():
                    h['typeStrength'] = type_ranking['threeOfAKind']
                else:
                    h['typeStrength'] = type_ranking['twoPair']
            
            if len(all_c.keys()) == 4:
                h['typeStrength'] = type_ranking['onePair']

            
            if len(all_c.keys()) == 5:
                h['typeStrength'] = type_ranking['highCard']

        
        n = len(hands)

        for i in range(1, n):
            key = hands[i]
            j = i - 1
            while j >= 0 and compare_hands(key, hands[j]):
                hands[j + 1] = hands[j]
                j -= 1
            hands[j + 1] = key
        
        total = 0
        for i in range(len(hands)):
            total = total + (int(hands[i]['bid']) * (i + 1))
        
        print('Total', total)

# part1()

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        hands = []
        for l in lines:
            l = l.strip()

            parts = l.split()
            hands.append({ 'hand': parts[0], 'bid': parts[1]})

        for h in hands:
            h['typeStrength'] = -1
            all_c = {}
            for c in h['hand']:
                if c not in all_c:
                    all_c[c] = 1
                else:
                    all_c[c] += 1
            
            if 'J' in all_c.keys():
                highest_key = ('', -1)
                for k,v in all_c.items():
                    if v > highest_key[1] and k != 'J':
                        highest_key = (k, v)

                if highest_key[0] != '':
                    all_c[highest_key[0]] += all_c['J']
                    del all_c['J']
                
            if len(all_c.keys()) == 1:
                h['typeStrength'] = type_ranking['fiveOfAKind']

            if len(all_c.keys()) == 2:
                for v in all_c.values():
                    if v == 1 or v == 4:
                        h['typeStrength'] = type_ranking['fourOfAKind']
                    elif v == 2 or v == 3:
                        h['typeStrength'] = type_ranking['fullHouse']
            
            if len(all_c.keys()) == 3:
                if 3 in all_c.values():
                    h['typeStrength'] = type_ranking['threeOfAKind']
                else:
                    h['typeStrength'] = type_ranking['twoPair']
            
            if len(all_c.keys()) == 4:
                h['typeStrength'] = type_ranking['onePair']

            
            if len(all_c.keys()) == 5:
                h['typeStrength'] = type_ranking['highCard']

        n = len(hands)

        for i in range(1, n):
            key = hands[i]
            j = i - 1
            while j >= 0 and compare_hands(key, hands[j], True):
                hands[j + 1] = hands[j]
                j -= 1
            hands[j + 1] = key
        
        total = 0
        for i in range(len(hands)):
            total = total + (int(hands[i]['bid']) * (i + 1))
        
        print('Total', total)

part2()