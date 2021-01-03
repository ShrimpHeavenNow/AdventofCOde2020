with open('trees.txt') as f:
    map = [line.rstrip() for line in f]
location = [0, 0]
map_width = len(map[0])
x_move = 3
y_move = 1
tree_hits = 0
finish = len(map)-1
print(finish)

tree_line = map[0]  # Find starting location
x_position = 0
for x in tree_line:
    if x == ".":
        break
    x_position += 1
location[0] = x_position

def shitty():
    while location[1] < finish:  # Moves if we're not on the bottom line.
        if location[0] + x_move > map_width :
            print("time to scroll")
            location[0] = location[0] % map_width
        location[0] = int(location[0]) + x_move
        location[1] = int(location[1]) + y_move
        tree_line = map[location[1]]
        print(tree_line)
        print(location[0])
        x_position = location[0]
        print(len(tree_line))
        terrain = tree_line[x_position]
        print(terrain)
        if terrain == "#":
            tree_hits += 1
        print(location[1])
        print(tree_hits)
def less_shitty(table, dx, dy):
    width = len(table[0])
    height = len(table)
    x = 0
    y = 0
    trees = 0
    while y < height:
        print(str(y) + " " + str(x) + " " + str(width) + " " + str(x % width))
        if table[y][x%width] == "#":
            trees += 1
        x += dx
        y += dy
    return trees

print(less_shitty(map, 1, 1) * less_shitty(map, 3, 1) * less_shitty(map, 5, 1) * less_shitty(map, 7, 1) * less_shitty(map, 1, 2) )


