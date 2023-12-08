from math import pow
input_file_name = 'puzzle4_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()

        game_point_total = 0
        for l in lines:
            l = l.strip()

            line_parts = l.split(':')
            game_parts = line_parts[1].split('|')
            
            winning_numbers = game_parts[0].split()
            numbers_you_have = game_parts[1].split()

            matching_numbers = 0
            for number in numbers_you_have:
                if number in winning_numbers:
                    matching_numbers += 1
            
            if matching_numbers > 0:
                game_point_total += pow(2, (matching_numbers - 1))
        print('Game Point Total', game_point_total)
# part1()

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()

        game_point_total = 0
        cards = {}
        for l in lines:
            l = l.strip()

            line_parts = l.split(':')
            card_num_parts = line_parts[0].split()
            card_num = int(card_num_parts[1])
            if card_num not in cards:
                cards[card_num] = 1
            else:
                cards[card_num] += 1

            game_parts = line_parts[1].split('|')
            
            winning_numbers = game_parts[0].split()
            numbers_you_have = game_parts[1].split()

            matching_numbers = 0
            for number in numbers_you_have:
                if number in winning_numbers:
                    matching_numbers += 1
            
            if matching_numbers > 0:
                if cards[card_num] > 1:
                    for j in range(cards[card_num]):
                        for i in range(1, matching_numbers + 1):
                            copy_number = card_num + i
                            if copy_number not in cards:
                                cards[copy_number] = 1
                            else:
                                cards[copy_number] += 1
                else:
                    for i in range(1, matching_numbers + 1):
                        copy_number = card_num + i
                        if copy_number not in cards:
                            cards[copy_number] = 1
                        else:
                            cards[copy_number] += 1
        total_copies = 0
        for v in cards.values():
            total_copies += v
        
        print('Total Copies', total_copies)
part2()
