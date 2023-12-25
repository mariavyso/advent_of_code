input_card = open("input.txt", "r").readlines()
sum_of_points = 0


def total_points_counter(win_points):
    total_points = 0
    card_points = []
    for point in range(len(win_points)):
        card_points.append(2**point)
    if len(card_points) > 0:
        total_points += int(card_points[-1])
    else:
        total_points += 0
    return total_points


def parse_card_info(card):
    win_points = []
    win_numbers = card.split(":")[1].split("|")[0].strip().split(" ")
    win_numbers = list(filter(None, win_numbers))
    elf_numbers = card.split(":")[1].split("|")[1].strip().split(" ")
    elf_numbers = list(filter(None, elf_numbers))
    for i in win_numbers:
        if i in elf_numbers:
            win_points.append(1)
    return total_points_counter(win_points)


for card in input_card:
    sum_of_points += parse_card_info(card)

print("Result", sum_of_points)
