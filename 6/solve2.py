import sys
from functools import reduce

print("Hello, friend")
print("Advent of code 2023, day 6")
print("https://adventofcode.com/2023/day/6")
print("\n")


debug_on = 0
if len(sys.argv) > 1 and sys.argv[1] == "debug":
    debug_on = 1

def debug(o):
    if debug_on == 1:
        print("DEBUG: ", end='')
        if isinstance(o, list):
            for i in o:
                print(i, end='')
            print('\n', end='')
        else:
            print(o)



if __name__ == '__main__':
    debug("start main")
    name = "input.txt"
    if len(sys.argv) > 2:
        name = sys.argv[2]

    with open(name) as f:
        lines = f.readlines()

    time = int(lines[0].split(':')[1].replace(" ", ""))

    distance = int(lines[1].split(':')[1].replace(" ", ""))

    print("time ", time)
    print("distance ", distance)

    r = 0

    j = 1
    while j < time:
        f1 = j
        f2 = time - j
        f = f1 * f2
        if f > distance:
            r += 1
        j += 1
    
    print(j)

    print("ans: ", r)

