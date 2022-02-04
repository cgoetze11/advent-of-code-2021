from collections import defaultdict


def calculate_position(input_file):
    with open(input_file, "rb") as input_file:
        content_list = input_file.readlines()

    distance = defaultdict(int)
    for val in content_list:
        direction, num = val.decode().strip().split(" ")
        distance[direction] += int(num)

    return (distance["down"] - distance["up"]) * distance["forward"]

print(calculate_position('day2/input.txt'))