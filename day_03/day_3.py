input_file_name = 'puzzle3_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()
        i = 1
        engine_parts = []
        prev_line = {}

        for l in lines:
            l = l.strip()

            symbols_discovered = []
            numbers_discovered = []
            
            line_engine_parts = []
            temp_num = ''
            prev_symbol = False

            for j in range(len(l)):
                if l[j] in '0123456789':
                    temp_num += l[j]
                    if j == len(l) - 1 and prev_symbol:
                        line_engine_parts.append({'line': i,'position': j, 'numberOrSymbol': temp_num})
                elif l[j] != '.':
                    symbols_discovered.append({'line': i, 'position': j, 'numberOrSymbol': l[j]})
                    if temp_num != '':
                        line_engine_parts.append({'line': i,'position': j, 'numberOrSymbol': temp_num})
                        numbers_discovered.append({'line': i,'position': j, 'numberOrSymbol': temp_num})
                    temp_num = ''
                    prev_symbol = True
                elif l[j] == '.':
                    if temp_num != '':
                        numbers_discovered.append({'line': i,'position': j - len(temp_num), 'numberOrSymbol': temp_num})
                        if prev_symbol:
                            line_engine_parts.append({'line': i,'position': j - len(temp_num), 'numberOrSymbol': temp_num})
                    prev_symbol = False
                    temp_num = ''
            if temp_num != '':
                numbers_discovered.append({'line': i,'position': j - len(temp_num), 'numberOrSymbol': temp_num})

            engine_parts.extend(line_engine_parts)

            i += 1
            evaluating_previous_symbol_engine_parts = []
            if prev_line != {}:
                print('Previous Line', prev_line)
                for symbol_entry in prev_line['symbolsDiscovered']:
                    for k,v in symbol_entry.items():
                        print(k, v)
                    
                    for number_entry in numbers_discovered:
                        number_positions = [number_entry['position']]
                        for k,v in number_entry.items():
                            print(k, v)
                        if len(number_entry['numberOrSymbol']) > 1:
                            number_positions = [int(number_entry['position']) + x for x in range(len(number_entry['numberOrSymbol']))]
                        print('Number Positions', sorted(number_positions))
                        
                        if number_entry not in engine_parts:
                            if symbol_entry['position'] in number_positions:
                                engine_parts.append(number_entry)
                                evaluating_previous_symbol_engine_parts.append(number_entry)
                            elif symbol_entry['position'] + 1 in number_positions:
                                engine_parts.append(number_entry)
                                evaluating_previous_symbol_engine_parts.append(number_entry)
                            elif symbol_entry['position'] - 1 in number_positions:
                                engine_parts.append(number_entry)
                                evaluating_previous_symbol_engine_parts.append(number_entry)
                
                for symbol_entry in symbols_discovered:
                    for k,v in symbol_entry.items():
                        print(k, v)

                    for number_entry in prev_line['numbersDiscovered']:
                        print('--- Evaluating Number in context of Symbol -- ')
                        number_positions = [number_entry['position']]
                        for k,v in number_entry.items():
                            print(k, v)
                        if len(number_entry['numberOrSymbol']) > 1:
                            number_positions = [int(number_entry['position']) + x for x in range(len(number_entry['numberOrSymbol']))]
                        
                        if number_entry not in engine_parts:
                            if symbol_entry['position'] in number_positions:
                                engine_parts.append(number_entry)
                                evaluating_previous_symbol_engine_parts.append(number_entry)
                            elif symbol_entry['position'] + 1 in number_positions:
                                engine_parts.append(number_entry)
                                evaluating_previous_symbol_engine_parts.append(number_entry)
                            elif symbol_entry['position'] - 1 in number_positions:
                                engine_parts.append(number_entry)
                                evaluating_previous_symbol_engine_parts.append(number_entry)



            prev_line = {'fullLine': l, 'numbersDiscovered': numbers_discovered, 'symbolsDiscovered': symbols_discovered}

        engine_part_symbols = []
        for e in engine_parts:
            engine_part_symbols.append(e['numberOrSymbol'])
        # print('Engine Part Symbols', engine_part_symbols)
        print('Sum', sum([int(x) for x in engine_part_symbols]))

