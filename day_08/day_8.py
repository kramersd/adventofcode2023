input_file_name = 'puzzle8_input.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()

        i = 0
        steps = ''
        nodes = {}
        for l in lines:
            l = l.strip()

            if i == 0:
                steps = l
                i += 1
            
            if '=' in l:
                parts = l.split('=')
                # print('Parts', parts)
                left_and_right = parts[1].strip().replace('(', '').replace(')', '').split(',')
                nodes[parts[0].strip()] = (left_and_right[0].strip(), left_and_right[1].strip())
            
        j = 1
        current_node = 'AAA'
        # print('Nodes', nodes)
        while current_node not in ['ZZZ']:
            # print('--------------------------------------')
            for s in steps:
                # print('S')
                if s == 'R':
                    # print('currentNode BR', current_node)
                    current_node = nodes[current_node][1]
                    # print('currentNode R', current_node)
                    if current_node in 'ZZZ':
                        break
                    j += 1
                elif s == 'L':
                    # print('currentNode BL', current_node)
                    current_node = nodes[current_node][0]
                    # print('currentNode L', current_node)
                    if current_node in 'ZZZ':
                        break
                    j += 1
                # else:
                    # print('Awkward')
            # print('More Steps?')
            # print('After break Current Node', current_node)
        print('Steps', j)

# part1()

def nodes_do_not_end_with_z(nodes):
    # print('------Processing while condition')
    for n in nodes:
        if not n.endswith('Z'):
            return True
    return False

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()

        i = 0
        steps = ''
        nodes = {}

        starting_nodes = []
        all_nodes =[]

        for l in lines:
            l = l.strip()

            if i == 0:
                steps = l
                i += 1
            
            if '=' in l:
                parts = l.split('=')
                # print('Parts', parts)
                left_and_right = parts[1].strip().replace('(', '').replace(')', '').split(',')
                nodes[parts[0].strip()] = (left_and_right[0].strip(), left_and_right[1].strip())
        
                if parts[0].strip().endswith('A'):
                    starting_nodes.append(parts[0].strip())
        
        # print('Starting Nodes', starting_nodes)
        # print('Nodes', nodes)
        # print('All Nodes', all_nodes)

        all_nodes.extend(starting_nodes)

        # print('All Nodes Extended', all_nodes)
        
        j = 0
        current_step_i = 0
        while nodes_do_not_end_with_z(all_nodes):
            # print('J', j)
            # print('current step i', current_step_i)
            output_nodes = []
            for an in all_nodes:
                # print('Considering Node', an)
                current_step_direction = steps[current_step_i]
                if current_step_direction == 'R':
                    output_nodes.append(nodes[an][1])
                elif current_step_direction == 'L':
                    output_nodes.append(nodes[an][0])
            # print('Output Nodes', output_nodes)
            j += 1
            current_step_i += 1
            # print('After current step i', current_step_i)
            if current_step_i > len(steps) - 1:
                # print('Resetting')
                current_step_i = 0
            all_nodes = output_nodes
            # if j > 5:
            #     break
        
        print('Processed', all_nodes)
        print('Steps', j)

part2()