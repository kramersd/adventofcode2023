
input_file_name = 'puzzle5_input_01.txt'

def part1():
    with open(input_file_name) as f:
        lines = f.readlines()

        seed_props = []
        maps = {}
        current_map = ''

        for l in lines:
            l = l.strip()

            if 'seeds' in l:
                line_parts = l.split(':')
                seed_numbers = line_parts[1].split()
                for seed_num in seed_numbers:
                    # seed_props[seed_num] = {}
                    seed_props.append({'seed': int(seed_num)})
                # print('Seed Props', seed_props)
            elif 'map:' in l:
                map_parts = l.split()
                properties_parts = map_parts[0].split('-')
                maps[properties_parts[0]] = {'destination': properties_parts[2]}
                current_map = properties_parts[0]
            elif l != '':
                if 'mappings' not in maps[current_map]:
                    mappings = []
                    nums = l.split()
                    mappings.append({'destinationRangeStart': int(nums[0]), 'sourceRangeStart': int(nums[1]), 'rangeLength': int(nums[2])})
                    maps[current_map]['mappings'] = mappings
                else:
                    nums = l.split()
                    maps[current_map]['mappings'].append({'destinationRangeStart': int(nums[0]), 'sourceRangeStart': int(nums[1]), 'rangeLength': int(nums[2])})
                    maps[current_map]['mappings']
            elif l == '':
                current_map = ''

        traversal_ordering = ['seed']
        x = ['seed']
        while len(x) > 0:
            current = x.pop()
            if current == 'location':
                continue
            traversal_ordering.append(maps[current]['destination'])
            x.append(maps[current]['destination'])
        print('Traversal Ordering', traversal_ordering)

        print('---------- Seed properties ----------')
        print(seed_props)
        print('---------- Maps ----------')
        for k,v in maps.items():
            print(k, v)

        
        for seed in seed_props:
            print('Seed', seed)
            for traversal in traversal_ordering:
                if traversal == traversal_ordering[len(traversal_ordering) - 1]:
                    continue
                value_at_traversal = seed[traversal]
                for traversal_mapping in maps[traversal]['mappings']:
                    offset = 0
                    if value_at_traversal >= traversal_mapping['sourceRangeStart'] and value_at_traversal <= traversal_mapping['sourceRangeStart'] + traversal_mapping['rangeLength'] - 1:
                        offset = value_at_traversal - traversal_mapping['sourceRangeStart']
                        seed[maps[traversal]['destination']] = traversal_mapping['destinationRangeStart'] + offset
                if not maps[traversal]['destination'] in seed:
                    seed[maps[traversal]['destination']] = value_at_traversal
            
        print('---------- Transformed Seed properties ----------')
        locations = []
        for sp in seed_props:
            print(sp)
            locations.append(sp['location'])
        print('Min location', min(locations))

# part1()

