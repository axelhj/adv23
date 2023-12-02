from pathlib import Path
from re import match, search

exampledata = open(f"{Path(__file__).stem}exampleinput.txt", "r").readlines()
exampledata2 = open(f"{Path(__file__).stem}example2input.txt", "r").readlines()
data = open(f"{Path(__file__).stem}input.txt", "r").readlines()

def process(item):
    return int("".join([
        (match(r"\D*(\d)", item)[1]),
        (search(r"(\d)\D*$", item)[1])
    ]))

print("ex", sum([process(input) for input in exampledata]))
print("real", sum([process(input) for input in data]))

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def parse(w):
    if not w in numbers:
        return w
    return str(numbers.index(w) + 1)

separator = "|"
term = fr"{separator.join(numbers)}|\d"
neg_group = fr"(?!{term})"
def process2(item, i):
    first = search(fr"{neg_group}*({term})", item)[1]
    original_last = search(fr".*({term})", item)
    last = original_last[1] if original_last else first
    # print(f"{i}, {item.strip()}")
    # print(f"  {parse(first)} = parse({first}), {parse(last)} = parse({last})")
    return int("".join([parse(first), parse(last)]))

print("ex", sum([
    process2(input, i + 1) for i, input in enumerate(exampledata2)
]))
print("real", sum([
    process2(input, i + 1) for i, input in enumerate(data)
]))