part1()

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()
        i = 1
        engine_parts = []

        all_lines = []

        for l in lines:
            l = l.strip()

            symbols_discovered = []
            numbers_discovered = []

            temp_num = ''

            for j in range(len(l)):
                if l[j] in '0123456789':
                    temp_num += l[j]
                elif l[j] != '.':
                    symbols_discovered.append({'line': i, 'position': j, 'numberOrSymbol': l[j]})
                    if temp_num != '':
                        print('Temp num D', temp_num)
                        numbers_discovered.append({'line': i,'position': j - len(temp_num), 'numberOrSymbol': temp_num})
                    temp_num = ''
                elif l[j] == '.':
                    if temp_num != '':
                        print('Temp num B', temp_num)
                        numbers_discovered.append({'line': i,'position': j - len(temp_num), 'numberOrSymbol': temp_num})
                    temp_num = ''
            if temp_num != '':
                print('Temp num C', temp_num)
                numbers_discovered.append({'line': i,'position': j - len(temp_num), 'numberOrSymbol': temp_num})

            i += 1
            all_lines.append({'lineNumber': i, 'numbersDiscovered': numbers_discovered, 'symbolsDiscovered': symbols_discovered})

        parsed_symbols = {}
        for i in range(len(all_lines)):
            for symbol_entry in all_lines[i]['symbolsDiscovered']:
                if symbol_entry['numberOrSymbol'] == '*':
                    # skipping if * in first or last line due to manually checking puzzle input

                    # line above
                    for number_entry in all_lines[i - 1]['numbersDiscovered']:
                        number_positions = [number_entry['position']]
                        if len(number_entry['numberOrSymbol']) > 1:
                            number_positions = [int(number_entry['position']) + x for x in range(len(number_entry['numberOrSymbol']))]
                        print('Number positions', number_positions)
                        if symbol_entry['position'] in number_positions:
                            dict_key = (symbol_entry['line'], symbol_entry['position'], symbol_entry['numberOrSymbol'])
                            if  dict_key not in parsed_symbols:
                                parsed_symbols[dict_key] = [number_entry]
                            else:
                                parsed_symbols[dict_key].append(number_entry)
                        elif symbol_entry['position'] - 1 in number_positions:
                            dict_key = (symbol_entry['line'], symbol_entry['position'], symbol_entry['numberOrSymbol'])
                            if  dict_key not in parsed_symbols:
                                parsed_symbols[dict_key] = [number_entry]
                            else:
                                 parsed_symbols[dict_key].append(number_entry)
                        elif symbol_entry['position'] + 1 in number_positions:
                            dict_key = (symbol_entry['line'], symbol_entry['position'], symbol_entry['numberOrSymbol'])
                            if  dict_key not in parsed_symbols:
                                parsed_symbols[dict_key] = [number_entry]
                            else:
                                parsed_symbols[dict_key].append(number_entry)

                    # line below
                    for number_entry in all_lines[i + 1]['numbersDiscovered']:
                        number_positions = [number_entry['position']]
                        if len(number_entry['numberOrSymbol']) > 1:
                            number_positions = [int(number_entry['position']) + x for x in range(len(number_entry['numberOrSymbol']))]
                        
                        # print('Number positions', number_positions)
                        if symbol_entry['position'] in number_positions:
                            dict_key = (symbol_entry['line'], symbol_entry['position'], symbol_entry['numberOrSymbol'])
                            if  dict_key not in parsed_symbols:
                                parsed_symbols[dict_key] = [number_entry]
                            else:
                                parsed_symbols[dict_key].append(number_entry)
                        elif symbol_entry['position'] - 1 in number_positions:
                            dict_key = (symbol_entry['line'], symbol_entry['position'], symbol_entry['numberOrSymbol'])
                            if  dict_key not in parsed_symbols:
                                parsed_symbols[dict_key] = [number_entry]
                            else:
                                parsed_symbols[dict_key].append(number_entry)
                        elif symbol_entry['position'] + 1 in number_positions:
                            dict_key = (symbol_entry['line'], symbol_entry['position'], symbol_entry['numberOrSymbol'])
                            if  dict_key not in parsed_symbols:
                                parsed_symbols[dict_key] = [number_entry]
                            else:
                                parsed_symbols[dict_key].append(number_entry)

                    # inline
                    for number_entry in all_lines[i]['numbersDiscovered']:
                        
                        number_positions = [number_entry['position']]
                        if len(number_entry['numberOrSymbol']) > 1:
                            number_positions = [int(number_entry['position']) + x for x in range(len(number_entry['numberOrSymbol']))]
                        
                        if symbol_entry['position'] - 1 in number_positions:
                            dict_key = (symbol_entry['line'], symbol_entry['position'], symbol_entry['numberOrSymbol'])
                            if  dict_key not in parsed_symbols:
                                parsed_symbols[dict_key] = [number_entry]
                            else:
                                parsed_symbols[dict_key].append(number_entry)
                        elif symbol_entry['position'] + 1 in number_positions:
                            dict_key = (symbol_entry['line'], symbol_entry['position'], symbol_entry['numberOrSymbol'])
                            if  dict_key not in parsed_symbols:
                                parsed_symbols[dict_key] = [number_entry]
                            else:
                                parsed_symbols[dict_key].append(number_entry)

        running_sum = 0
        for k in parsed_symbols.keys():
            if len(parsed_symbols[k]) == 2:
                running_sum = running_sum + (int(parsed_symbols[k][0]['numberOrSymbol']) * int(parsed_symbols[k][1]['numberOrSymbol']))
        print('Running Sum', running_sum)
part2()