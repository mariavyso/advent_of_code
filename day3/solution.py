input_schematic = open("input.txt", "r").read().splitlines()
numbers_and_dot = "0123456789."


def check_the_number(line, j, direction):
    number = ""
    k = j + direction
    while k >= 0 and k < len(line) and line[k].isdigit():
        number += line[k]
        k += direction
    return number


def search_number(line, j):
    if j < 0:
        return 0
    right = check_the_number(line, j, +1)
    left = check_the_number(line, j, -1)[::-1]
    center = line[j]
    if not center.isdigit():
        number_list = list(filter(None, ([left, right])))
        numb = [int(n) for n in number_list]
    else:
        number_list = list(filter(str.isdigit, [left, center, right]))
        number = "".join(n for n in number_list)
        numb = [int(number)]
    return numb


def iterate_by_row(schematic):
    result_list = []
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j] in numbers_and_dot:
                continue
            result_list += search_number(schematic[i], j)
            if i - 1 >= 0:
                result_list += search_number(schematic[i - 1], j)
            if i + 1 < len(schematic):
                result_list += search_number(schematic[i + 1], j)
    return sum(result_list)


print(iterate_by_row(input_schematic))
