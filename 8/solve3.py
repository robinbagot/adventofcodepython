import sys
from collections import defaultdict
import array

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

    print("dd: ", dd)
    
    # create key/index map
    dd_map = {}
    for i, k in enumerate(dd.keys()):
        dd_map[k] = i

    # creat new node Vec instead of Dict with index pointers plus numeric node type
    ddd = []
    for i, (k, v) in enumerate(dd.items()):
        nt = 0
        if k.endswith("A"):
            nt = 1
        if k.endswith("Z"):
            nt = -1
        ddd.append((dd_map[v[0]], dd_map[v[1]], nt))

    print("ddd: ", ddd)
    nodes = []

    # scan for ones ending in A
    for v in ddd:
        if v[2] > 0:
            nodes.append(v)

    count = 0

    #print("nodes: ", nodes)

    while 1:
        for i in indices:

            nr = []
            for node in nodes:
                #print("node: ", node)
                nr.append(process_tuple(node, i))
            
            count += 1

            #print("nodes: ", nodes)
            #print("sum(nodes): ", sum([n[2] for n in nodes]))
            #print("len(nodes): ", len(nodes))

            if -1 * sum([n[2] for n in nodes]) == len(nodes):
                print("steps: ", count)
                exit(0)

            nodes =[]
            for nrn in nr:
                nodes.append(ddd[nrn])


