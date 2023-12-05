import sys

print("Hello, friend")
print("Advent of code 2023, day 4")
print("https://adventofcode.com/2023/day/4")
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

def parse_row(line):
    
    (card, rest) = line.split(':')

    (w, h) = rest.split('|')

    w1 = w.strip().split(' ')
    wis = []
    for wn in w1:
        if not wn == '':
            wis.append(int(wn))

    h1 = h.strip().split(' ')

    count = 0
    for hn in h1:
        if not hn == '':
            hi = int(hn)
            if hi in wis:
                count += 1

    return 1 * pow(2, count-1) if count > 0 else 0

if __name__ == '__main__':
    debug("start main")
    name = "input.txt"
    if len(sys.argv) > 2:
        name = sys.argv[2]
    with open(name) as f:
        counter = 0
        ssum = 0
        for line in f:
            #if debug_on == 1 and counter > 3:
            #    break
            ssum += parse_row(line)
            counter += 1
            
    print(f"sum: {ssum}, count: {counter}")


