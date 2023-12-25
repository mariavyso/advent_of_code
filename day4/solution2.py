import re

input_txt = open("input.txt", "r").read().splitlines()
card_dict = {line: 1 for line in range(1, len(input_txt) + 1)}


def match_to_card_copy(number_of_matches, card_number):
    copy_list = []
    for j in range(1, number_of_matches + 1):
        copy_number = card_number + j
        copy_list.append(copy_number)
    for i in copy_list:
        card_dict[i] += 1 * card_dict[card_number]
    return card_dict


def find_match(one_card):
    win_numbers = one_card.split(":")[1].split("|")[0].strip().split(" ")
    win_numbers = filter(None, win_numbers)
    elf_numbers = one_card.split(":")[1].split("|")[1].strip().split(" ")
    elf_numbers = filter(None, elf_numbers)
    return len(set(win_numbers) & set(elf_numbers))


def analyse_one_card(one_card):
    card_number = int(re.findall(r"\d+", one_card)[0])
    number_of_matches = find_match(one_card)
    return match_to_card_copy(number_of_matches, card_number)


for one_card in input_txt:
    card_dict = analyse_one_card(one_card)

print("Result", sum(card_dict.values()))
