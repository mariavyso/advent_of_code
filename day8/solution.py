from itertools import cycle
import re

input_lines = open("input.txt", "r").read()
direction_str, input_lines = input_lines.split("\n\n")
nodes = {}

for key, left, right in re.findall(r"(\w+) = \((\w+), (\w+)\)", input_lines):
    nodes[key] = [left, right]


def finding_steps(direction_str, nodes):
    k = "AAA"
    steps = 0
    for direction in cycle(direction_str):
        if direction == "L":
            k = nodes[k][0]
        else:
            k = nodes[k][1]
        steps += 1
        if k == "ZZZ":
            return steps


print(finding_steps(direction_str, nodes))

