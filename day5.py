from pathlib import Path
from re import compile, findall, finditer, search, split, sub, match
from json import dumps

exampledata = open(f"{Path(__file__).stem}exampleinput.txt", "r").readlines()
data = open(f"{Path(__file__).stem}input.txt", "r").readlines()

def parse(input):
    seeds = [int(seed[0]) for seed in finditer(r"\d+", input.pop(0))]
    input.pop(0)
    # destination, source, range
    source_map = {}
    destination_map = {}
    current_item = []
    for item in input:
        section = match(r"(.+)-to-(.+) map:", item)
        if section != None:
            current_section = section[1]
            current_item = []
            source_map[current_section] = current_item
            destination_map[current_section] = section[2]
        elif len(item) > 3:
            re_match = findall(r"\d+", item)
            section = [int(re_match[0]), int(re_match[1]), int(re_match[2])]
            current_item.append(section)
    return seeds, source_map, destination_map

def find_in_ranges(ranges, item):
    for destination, source, length in ranges:
        if item >= source and item <= (source + length):
            return destination + (item - source)
    return item

def solve(seeds, source_map, destination_map):
    lowest_loc = None
    for seed in seeds:
        segment = "seed"
        target = seed
        # target_before = seed
        while segment != "location":
            # target_before = target
            target = find_in_ranges(source_map[segment], target)
            # print(target_before, "->", target, ",", segment, "->", \
            #     destination_map[segment], source_map[segment])
            segment = destination_map[segment]
            # if segment != "location":
            #     target_before = target
        # print(target_before, "->", target, segment)
        # print()
        if (lowest_loc == None or target < lowest_loc):
            lowest_loc = target
    return lowest_loc

seeds, source_map, destination_map = parse(exampledata)
solution = solve(seeds, source_map, destination_map)
print(solution)
seeds, source_map, destination_map = parse(data)
solution = solve(seeds, source_map, destination_map)
print(solution)
