def calculate_position(input_file):
    with open(input_file, "rb") as input_file:
        content_list = input_file.readlines()

    horizantal, = aim = depth = 0
    for val in content_list:
        direction, num = val.decode().strip().split(" ")
        if direction == 'forward':
            horizantal += int(num)
            depth += aim * int(num)
        elif direction == 'down':
            aim += int(num)
        else:
            aim -= int(num)

    return (horizantal * depth)

print(calculate_position('day2/input.txt'))