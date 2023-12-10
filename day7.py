from pathlib import Path
from re import compile, findall, finditer, search, split, sub, match
from json import dumps

exampledata = open(f"{Path(__file__).stem}exampleinput.txt", "r").readlines()
data = open(f"{Path(__file__).stem}input.txt", "r").readlines()

print("ex", exampledata)
print("re", exampledata)
