input_schematic = open("input.txt", "r").readlines()


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


def gear_from_result(result_list):
    result_list = list(filter(None, result_list))
    if len(result_list) == 2:
        return int(result_list[0]) * int(result_list[1])
    else:
        return 0


def iterate_by_row(input_schematic):
    final_result = 0
    for row in range(len(input_schematic)):
        for j in range(len(input_schematic[row])):
            result_list = []
            if input_schematic[row][j] == "*":
                result_list += search_number(input_schematic[row], j)
                if row - 1 >= 0:
                    result_list += search_number(input_schematic[row - 1], j)
                if row + 1 < len(input_schematic):
                    result_list += search_number(input_schematic[row + 1], j)
                final_result += gear_from_result(result_list)
    return final_result


print(iterate_by_row(input_schematic))
