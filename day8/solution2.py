from math import gcd
from itertools import cycle
import re

input_lines = open("input.txt", "r").read()
direction_str, input_lines = input_lines.split("\n\n")
nodes = {}

for key, left, right in re.findall(r"(\w+) = \((\w+), (\w+)\)", input_lines):
    nodes[key] = [left, right]


def finding_steps(direction_str, nodes, k="AAA"):
    steps = 0
    for direction in cycle(direction_str):
        if direction == "L":
            k = nodes[k][0]
        else:
            k = nodes[k][1]
        steps += 1
        if k.endswith("Z"):
            return steps


def total_steps_count(nodes, direction_str):
    total_steps = []
    for k in nodes.keys():
        if k.endswith("A"):
            total_steps.append(finding_steps(direction_str, nodes, k))
    lcm = 1
    for step in total_steps:
        lcm = lcm * step // gcd(lcm, step)
    return lcm


print(total_steps_count(nodes, direction_str))

