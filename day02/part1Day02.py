import sys
import re

def main():
    filename = sys.argv[1]
    total = 0

    with open(filename, 'r') as file:
        for line in file:
            game_id, cube_sets = line.split(':')
            game_id = int(game_id.split()[1])

            possible = True
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

                if red > 12 or green > 13 or blue > 14:
                    possible = False
                    break

            if possible:
                total += game_id

    print(total)

if __name__ == "__main__":
    main()