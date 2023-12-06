from pathlib import Path
from re import compile, findall, finditer, search, split, sub, match
from json import dumps

exampledata = open(f"{Path(__file__).stem}exampleinput.txt", "r").readlines()
data = open(f"{Path(__file__).stem}input.txt", "r").readlines()

def parse(text):
    return [int(finditer(r"\d+", text).__next__()[0])] + [split(r" +", part) for part in
        split(r" +\| +", sub(r".*: +", "", text.strip()))
    ]

def calculate(input):
    [game, winners, mine] = parse(input)
    score = 0
    wins = 0
    for winner in winners:
        for number in mine:
            if winner == number:
                score = 1 if score == 0 else score * 2
                wins += 1
    return score, wins

print("ex", sum([calculate(game)[0] for game in exampledata]))
print("real", sum([calculate(game)[0] for game in data]))

def parse_strong(text):
    number = int(finditer(r"\d+", text).__next__()[0])
    winners, mine = [split(r" +", part) for part in
            split(r" +\| +", sub(r".*: +", "", text.strip()))
    ]
    entries = {}
    for scratch_number in mine:
        entries[scratch_number] = True
    return [number, winners, entries]

def new_rules(input):
    card_counts = {}
    score = 0
    for game, winners, mine in [parse_strong(text) for text in input]:
        wins = 0
        for winner in winners:
            if winner in mine:
                wins += 1
        copies_count = card_counts[game] + 1 if game in card_counts else 1
        score += copies_count
        for i in range(wins):
            card_counts[game + i + 1] = card_counts[game + i + 1] + copies_count \
                if (game + i + 1) in card_counts \
                else copies_count
    return score

print("ex", new_rules(exampledata))
print("real", new_rules(data)) # 558215720 is wrong

