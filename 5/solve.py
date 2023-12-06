import sys

print("Hello, friend")
print("Advent of code 2023, day 5")
print("https://adventofcode.com/2023/day/5")
print("\n")

lines = []
seeds = []
# maps = {seed: [(x1, x2, diff), ], soil: [(x1, x2, diff)]}
maps = {}

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

def parse_seeds():
    global seeds
    global lines

    (junk, rest) = lines.pop(0).split(':')
    seeds = list(map(int, rest.split()))

def parse_map(name):
    global maps
    global lines
    
    #debug(["name", name])

    maps[name] = []

    while 1:
        l = lines.pop(0)
        if l.startswith(name):
            # read until blank line
            while 1:
                if len(lines) == 0:
                    return
                l2 = lines.pop(0)
                #debug(["l2: ", l2])
                if len(l2) < 2:
                    return
                (c1, c2, c3) = l2.split()
                maps[name].append((int(c2), int(c2)+int(c3)-1, int(c2)-int(c1)))

def get_map(n, v):
    for (x1, x2, diff) in maps[n]:
        if v >= x1 and v <= x2:
            return v - diff if diff >=0 else v + (-1*diff)

    return v

def calc():
    mv = 2**62
    for s in seeds:
        sv = get_map("seed", s)
        slv = get_map("soil", sv)
        fv = get_map("fertilizer", slv)
        wv = get_map("water", fv)
        lv = get_map("light", wv)
        tv = get_map("temperature", lv)
        locv = get_map("humidity", tv)
        if locv < mv:
            mv = locv
    return mv

if __name__ == '__main__':
    debug("start main")
    name = "input.txt"
    if len(sys.argv) > 2:
        name = sys.argv[2]

    with open(name) as f:
        lines = f.readlines()

    #print("lines", lines)

    parse_seeds()
    parse_map("seed")
    parse_map("soil")
    parse_map("fertilizer")
    parse_map("water")
    parse_map("light")
    parse_map("temperature")
    parse_map("humidity")
    
    print("maps", maps)

    print("lowest: %s", calc())

