import sys
from collections import defaultdict

print("Hello, friend")
print("Advent of code 2023, day 9")
print("https://adventofcode.com/2023/day/9")
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
        d = f.read()

    lines = d.split("\n")

    addsum = 0
    i = 0
    for line in lines:
        if line == "":
            continue
        print("line: ", line)
        addition = 0
        z = list(map(int, line.split()))
        j = 0
        diffs = []
        k = 0
        cmp_list = z
        while 1:
            diffs.append([])
            while j < len(cmp_list) - 1:
                diffs[k].append(cmp_list[1+j] - cmp_list[j])
                j += 1
            #print("diffs: ", diffs)
            if len(set(diffs[k])) <= 1:
                #print("addition: ", diffs[k][0])
                addition = diffs[k][0]
                break
            
            cmp_list = diffs[k]
            k += 1
            j = 0

        k = len(diffs) -2
        while k >= 0:
            j = len(diffs[k])
            diffs[k].append(diffs[k][j-1] + addition)
            addition = diffs[k][j-1] + addition
            k -= 1

        #print("diffs: ", diffs)

        print("add: ", diffs[0][len(diffs[0])-1])
        addsum += z[len(z)-1] + diffs[0][len(diffs[0])-1]

    print("addsum: ", addsum)
    
