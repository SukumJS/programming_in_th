def peter_pan(iter, line, word, last_line):
    edge = ["..#..", ".#.#.", "#.{}.#".format(word), ".#.#.", "..#.."]
    link = ["..#.", ".#.#", "#.{}.".format(word), ".#.#", "..#."]
    aster_link = [".{}.".format(word), ".{}.#".format(word)]
    if iter != 0 and iter % 3 == 0 and line == 2 and iter != last_line:
        return aster_link[0]
    elif iter != 0 and iter % 3 == 0 and line == 2 and iter == last_line:
        return aster_link[1]
    elif iter == last_line:
        return edge[line]
    else:
        return link[line]


def wendy(iter, line, word, last_line):
    edge = ["..*..", ".*.*.", "*.{}.*".format(word), ".*.*.", "..*.."]
    link = ["..*.", ".*.*", "*.{}.*".format(word), ".*.*", "..*."]
    if iter == last_line:
        return edge[line]
    else:
        return link[line]


decorate = input()

for j in range(1, 6):
    for i in range(1, len(decorate) + 1):
        if i % 3 == 0:
            print(
                wendy(i - 1, j - 1, decorate[i-1], len(decorate) - 1), end="")
        if i % 3 != 0:
            print(peter_pan(i - 1, j - 1,
                  decorate[i-1], len(decorate) - 1), end="")
    print("")
