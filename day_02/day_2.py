input_file_name = 'puzzle2_input.txt'

def part1():
    bag = {
        'red': '12',
        'green': '13',
        'blue': '14'
    }
    sum = 0
    with open(input_file_name) as f:
        lines = f.readlines()
        games = {}
        for l in lines:
            l = l.strip()

            game_parts = l.split(':')
            game_number_parts = game_parts[0].split()
            games[game_number_parts[1]] = []

            game_set_parts = game_parts[1].split(';')
            for set in game_set_parts:
                comma_split = set.split(',')
                new_set = []
                for items in comma_split:
                    dice = items.split()
                    new_set.append(dice)
                games[game_number_parts[1]].append(new_set)
        for id in games:
            for set in games[id]:
                bad_set = False
                for item in set:
                    if int(item[0]) > int(bag[item[1]]):
                        bad_set = True
                        break
                if bad_set:
                    break
            if not bad_set:
                sum += int(id)
            
        print(sum)
def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        games = {}
        for l in lines:
            l = l.strip()

            game_parts = l.split(':')
            game_number_parts = game_parts[0].split()
            games[game_number_parts[1]] = []

            game_set_parts = game_parts[1].split(';')
            for set in game_set_parts:
                comma_split = set.split(',')
                new_set = []
                for items in comma_split:
                    dice = items.split()
                    new_set.append(dice)
                games[game_number_parts[1]].append(new_set)
        power_games = []
        for id in games:
            min_dice = {}
            for set in games[id]:
                for item in set:
                    if item[1] not in min_dice:
                        min_dice[item[1]] = int(item[0])
                    elif min_dice[item[1]] < int(item[0]):
                        min_dice[item[1]] = int(item[0])
            power = 1
            for color, number in min_dice.items():
                power *= number
            power_games.append(power)
        print('Sum', sum(power_games))

part2()