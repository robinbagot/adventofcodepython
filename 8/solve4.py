import sys
import math

print("Hello, friend")
print("Advent of code 2023, day 8")
print("https://adventofcode.com/2023/day/8")
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


def process_tuple(t, i):
    return t[i]


if __name__ == '__main__':
    debug("start main")
    name = "input.txt"
    if len(sys.argv) > 2:
        name = sys.argv[2]

    d = ""
    with open(name) as f:
        d = f.read()

    (d1, d2) = d.split("\n\n")

    indices = list(int(c.replace("L", "0").replace("R", "1")) for c in d1)

    dd = {}
    for n in d2.split("\n"):
        if n == "":
            break
        (s1, s2) = n.split(" = ")
        dd[s1] = s2
    for (dd1, dd2) in dd.items():
        (l, r) = dd2.split(", ")
        dd[dd1] = (l.strip("("), r.strip(")"))

    #print("dd: ", dd)
    

    ghosts = {}
    
    path_lengths = {}

    for (k,v) in dd.items():
        if k.endswith("A"):
            ghosts[k] = v
            path_lengths[k] = 0

    count = 0
    print("ghosts: ", ghosts)

    got_all_paths = 0

    while 1:
        for i in indices:

            nrs = {}
            for (k, g) in ghosts.items():
                nrs[k] = process_tuple(g, i)
            
            count += 1

            zs = 0
            ghosts = {}

            for (k, nr) in nrs.items():
                path_lengths[k] += 1
                if not nr.endswith("Z"):
                    ghosts[k] = dd[nr]
                
                if zs == len(nr):
                    print("steps: ", count)
                    exit(0)

            if len(ghosts) == 0:
                print("all ghost paths found")
                print("path_lengths: ", path_lengths)
                sss = 1
                for (k, p) in path_lengths.items():
                    sss *= p
                print("ans: ", math.lcm(*list(path_lengths.values())))
                exit(0)


