def get_input(filepath):
    with open(filepath, 'rb') as input_file:
        content_list = input_file.readlines()

    input_list = []
    for val in content_list:
        input_list.append(int(val.strip()))

    return input_list


def count_larger(input_list):
    num_larger = 0
    for i in range(len(input_list) - 1):
        if input_list[i] < input_list[i + 1]:
            num_larger += 1
    return num_larger


print(count_larger(get_input('day1/input.txt')))