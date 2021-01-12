with open('boot.txt') as f:
    boot = [line.rstrip() for line in f]


def parse(boot):
    boot_split = []
    position = 0
    for x in boot:
        boot_split.append(x.split(" "))
        boot_split[-1][1] = int(boot_split[-1][1])
        boot_split[-1].append(position)

        position += 1
    return boot_split


boot = parse(boot)


def part_one(boot):
    visited = set()  # set of list positions we've done.
    accumulator = 0
    position = 0
    steps = 0

    while position not in visited:
        steps += 1
        x = boot[position]
        visited.add(position)
        print(accumulator)
        print(x)
        if x[0] == "nop":
            position += 1
            print(position)
            continue
        elif x[0] == "acc":
            if x[1][0] == "+":
                accumulator += int(x[1][1:])
            else:
                accumulator -= int(x[1][1:])
            print(position)
            position += 1
        elif x[0] == "jmp":
            if x[1][0] == "+":
                position += int(x[1][1:])
            else:
                position -= int(x[1][1:])
            print(position)
            print("why haven't I jumped yet!?")
        print("NEXT!")
    print(accumulator)
    print(steps)


visited = set()
accumulator = 0
position = 0
steps = 0
target = len(boot)


def jump(position, x):
    position += x
    return position


visited = set()
switched = set()
accumulator = 0
position = 0
steps = 0
target = len(boot)
while position != target -1:
    visited = set()
    accumulator = 0
    position = 0
    switch = False
    while position not in visited:
        steps += 1
        x = boot[position]
        visited.add(position)
        print("value: " + str(accumulator))
        print(x)
        if position == target -1:
            print("final thing:")
            print(x)
            if x[0] =="acc":
                accumulator += x[1]

            break
        if x[0] == "nop":
            if x[2] not in switched and switch == False:
                visited.add(position)
                switch = True
                print("this is a jmp now")
                position = jump(position, x[1])
                switched.add(x[2])
                print("position: " + str(position))
            else:
                position += 1
                print("position: " + str(position))

        elif x[0] == "acc":
            accumulator += x[1]
            position += 1
            print("position: " + str(position))
        elif x[0] == "jmp":
            if x[2] not in switched and switch == False:
                visited.add(position)
                switch = True
                position += 1
                switched.add(x[2])
                print("this is a nop now")
                print("position: " + str(position))
            else:
                position = jump(position, x[1])
                print("position: " + str(position))
    print("again")
    print("")

print("Made it!")
print(accumulator)
