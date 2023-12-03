from pathlib import Path
from re import findall, finditer, search
from json import dumps

exampledata = open(f"{Path(__file__).stem}exampleinput.txt", "r").readlines()
data = open(f"{Path(__file__).stem}input.txt", "r").readlines()

def parse(input):
    # re.search returns None and so cannot be used
    # without extra check, use finditer instead
    id = finditer(r"\d+", input).__next__()[0]
    return [{
        "count": int(r[0]),
        "color": r[1],
        "id": int(id),
        "turn": "end" if r[2] == ";" or r[2] == "" else None
    } for r in findall(
        r"(\d+) (red|green|blue)(?:(;|,) )?",
        input
    )]

budget = { "red": 12, "green": 13, "blue": 14 }

def tally_ok(tally):
    return tally["red"] <= budget["red"] and \
        tally["green"] <= budget["green"] and\
        tally["blue"] <= budget["blue"]

def get_tally():
    return {
        "red": 0,
        "green": 0,
        "blue": 0
    }

def process(game):
    tally = get_tally()
    for move in game:
        tally[move["color"]] += move["count"]
        if move["turn"] == "end":
            if not tally_ok(tally):
                return 0
            tally = get_tally()
    return game[0]["id"]

# print (dumps(examplegames[0], indent=2))
print("ex", sum([process(game) for game in parse(exampledata)]))
print("real", sum([process(input) for input in parse(data)]))
