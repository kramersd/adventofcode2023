input_file_name = 'puzzle6_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()

        times = []
        distances = []
        for l in lines:
            l = l.strip()
            
            if 'Time' in l:
                parts = l.split()

                for i in parts:
                    if i != 'Time:':
                        times.append(int(i))
            
            if 'Distance' in l:
                parts = l.split()

                for i in parts:
                    if i != 'Distance:':
                        distances.append(int(i))
        
        races = []
        for i in range(len(times)):
            for j in range(times[i]):
                speed_of_boat = j

                time_left = times[i] - j
                distance_traveled = time_left * speed_of_boat

                races.append({'buttonHeld': speed_of_boat, 'distanceTraveled': distance_traveled, 'race': (times[i], distances[i])})
        
        winning_races = {}
        for r in races:
            if r['distanceTraveled'] > r['race'][1]:
                if r['race'] not in winning_races:
                    winning_races[r['race']] = 1
                else:
                    winning_races[r['race']] = winning_races[r['race']]  + 1
        margin_of_error = 1
        for v in winning_races.values():
            margin_of_error *= v

        print('Margin of Error', margin_of_error)

part1()

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()

        time = ''
        distance = ''
        for l in lines:
            l = l.strip()
            
            if 'Time' in l:
                parts = l.split()

                for i in parts:
                    if i != 'Time:':
                        time += i
            
            if 'Distance' in l:
                parts = l.split()

                for i in parts:
                    if i != 'Distance:':
                        distance += i
        
        time = int(time)
        distance = int(distance)

        winning = 0
        for i in range(time):
            if (i * (time - i)) > distance:
                winning += 1

        print('Number of Ways', winning)

part2()