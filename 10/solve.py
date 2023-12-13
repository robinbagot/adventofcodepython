import sys
from collections import defaultdict

print("Hello, friend")
print("Advent of code 2023, day 10")
print("https://adventofcode.com/2023/day/10")
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

up = 1
down = 2
right = 4
left = 8
t_go = {'.':0,'|':3,'-':12,'L':5,'J':9,'F':6,'7':10,'S':15}
t_rec = {'.':0,'|':3,'-':12,'L':10,'J':6,'F':9,'7':5,'S':15}

# pos: row, col
def can_go(direc, frome, to, prev):
    if prev[0] == to[0] and prev[1] == to[1]:
        return False
    tt_current = m[frome[0]][frome[1]]
    tt_can = m[to[0]][to[1]]
    #(char, t_go, t_rec)
    possible = tt_current[1] & tt_can[2]
    if possible & direc == direc:
        return True
    return False

def can_go_left(pos, prev_pos):
    if pos[1] > 0:
        return can_go(left, pos, (pos[0], pos[1]-1), prev_pos)
    return False

def can_go_right(pos, pev):
    if pos[1] < len(m[0]) - 1:
        return can_go(right, pos, (pos[0], pos[1]+1), prev_pos)
    return False

def can_go_up(pos, prev):
    if pos[0] > 0:
        return can_go(up, pos, (pos[0]-1, pos[1]), prev_pos)
    return False

def can_go_down(pos, prev):
    if pos[0] < len(m) - 1:
        return can_go(down, pos, (pos[0]+1, pos[1]), prev_pos)
    return False

def move(direc, pos):
    if direc == down:
        return (pos[0]+1, pos[1])
    if direc == up:
        return (pos[0] - 1, pos[1])
    if direc == left:
        return (pos[0], pos[1]-1)
    if direc == right:
        return (pos[0], pos[1]+1)
    return pos

if __name__ == '__main__':
    debug("start main")
    name = "input.txt"
    if len(sys.argv) > 2:
        name = sys.argv[2]

    m = []
    row = 0
    s_pos = (0,0)
    with open(name) as f:
        while 1:
            d = f.readline()
            if d == "":
                break
            dd = []
            col = 0
            for c in d:
                if c =='\n':
                    break
                dd.append((c, t_go[c], t_rec[c]))
                if c == 'S':
                    s_pos = (row, col)
                col += 1
            m.append(dd)
            row += 1

    print("m: ", m)
    print("s: ", s_pos)

    current = s_pos
    prev_pos = s_pos
    s = True
    count = 0
    while 1:
        count += 1

        if can_go_down(current, prev_pos):
            print("down")
            prev_pos = current
            current = move(down, current)
        elif can_go_right(current, prev_pos):
            print("right")
            prev_pos = current
            current = move(right, current)
        elif can_go_up(current, prev_pos):
            print("up")
            prev_pos = current
            current = move(up, current)
        elif can_go_left(current, prev_pos):
            print("left")
            prev_pos = current
            current = move(left, current)
        if current[0] == s_pos[0] and current[1] == s_pos[1]:
            break

    print("count: ", count)
    print("max: ", int(count/2))
