from pathlib import Path
from re import match, search

exampledata = open(f"{Path(__file__).stem}exampleinput.txt", "r").readlines()
data = open(f"{Path(__file__).stem}input.txt", "r").readlines()
print(match(r"\D*(\d)", exampledata[0])[1])
print(search(r"(\d)\D*$", exampledata[0])[0])

def process(item):
    num = int("".join([
        (match(r"\D*(\d)", item)[1]),
        (search(r"(\d)\D*$", item)[1])
    ]))
    return num if num > 9 else int(str(num) * 2)
print("ex", sum([process(input) for input in exampledata]))
print("real", sum([process(input) for input in data]))
