from collections import defaultdict

WIDTH = 140

# Extract numbers with start position in string
def get_numbers(line):
    result = []
    i = 0
    num = ""
    while i < len(line):
        while i < len(line) and not line[i].isdigit():
            i += 1
        start = i
        while i < len(line) and line[i].isdigit():
            num += line[i]
            i += 1
        if len(num) > 0:
            result.append((start, num))
            num = ""
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

# Initialize input_lines with a single row of dots
input_lines = [["." for i in range(WIDTH + 2)]]

# Read lines from the file and add dots at the beginning and end
with open('input.txt', 'r') as file:
    input_lines += ['.' + line.strip() + '.' for line in file]

# Add the last row of dots
input_lines.append(["." for i in range(WIDTH + 2)])

# Initialize a list to store numbers extracted from the input
result_numbers = []

# Iterate through rows in input_lines (excluding the first and last rows)
for i in range(1, len(input_lines) - 1):
    lst = get_numbers(input_lines[i])
    for pos, number in lst:
        for j in [-1, 0, 1]:
            if is_any_symbol(input_lines[i + j][pos - 1 : pos + len(number) + 1]):
                result_numbers.append(int(number))

print("day 3, part 1:", sum(result_numbers))

# Initialize a defaultdict to store gears at different positions
gears = defaultdict(list)

# Iterate through rows in input_lines (excluding the last row)
for i in range(len(input_lines) - 1):
    lst = get_numbers(input_lines[i])
    for pos, number in lst:
        for j in [-1, 0, 1]:
            gear_pos = is_any_gear(input_lines[i + j][pos - 1 : pos + len(number) + 1])
            if gear_pos != -1:
                gears[(i + j, gear_pos + pos)].append(int(number))

# Calculate the result by multiplying pairs of gears and summing the results
result = 0
for k, v in gears.items():
    if len(v) == 2:
        result += v[0] * v[1]

print("day 3, part 2:", result)
