import sys
from collections import defaultdict
from functools import cmp_to_key 

print("Hello, friend")
print("Advent of code 2023, day 7")
print("https://adventofcode.com/2023/day/7")
print("\n")

cards = {"A":14, "K":13, "Q":12, "J":1, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2}
# hands = {string: ({"A": 0, "K": 1, "Q": 0, "J": 2, }, bid, type, score)}

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


def parse_line(l):
    h, s = l.split()
    hh = parse_hand(h)
    return (h, (hh, int(s), hand_type(hh), 0))


def hand_type(hh):

    hhl = list(hh.values())
    hhk = list(hh.keys())

    jokerth = 0
    if "J" in hh:
        jokerth = hh["J"]

    if jokerth == 4:
        return 7
    
    if jokerth == 3:
        if hhl[1] == 2:
            return 7
        return 6
    
    if jokerth == 2:
        if hhl[0] == 3:
            return 7
        if hhl[0] == 2 and hhk[0] != "J":
            return 6
        if hhl[1] == 2 and hhk[0] == "J":
            return 6
        return 4

    if hhl[0] == 5:
        return 7

    if hhl[0] == 4:
        if jokerth == 1:
            return 7
        return 6
    
    if hhl[0] == 3 and hhl[1] == 2:
        return 5

    if hhl[0] == 3:
        if jokerth == 1:
            return 6
        return 4

    if hhl[0] == 2 and hhl[1] == 2:
        if jokerth == 1:
            return 5
        return 3

    if hhl[0] == 2:
        if jokerth == 1:
            return 4
        return 2

    if jokerth == 1:
        return 2

    return 1


def parse_hand(h):
    hh = defaultdict(int)
    for i, char in enumerate(h):
        for card, v in cards.items():
            if card == char:
                hh[card] += 1
    return dict(sorted(hh.items(), key=lambda item: item[1], reverse=True))


def score_hands(hands):
    for h, (hh, b, t, s) in hands.items():
        ss = 0
        ss += t * 0x1000000
        i = 0x10000
        for c in h:
            v = cards[c]
            ss += v * i
            i /= 0x10
        hands[h] = (hh, b, t, ss)
    return dict(sorted(hands.items(), key = lambda item: item[1][3]))


if __name__ == '__main__':
    debug("start main")
    name = "input.txt"
    if len(sys.argv) > 2:
        name = sys.argv[2]

    with open(name) as f:
        lines = f.readlines()

    hands = score_hands(dict(parse_line(l) for l in lines))
    
    #print("hands ", hands)

    i = 1
    win = 0
    for h, (hh, b, t, s) in hands.items():
        win += i * b
        i += 1

    print("winnings: ", win)
    
