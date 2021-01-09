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
    rule = rule.split("contain")
    color = rule[0][:-6]
    contents = rule[1].strip().split(",")
    for x in range(len(contents)):
        contents[x] = contents[x].strip()
        if contents[x] == "no other bags":
            contains = {}
            return bag(color, contains)
        count = int(contents[x][:1])
        name = contents[x][2:].strip("bag").strip("bags").strip()
        contains[name] = count
    return bag(color, contains)

def parents(bags):  # Could this be a function in the bag class?
    """Makes dictionary of bag color: bags it's inside"""
    containers = collections.defaultdict(list)
    for bag in bags:
        for x in bag.inside:
            containers[x].append(bag.name)

    print(containers)
    print(containers)
    return containers

def count_bags(bags, bag_name):
    parent_map = parents(bags)
    check_me = [bag_name]
    can_contain = set()
    print(parent_map)
    while check_me:
        child = check_me.pop()
        for x in parent_map:
            print([x])
            # fart = x.get(child, [])
            # if x not in can_contain:
            #     can_contain.add(fart[0])
            #     check_me.append(fart[1])
    return can_contain



bags = [parser(x) for x in rules]
print(len(count_bags(bags, "shiny gold")))

# count_bags(bags, "shiny gold  ")










"""
Cool, you've parsed it out... now what?

so we need to make and check every bag as a tree to see if "shiny gold" is in the tree somewhere.
we could convert the contains dict into a list and easily make children that way. 
Right now the amount of bags doesn't matter, but I'm sure it will later...
"""
