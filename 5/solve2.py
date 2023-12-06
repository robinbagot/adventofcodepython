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

def get_mapr(n, v, v2):
    for (x1, x2, diff) in maps[n]:
        if x1 <= v <= x2:
            remainder = 0 if v2 <= x2 else v2 - x2
            return (diff, remainder, x2+1)

    return (0,0,0)

def calc_seeds():
    global seeds

    seeds_out = []

    while 1:
        if len(seeds) == 0:
            break

        x = seeds.pop(0)
        c = seeds.pop(0)

        (diff, remainder, offset) = get_mapr("seed", x, x + c)

        svx = x - diff
        svy = x + c - remainder - diff

        seeds_out.append((svx, svy))

        if remainder > 0:
            seeds.append(offset)
            seeds.append(remainder)

    return seeds_out


def calc_2(n, ain):
    aout = []

    while 1:
        if len(ain) == 0:
            break

        (x, y) = ain.pop(0)

        (diff, remainder, offset) = get_mapr(n, x, y)

        x1 = x - diff
        y1 = y - remainder - diff

        aout.append((x1, y1))

        if remainder > 0:
            ain.append((offset, offset+remainder))

    return aout


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

    wtfout = calc_seeds()

    print("seeds: ", wtfout)

    wtfout = calc_2("soil", wtfout)
    wtfout = calc_2("fertilizer", wtfout)
    wtfout = calc_2("water", wtfout)
    wtfout = calc_2("light", wtfout)
    wtfout = calc_2("temperature", wtfout)
    wtfout = calc_2("humidity", wtfout)

    print("lowest: ", sorted(wtfout, key=lambda x: x[0]))

