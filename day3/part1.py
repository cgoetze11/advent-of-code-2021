from collections import defaultdict

def binary_diagnostic(input_file):
    with open(input_file, "rb") as input_file:
        content_list = input_file.readlines()

    zeroes = defaultdict(int)
    ones = defaultdict(int)
    for val in content_list:
        num = str(val.strip())
        for i in range(len(num)):
            zeroes[i] += 1 if num[i] == '0' else 0
            ones[i] += 1 if num[i] == '1' else 0

    gamma = epsilon = ''
    for i in range(len(zeroes)):
        if zeroes[i] > ones[i]:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(epsilon, 2) * int(gamma, 2)

print(binary_diagnostic('day3/input.txt'))
