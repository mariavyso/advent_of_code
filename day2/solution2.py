input_game = open("input.txt","r").readlines()
sum_of_power = 0

for game in input_game:
    games_list = game.split(":")[1].replace(";",",").strip().split(",")
    set_of_cubes ={}
    for item in games_list:
        num, color = item.split()
        if color in set_of_cubes:
            set_of_cubes[color].append(int(num))
        else:
            set_of_cubes[color] = [int(num)]
    power_of_cubes = (max(set_of_cubes.get('red',1)))*(max(set_of_cubes.get('blue',1)))*(max(set_of_cubes.get('green',1)))
    sum_of_power += int(power_of_cubes)
print("Sum of the power of sets:", sum_of_power)
