from pathlib import Path
from re import compile, findall, finditer, search, match
from json import dumps

exampledata = open(f"{Path(__file__).stem}exampleinput.txt", "r").readlines()
data = open(f"{Path(__file__).stem}input.txt", "r").readlines()

def calculate(input):
    h = len(input)
    w = len(input[0])
    pat_d = compile(r"\d+")
    pat_s = compile(r"[^.\d]")
    sum = 0
    for i, row in enumerate(input):
        for m in pat_d.finditer(row):
            start_x = max(m.start() - 1, 0)
            end_x = min(m.end() + 1, w-1)
            start_y = max(i - 1, 0) 
            end_y = min(i + 1, h - 1)
            prev = pat_s.search(input[start_y], start_x, end_x)
            cur = pat_s.search(input[i], start_x, end_x)
            next = pat_s.search(input[end_y], start_x, end_x)
            if prev != None or cur != None or next != None:
                sum += int(m[0])
    return sum

print("ex", calculate([game.strip() for game in exampledata]))
print("real", calculate([game.strip() for game in data]))

def try_upsert(match, gears, i, number_match):
    if match != None:
        n = int(number_match[0])
        key = f"{i} - {match.start()}-{match.end()}"
        if key in gears:
            gears[key].append(n)
        else:
            gears[key] = [n]
    return match != None

def pcalculate(input):
    h = len(input)
    w = len(input[0])
    pat_d = compile(r"\d+")
    pat_s = compile(r"\*")
    gears = {}
    for i, row in enumerate(input):
        for m in pat_d.finditer(row):
            start_x = max(m.start() - 1, 0)
            end_x = min(m.end() + 1, w-1)
            start_y = max(i - 1, 0) 
            end_y = min(i + 1, h - 1)
            prev = pat_s.search(input[start_y], start_x, end_x)
            cur = pat_s.search(input[i], start_x, end_x)
            next = pat_s.search(input[end_y], start_x, end_x)
            if prev != None or cur != None or next != None:
                _ = try_upsert(prev, gears, max(i - 1, 0), m) or \
                    try_upsert(cur, gears, i, m) or \
                    try_upsert(next, gears, min(i + 1, h - 1), m)
    return sum([g[0] * g[1] for g in [
        v for v in gears.values() if len(v) == 2
    ]])

print("ex", pcalculate([game.strip() for game in exampledata]))
print("real", pcalculate([game.strip() for game in data]))
