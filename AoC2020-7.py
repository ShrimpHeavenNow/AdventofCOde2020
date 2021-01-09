import collections
from typing import NamedTuple, Dict, List, Tuple
with open('rules.txt') as f:
    rules = [line.rstrip() for line in f]

class bag:
    def __init__(self, name, inside):
        self.name = name
        self.inside = inside  # CHILDREEEEEN
        self.parent = None  # Do I need this?


def parser(x):
    """Returns bag object with it's name and bags it has inside."""
    contains = {}
    rule = x[:-1]  # Get rid of the period at the end.
    rule = rule.split(" bags contain ")
    color = rule[0]
    contents = rule[1].strip().split(",")
    for x in range(len(contents)):
        contents[x] = contents[x].strip()
        if contents[x] == "no other bags":
            contains = {}
            return bag(color, contains)
        count = int(contents[x][:1])
        name = contents[x][1:].strip("bag").strip("bags").strip()
        contains[name] = count
    return bag(color, contains)

def parents(bags):  # Could this be a function in the bag class?
    """Makes dictionary of bag color: bags it's inside"""
    containers = collections.defaultdict(list)
    for bag in bags:
        for x in bag.inside:
            containers[x].append(bag.name)
    return containers

def count_bags(bags, bag_name):
    parent_map = parents(bags)
    check_me = [bag_name]
    can_contain = set()
    while check_me:
        child = check_me.pop()
        for x in parent_map.get(child, []):
            if x not in can_contain:
                can_contain.add(x)
                check_me.append(x)
    return can_contain

def bag_amount (bags, bag_name, count):
    for x in bags:
        if x.name == bag_name:
            print(x.name)
            print(x.inside)
            for y in list(x.inside.values()):
                count += y
            print(count)
            for y in list(x.inside.keys()):  #Ah, also I need to do it for the amount of instances.
                print(y)
                for z in range(0,x.inside.get(y)):
                    count = bag_amount(bags, y, count)

    return count



bags = [parser(x) for x in rules]
# print(len(count_bags(bags, "shiny gold")))

print(bag_amount(bags, "shiny gold", 0))



