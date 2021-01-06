import collections
from typing import NamedTuple, Dict, List, Tuple
with open('rules.txt') as f:
    rules = [line.rstrip() for line in f]
"""
Ok, so:
Parse each line into lists seperated by "contain" and ","
things before contain are the name of the bag.
thing after contain the rules for that bag.
each bag has 2 descriptors.
Do we make each bag into a class?

we have to see which bags/ how many bags will wind up with a shiny gold bag inside.
So do we have each bag be a list of ALL the bags it contains and heck "shiny gold in"?

make each bag a variable containing a list of the bags inside, which are, themselves, varialbles of lists.

so "light red bags contain 1 bright white bag, 2 muted yellow bags." becomes:

light_red = [bright white, muted yellow, muted yellow]

and you do 

if shiny_gold in light_red: count += 1

yeah, i guess. Lets try it, sure.

shit, how do I have a variable declare its won name?
Ok, dynamic variables exist, but are weird. I don't think this will work as you'd be declaring the variables of its contents before they exist.

classes seems a better call.
but how do you declare the variable as a class? do I do a list of lists, with the name as one value and the dictionary as another?

Do I just do a dictionary of rules?
"""


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
    color = rule[0][:-5]
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
    return containers


bags = [parser(x) for x in rules]
bag_parents = parents(bags)
print(bag_parents)
count = 0
for x in bag_parents:
    print(x)








"""
Cool, you've parsed it out... now what?

so we need to make and check every bag as a tree to see if "shiny gold" is in the tree somewhere.
we could convert the contains dict into a list and easily make children that way. 
Right now the amount of bags doesn't matter, but I'm sure it will later...
"""
