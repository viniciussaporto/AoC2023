import sys
import re

def main():
    filename = sys.argv[1]
    total_power = 0

    with open(filename, 'r') as file:
        for line in file:
            game_id, cube_sets = line.split(':')

            max_red = max_green = max_blue = 0
            for cube_set in cube_sets.split(';'):
                red = green = blue = 0
                for cube in cube_set.split(','):
                    count, color = re.findall(r'(\d+) (\w+)', cube)[0]
                    if color == 'red':
                        red = int(count)
                    elif color == 'green':
                        green = int(count)
                    elif color == 'blue':
                        blue = int(count)

                max_red = max(max_red, red)
                max_green = max(max_green, green)
                max_blue = max(max_blue, blue)

            total_power += max_red * max_green * max_blue

    print(total_power)

if __name__ == "__main__":
    main()