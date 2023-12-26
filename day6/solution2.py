input_list = open("input.txt", "r").readlines()


def count_ways(possible_list, distance):
    ways = 0
    for i in possible_list:
        if i > distance:
            ways += 1
    return ways


def count_possible_distance(time):
    possible_list = [i * (time - i) for i in range(1, time)]
    return possible_list


def parse_input(input_list):
    time_line = input_list[0]
    distance_line = input_list[1]
    time_all = list(filter(None, time_line.split(":")[1].strip().split(" ")))
    time = [int("".join(time_all))]
    distance_all = list(filter(None, distance_line.split(":")[1].strip().split(" ")))
    distance = [int("".join(distance_all))]
    time_distance = zip(time, distance)
    return time_distance


def res(input_list):
    time_distance = parse_input(input_list)
    total_ways = 1
    for time, distance in time_distance:
        possible_list = count_possible_distance(time)
        ways = count_ways(possible_list, distance)
        total_ways *= ways
    print(total_ways)


res(input_list)
