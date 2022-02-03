from day1.part1 import count_larger, get_input

def count_larger_by_three(input_list):
    sums = []
    for i in range(0, len(input_list) - 1, 4):
        indices = [i, i + 1, i + 2, i + 3]
        for index in indices:
            if index < len(input_list) - 2:
                sums.append(
                    input_list[index] + input_list[index + 1] + input_list[index + 2]
                )
    return count_larger(sums)


print(count_larger_by_three(get_input('day1/input.txt')))