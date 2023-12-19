import re

input_text = open("input.txt", "r").readlines()
calibration_values = 0
new_values_list = []
dict_letters = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
for line in input_text:
    n = 0
    text_to_num = ""
    while n < len(line):
        changed = False
        for k, v in dict_letters.items():
            if line[n : len(k) + n] == k:
                text_to_num += str(v)
                n += len(k) - 1
                changed = True
                break
        if not changed:
            text_to_num += line[n]
            n += 1
    new_values_list.append(text_to_num.strip())

for number in new_values_list:
    number = re.sub("[^0-9]", "", number)
    first_value = number[0]
    last_value = number[-1]
    calibration_values += int(first_value + last_value)
print(calibration_values)
