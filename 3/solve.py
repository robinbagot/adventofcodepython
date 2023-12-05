import sys

print("Hello, friend")
print("Advent of code 2023, day 3")
print("https://adventofcode.com/2023/day/3")
print("\n")

part_num_sum = 0

#format::  
#  prev_line = [(char, colindex1), (char, colindex2), (char, colindex3), ]
#  part_nums = {row: [(num, i1, i2, is_part)]}

prev_line = []
part_nums = {}

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
    
    global prev_line
    global part_nums

    prev_char_is_symbol = 0
    next_char_is_symbol = 0
    in_number = 0
    number = ""
    new_prev_line = []
    set_part = 0
    i = 0

    part_nums[row_num] = []

    # build number list
    for c in line:
        # nothing
        if c == '.':
            if in_number == 0:
                prev_char_is_symbol = 0
            next_char_is_symbol = 0
        elif c.isdigit():
            number += c
            in_number = 1
            i += 1
            continue
        # nothing
        elif c == '\n':
            pass
        # should do check char in list etc here, but lazy
        else:
            # build up symbol/index list
            new_prev_line.append((c, i))

            # maybe the symbol is adjacent to number on previous row
            #debug(f"updating prev row with index {i}, row {row_num}")
            update_numbers_from_adjacent_symbol(row_num-1, i)

            # case symbol after number
            if in_number:
                next_char_is_symbol = 1
            
            prev_char_is_symbol = 1

        if in_number:
            if row_num == 84:
                debug(f"pushing number {number} i {i} row_num {row_num} prev_ {prev_char_is_symbol} next_ {next_char_is_symbol}")
            push_number(number, i, row_num, prev_char_is_symbol + next_char_is_symbol)
            number = ""
            in_number = 0

        i += 1

    #debug(["line:", line])

    # scan prev for updating part number
    if row_num > 0:
        #debug(f"going to handle prev_line, row_num: {row_num}")
        #debug(["prev_line", prev_line])
        for (c, i) in prev_line:
            update_numbers_from_adjacent_symbol(row_num, i)

    prev_line = new_prev_line

    return 0

def push_number(n, i, r, is_part):
    p = 0
    if is_part > 0:
        p = 1
    part_nums[r].append((int(n), i - len(n), i, p))

def update_numbers_from_adjacent_symbol(r, i):
    if r == 84:
        debug(["r:", r])
        debug(["i:", i])
        debug(["update_number, part_nums:", part_nums])
    c = 0
    for (n, i1, i2, p) in part_nums[r]:
        # index adjacent
        if i >= i1-1 and i <= i2:
            part_nums[r][c] = (n, i1, i2, 1)
            if r == 84:
                debug(f"updated, r: {r}, n: {n}")
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
    
    debug(["part_nums:", part_nums])

    part_sum = 0
    part_count = 0
    i = 0
    for (r, l) in part_nums.items():
        debug(f"row {i}, {l}")
        for (n, i1, i2, p) in l:
            if p:
                part_sum += n
                part_count += 1
        i += 1

    print(f"part number sum: {part_sum}, count: {part_count}")


