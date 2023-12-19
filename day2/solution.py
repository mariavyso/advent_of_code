input_game = open("input.txt", "r").readlines()
sum_game_ids = 0
elf_cubes = {"red": 12, "green": 13, "blue": 14}

for game in input_game:
    game_id = game.split(":")[0].split(" ")[1]
    games_list = game.split(":")[1].split(";")
    possible_game = True
    for one_game in games_list:
        one_game = one_game.strip().split(",")
        for cube in one_game:
            number,color = cube.strip().split(" ")
            if color in elf_cubes and int(number) > elf_cubes[color]:
                possible_game = False
                break
    if possible_game:
        sum_game_ids += int(game_id)
print("Sum of the IDs of games:", sum_game_ids)
