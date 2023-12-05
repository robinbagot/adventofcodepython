import sys

print("Hello, friend")
print("Advent of code 2023, day 2")
print("https://adventofcode.com/2023/day/2")
print("\n")

game_id_sum = 0

balls = {"red": 12, "green": 13, "blue": 14}

# games = {1 -> ([{"red" -> 3, "green" -> 2}], valid)}
games = {}

colors = ["red", "green", "blue"]

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


def valid_game(line):
    g, rest = line.split(':', maxsplit=1)
    junk, game_id = g.split(' ', maxsplit=1)
    pulls = rest.split(';')
    #debug(["valid_game:", game_id, pulls])
    all_valid_pulls = 1
    game = []
    for pull in pulls:
        rgb = pull.split(',')
        play = {}
        for color in rgb:
            v1, n = color.strip().split(' ', maxsplit=1)
            v = int(v1)
            if v > balls[n]:
                all_valid_pulls = 0
            play[n] = v
        game.append(play)
    
    games[game_id] = (game, all_valid_pulls)

    debug(["games:", games])

    return int(game_id) if all_valid_pulls else 0 

if __name__ == '__main__':
    debug("start main")
    with open("input.txt") as f:
        counter = 0
        for line in f:
            counter += 1
            if debug_on == 1 and counter > 3:
                break
            v = valid_game(line)
            debug([line, " ->", v])
            game_id_sum += v
    print("game id sum: ", game_id_sum)