def part2():
    with open(input_file_name) as f:
        lines = f.readlines()

        seed_props = []
        maps = {}
        current_map = ''

        for l in lines:
            l = l.strip()

            if 'seeds' in l:
                line_parts = l.split(':')
                seed_numbers = line_parts[1].split()
                for i in range(0, len(seed_numbers), 2):
                    seed_props.append({'seed': [(int(seed_numbers[i]), int(seed_numbers[i]) + int(seed_numbers[i + 1]) - 1)]})
            elif 'map:' in l:
                map_parts = l.split()
                properties_parts = map_parts[0].split('-')
                maps[properties_parts[0]] = {'destination': properties_parts[2]}
                current_map = properties_parts[0]
            elif l != '':
                if 'mappings' not in maps[current_map]:
                    mappings = []
                    nums = l.split()
                    mappings.append({'destinationRangeStart': int(nums[0]), 'sourceRangeStart': int(nums[1]), 'rangeLength': int(nums[2])})
                    maps[current_map]['mappings'] = mappings
                else:
                    nums = l.split()
                    maps[current_map]['mappings'].append({'destinationRangeStart': int(nums[0]), 'sourceRangeStart': int(nums[1]), 'rangeLength': int(nums[2])})
                    maps[current_map]['mappings']
            elif l == '':
                current_map = ''

        traversal_ordering = ['seed']
        x = ['seed']
        while len(x) > 0:
            current = x.pop()
            if current == 'location':
                continue
            traversal_ordering.append(maps[current]['destination'])
            x.append(maps[current]['destination'])
        print('---------- Traversal Ordering ----------')
        print(traversal_ordering)
        print('---------- Seed properties ----------')
        print(seed_props)
        print('---------- Maps ----------')
        for k,v in maps.items():
            print(k, v)
        
        
        for seed in seed_props:
            print('-------- Current evaluating seed ----------', seed)
            for traversal in traversal_ordering:
                print('Processing traversal type:', traversal)
                if traversal == traversal_ordering[len(traversal_ordering) - 1]:
                    continue

                ranges_at_traversal = seed[traversal]
                print('Ranges List', ranges_at_traversal)

                split_seed_ranges = {}
                transformed_seed_ranges = []
                for traversal_mapping in maps[traversal]['mappings']:
                    print('Traversal_mapping', traversal_mapping)
                    
                    for current_seed_range in ranges_at_traversal:
                        print('Current range', current_seed_range)
                        print('sourceRangeStart', traversal_mapping['sourceRangeStart'])
                        print('sourceRangeEnd', traversal_mapping['sourceRangeStart'] + traversal_mapping['rangeLength'] - 1)
                        print('rangeLength', traversal_mapping['rangeLength'])

                        source_range_start = traversal_mapping['sourceRangeStart']
                        source_range_end = traversal_mapping['sourceRangeStart'] + traversal_mapping['rangeLength'] - 1
                        destination_range_start = traversal_mapping['destinationRangeStart']

                        if current_seed_range[0] >= source_range_start and current_seed_range[1] <= source_range_end:
                            print('Seed range all within mapping range')
                            offset_start = current_seed_range[0] - source_range_start
                            offset_end = current_seed_range[1] - source_range_start

                            split_seed_ranges[current_seed_range] = {'processed': True}
                            print('Split seed ranges', split_seed_ranges)
                            transformed_seed_ranges.append((destination_range_start + offset_start, destination_range_start + offset_end))
                            print('Transformed Seed Ranges', transformed_seed_ranges)
                        else:
                            print('Overlap either left or right or none')
                            if current_seed_range[0] <= source_range_start and current_seed_range[1] >= source_range_start and current_seed_range[1] <= source_range_end:
                                print('>Overlap Left')
                                current_seed_start_to_source_range_start = (current_seed_range[0], source_range_start)
                                source_range_start_to_current_seed_end = (source_range_start, current_seed_range[1])
                                if current_seed_start_to_source_range_start not in split_seed_ranges:
                                    split_seed_ranges[current_seed_start_to_source_range_start] = {'processed': False}
                                split_seed_ranges[source_range_start_to_current_seed_end] = {'processed': True}
                                transformed_seed_ranges.append(source_range_start_to_current_seed_end)

                                print('Split seed ranges', split_seed_ranges)
                                print('Transformed Seed Ranges', transformed_seed_ranges)

                            elif current_seed_range[0] >= source_range_start and current_seed_range[0] <= source_range_end and current_seed_range[1] > source_range_end:
                                print('>Overlap Right')
                            elif current_seed_range[0] < source_range_start and current_seed_range[1] < source_range_start:
                                print('>Outside to the left of the range')
                                continue
                            elif current_seed_range[0] > source_range_end and current_seed_range[1] > source_range_start:
                                print('>Outside to the right of range')
                                continue
                            else:
                                print('UNKNOWN OR OTHER')
                
                print('########## I HAVE THE HIGH GROUND ##########')
                print('---Only processed seed-to-soil, then break')
                print('---Current seed', seed)
                print('---Split seed ranges', split_seed_ranges)
                print('---Transformed Seed Ranges', transformed_seed_ranges)
                print('###########################################')

                # return
                break


        # for seed in seed_props:
        #     print('Seed', seed)
        #     for traversal in traversal_ordering:
        #         if traversal == traversal_ordering[len(traversal_ordering) - 1]:
        #             continue
        #         value_at_traversal = seed[traversal]
        #         for traversal_mapping in maps[traversal]['mappings']:
        #             offset = 0
        #             if value_at_traversal >= traversal_mapping['sourceRangeStart'] and value_at_traversal <= traversal_mapping['sourceRangeStart'] + traversal_mapping['rangeLength'] - 1:
        #                 offset = value_at_traversal - traversal_mapping['sourceRangeStart']
        #                 seed[maps[traversal]['destination']] = traversal_mapping['destinationRangeStart'] + offset
        #         if not maps[traversal]['destination'] in seed:
        #             seed[maps[traversal]['destination']] = value_at_traversal


part2()