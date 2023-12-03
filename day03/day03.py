from collections import defaultdict
from itertools import takewhile

# Extract numbers with start position in string
def get_numbers(line):
    result = []
    i = 0
    while i < len(line):
        while i < len(line) and not line[i].isdigit():
            i += 1
        start = i
        num = ''.join(c for c in takewhile(str.isdigit, line[i:]))
        i += len(num)
        if num:
            result.append((start, num))
    return result

# Symbol is not digit and not '.'
def is_symbol(ch):
    return not (ch.isdigit() or ch == ".")

# At least one of the char in string is symbol
def is_any_symbol(s):
    for ch in s:
        if is_symbol(ch):
            return True
    return False

# At least one of the char in string is gear
def is_any_gear(s):
    i = 0
    for i in range(len(s)):
        if s[i] == '*':
            return i
    return -1

# Read lines from the file and add dots at the beginning and end
with open('input.txt', 'r') as file:
    lines = ['.' + line.strip() + '.' for line in file]

# Initialize input_lines with a single row of dots
input_lines = [['.' for _ in range(len(lines[0]))]]

# Add the lines with dots at the beginning and end
input_lines += lines

# Add the last row of dots
input_lines.append(['.' for _ in range(len(lines[0]))])

# Initialize a list to store numbers extracted from the input
result_numbers = []

# Iterate through rows in input_lines (excluding the first and last rows)
result_numbers.extend(
    int(number)
    for i in range(1, len(input_lines) - 1)
    for pos, number in get_numbers(input_lines[i])
    for j in [-1, 0, 1]
    if is_any_symbol(input_lines[i + j][pos - 1 : pos + len(number) + 1]))


print("Day 03 Part 1:", sum(result_numbers))

# Initialize a defaultdict to store gears at different positions
gears = defaultdict(list)

# Iterate through rows in input_lines (excluding the last row)
for i, line in enumerate(input_lines[:-1]):
    for pos, number in get_numbers(line):
        for j in [-1, 0, 1]:
            gear_pos = is_any_gear(input_lines[i + j][pos - 1: pos + len(number) + 1])
            if gear_pos != -1:
                gears[(i + j, gear_pos + pos)].append(int(number))

# Calculate the result by multiplying pairs of gears and summing the results
result = sum(v[0] * v[1] for k, v in gears.items() if len(v) == 2)

print("Day 03 Part 2:", result)
