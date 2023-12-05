import sys

print("Hello, friend")
print("Advent of code 2023, day 1")
print("https://adventofcode.com/2023/day/1")
print("\n")

cal_sum = 0

nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

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

def get_digit_int_value(b):
    #debug(["get_digit_int_value: ", b])
    if b >= 48 and b <= 57:
        #debug(["looks like a digit: ", b-48])
        return b - 48
    #debug("returning -1")
    return -1

def calibration_value(line):
    byte_array = bytes(line, "ascii")
    d1 = 0
    d2 = 0
    i = 0
    for b in byte_array:
        i += 1
        #debug(["byte", i])
        if d1 == 0:
            #debug("looking for d1")
            d = get_digit_int_value(b)
            if d >= 0:
                d1 = d
        else:
            #debug("looking for d2")
            d = get_digit_int_value(b)
            if d >= 0:
                d2 = d
    if d2 == 0:
        d2 = d1
    return (d1*10)+d2

if __name__ == '__main__':
    debug("start main")
    with open("input.txt") as f:
        counter = 0
        for line in f:
            counter += 1
            if debug_on == 1 and counter > 3:
                break
            c = calibration_value(line)
            debug([line, " ->", c])
            cal_sum += c
    print("calibration sum: ", cal_sum)

