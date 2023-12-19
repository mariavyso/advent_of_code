input_text = open("input.txt", "r").readlines()
calibration_values = 0

for line in input_text:
    proto_number = [x for x in line if x.isdecimal()]
    calibration_values += int(proto_number[0] + proto_number[-1])


print(calibration_values)
