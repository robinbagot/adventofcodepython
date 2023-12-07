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

    #print("lines", lines)

    times = list(map(int, lines[0].split(':')[1].split()))
    distances = list(map(int, lines[1].split(':')[1].split()))
    print("times ", times)
    print("distances ", distances)

    r = []

    i = 0
    j = 1
    for t in times:
        r1 = []
        j = 0
        while j < t:
            f1 = j
            f2 = t - j
            f = f1 * f2
            if f > distances[i]:
                r1.append(f)
            j += 1
        print("r1: ", r1)
        r.append(len(r1))
        i += 1

    print("r: ", r)

    print("ans: ", reduce(lambda x, y: x*y, r))

