input_file_name = 'puzzle1_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        numbers = '123456789'
        digits_in_line = []
        sum = 0
        for l in lines:
            l = l.strip()
            if l.strip():
                for i in l:
                    if i in numbers:
                        digits_in_line.append(i)
               
                two_digit = digits_in_line[0] + digits_in_line[len(digits_in_line) - 1]

                sum += int(two_digit)
                digits_in_line = []
        
        print('Sum', sum)

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        numbers = '123456789'
        digits_in_line = []
        sum = 0
        word_number_map = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }

        for l in lines:
            l = l.strip()
            for k,v in word_number_map.items():
                l = l.replace(k, k[0] + v + k[len(k) - 1])
            for i in l:
                if i in numbers:
                    digits_in_line.append(i)
            two_digit = digits_in_line[0] + digits_in_line[len(digits_in_line) - 1]
            sum += int(two_digit)
            digits_in_line = []
            ppp += 1
        print('Sum', sum)
part2()