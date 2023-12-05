import sys

print("Hello, friend")
print("Advent of code 2023, day 3")
print("https://adventofcode.com/2023/day/3")
print("\n")

part_num_sum = 0

#format::  
#  nums = {row: [(num, i1, i2)]}
#  gears = {row: [(i, [(connection-r, connection-i1, connection-i2, value), ], connection-count)]}

nums = {}
gears = {}

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

def parse_row(line, row_num):
    
    global nums
    global gears

    prev_was_digit = 0
    prev_was_gear = 0
    in_number = 0
    number = ""
    new_prev_line = []
    set_part = 0
    i = 0

    gears[row_num] = []
    nums[row_num] = []

    # build number list
    for c in line:
        
        if c.isdigit():
            number += c
            in_number = 1
            i += 1
            continue
        elif c == '*':
            # build up gear list
            # include number if this gear follows a number
            push_gear(i, row_num, number if in_number else "0")

            if in_number:
                push_number(number, i, row_num)
                number = ""
                in_number = 0

            prev_was_gear = 1
        # . or other symbol or \n
        else:
            if in_number:
                push_number(number, i, row_num)
                if prev_was_gear:
                    update_gear(row_num, i, number)
                prev_was_gear = 0
                number = ""
                in_number = 0

        i += 1

    return 0

def push_gear(i, r, number):

    global nums
    global gears

    n = int(number)
    pos = []
    c = 0

    # a number was passed
    if n > 0:
        pos.append((r, i - len(number), i, n))
        c += 1

    # have to check previous line for nums adjacent to gear
    if r > 0:
        for (n2, i1, i2) in nums[r-1]:
            if i >= i1-1 and i <= i2:
                pos.append((r-1, i1, i2, n2))
                c += 1
        
    gears[r].append((i, pos, c))

def push_number(n, i, r):

    global nums
    nums[r].append((int(n), i - len(n), i))

    if r > 0:
        update_gear(r-1, i, n)

def update_gear(r, ni, n):

    global gears
    c = 0
    i1 = ni - len(n)
    i2 = ni
    for (gi, list2, cc) in gears[r]:
        # index adjacent
        if gi >= i1-1 and gi <= i2:
            list2.append((r, i1, i2, int(n)))
            gears[r][c] = (gi, list2, cc+1)
        c += 1

if __name__ == '__main__':
    debug("start main")
    name = "input.txt"
    if len(sys.argv) > 2:
        name = sys.argv[2]
    with open(name) as f:
        counter = 0
        for line in f:
            #if debug_on == 1 and counter > 3:
            #    break
            parse_row(line, counter)
            counter += 1
    
    debug(["gears:", gears])

    gear_sum = 0
    gear_count = 0

    for (r, l) in gears.items():

        for (i, list2, cc) in l:
            if cc > 1:
                if cc > 2:
                    print("not good")
                vs = 1
                for (r, i1, i2, v) in list2:
                    vs *= v
                gear_sum += vs
                gear_count += 1

    print(f"gear sum: {gear_sum}, count: {gear_count}")


