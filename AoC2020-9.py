with open('xmas.txt') as f:
    xmas = [int(line.rstrip()) for line in f]


def make_values(fart):
    possible_values = []
    for x in fart:
        for y in fart:
            if x != y:
                possible_values.append(x + y)
    return possible_values


def part_one(xmas):
    offset = 0
    the25 = xmas[0:25]
    possible = make_values(the25)

    while True:
        next_value = 25 + offset
        if xmas[next_value] in possible:
            the25.append(xmas[next_value])
            del the25[0]
            offset += 1
            possible = make_values(the25)
        else:
            break
    return xmas[next_value]


invalid = part_one(xmas)
offset = 0
the25 = xmas[0:25]
next_value = 25 + offset
solved = False

while True:
    run = []
    next_value = 25 + offset
    step = 0
    print("")
    print("next")
    print("")
    for x in the25:  # Adds x and subsequent numbers
        run = []
        run.append(x)
        tally = x
        print(str(the25) + " " + str(len(the25)))
        print("new x: " + str(x))
        for y in the25[step:]:  # Only adds numbers after x
            if x != y:
                tally = tally + y
                print(tally)
                run.append(y)
                print(run)
            if tally == invalid:  # Ends loop if the series of numbers adds to part ones answer.
                print("solved!")
                solved = True
                print(tally)
                run.sort()  # MOTHER FUCKER! This is what I kept missing. Helps to read the damn prompt.
                print(run)
                answer = run[0] + run[-1]
                fart = 0
                for x in run:
                    fart += x
                print(fart)
                print(invalid)
                print(answer)
                input()
        step += 1  # To make sure it's only subsequent numbers adding to x

    the25.append(xmas[next_value])  # Adds next number in xmas, removes first number.
    del the25[0]
    offset += 1

#  85848519 invalid

# 10514990 low SHIT! THis was my first answer and probably correct if I sorted the damn thing.
# I bet I didn't even have to the "make sure it's only subsequent numbers" thing. UGH.
# 138598244 high

# 9401414 wrong
# 9162974 Wrong
# 11550490 Wrong
# 226195028 Wrong
