import sys

print("Hello, friend")
print("Advent of code 2023, day 4")
print("https://adventofcode.com/2023/day/4")
print("\n")

# cards = {r: count}
cards = {}
wins = {}

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

    global cards
    global wins
    
    (card, rest) = line.split(':')

    card_num = int(card[5:])

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
    
    wins[card_num] = count

    # itself
    if card_num in cards:
        cards[card_num] += 1
    else:
        cards[card_num] = 1

    # winner
    if count > 0:
        for r in range(card_num+1, card_num+count+1):
            if r in cards:
                cards[r] +=  cards[card_num]
            else:
                cards[r] = 1
    
    return cards[card_num]

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
    debug(["cards", cards])
    debug(["wins", wins])
    print(f"sum: {ssum}, count: {counter}")

    x = 0
    for (r, v) in cards.items():
        x += v

    print(f"x {x}")

