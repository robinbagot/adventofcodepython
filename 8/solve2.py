import sys
from collections import defaultdict

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
    

    nodes = []

    for (k,v) in dd.items():
        if k.endswith("A"):
            nodes.append(v)

    count = 0
    print("nodes: ", nodes)
    while 1:
        for i in indices:

            nr = []
            for node in nodes:
                nr.append(process_tuple(node, i))
            
            count += 1

            zs = 0
            nodes = []

            for nrn in nr:
                if nrn.endswith("Z"):
                    zs += 1
                if zs == len(nr):
                    print("steps: ", count)
                    exit(0)
                nodes.append(dd[nrn])


