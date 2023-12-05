import sys

print("Hello, friend")
print("Advent of code 2023, day 1")
print("https://adventofcode.com/2023/day/1")
print("\n")

cal_sum = 0

nums = [("one", 3, 1), ("two", 3, 2), ("three", 5, 3), ("four", 4, 4), ("five", 4, 5), ("six", 3, 6), ("seven", 5, 7), ("eight", 5, 8), ("nine", 4, 9)]

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

def get_digit(b):
    debug(["get_digit: ", b])
    if b >= 48 and b <= 57:
        debug(["looks like a digit: ", b-48])
        return b - 48
    debug("returning -1")
    return -1

def get_word(s, direction):
    debug(["get_word: ", s, direction])
    for t in nums:
        (n, l, v) = t
        debug(["checking", n, l, v])
        if direction == 0:
            debug(["against", s[:l]])
            if s[:l] == n:
                return v
        else:
            debug(["against", s[len(s)-l:]])
            if s[len(s)-l:] == n:
                return v

    return -1

def calibration_value(line):
    #byte_array = bytes(line, "ascii")
    d1 = 0
    d2 = 0
    i = 0
    right = len(line)


    while 1:
        debug(["i is: ", i])
        i += 1
        if d1 == 0:
            c = line[0]
            debug("looking for d1")
            d = get_digit(bytes(c, "ascii")[0])
            if d >= 0:
                d1 = d
                debug(["got d1:", d1])
                continue
            else:
                d = get_word(line, 0)
                if d >= 0:
                    d1 = d
                    debug(["got d1:", d1])
                    continue
            line = line[1:]
        else:
            c = line[len(line)-1]
            debug("looking for d2")
            d = get_digit(bytes(c, "ascii")[0])
            if d >= 0:
                d2 = d
                debug(["got d2:", d2])
                break
            else:
                d = get_word(line, 1)
                if d >= 0:
                    d2 = d
                    debug(["got d2:", d2])
                    break
            line = line[:len(line)-1]
    print("d1:",d1,"d2:",d2)
    return (d1*10)+d2

if __name__ == '__main__':
    debug("start main")
    name = "input.txt"
    if len(sys.argv) > 2:
        name = sys.argv[2]
    with open(name) as f:
        counter = 0
        for line in f:
            counter += 1
            if debug_on == 1 and counter > 10:
                break
            c = calibration_value(line)
            print([line, " ->", c])
            cal_sum += c
        print("count:", counter)
    print("calibration sum: ", cal_sum)

