with open('customs.txt') as f:
    customs = [line.rstrip() for line in f]
answers = "abcdefghijklmnopqrstuvwxyz"
def shitty(fart):
    finished_entry = ""
    entries =[]
    for x in fart:
        #entry = []
        if x != "":  # Check if line is part of previous lines entry
            entry = x
            finished_entry = finished_entry + entry
        else:
            entries.append((finished_entry))
            finished_entry = ""
    entries.append((finished_entry))  # Adds lest entry into list.

    return entries

#customs = (shitty(customs))
#part_one(customs)

def part_one(customs):

    total_count = 0
    for x in customs:
        count = 0
        for y in answers:
            if y in x:
                count += 1
        total_count += count
    print(total_count)

def fart_attack(customs):
    entries = []
    finished_entry = []
    for x in customs:
        entry = []
        if x != "":  # Check if line is part of previous lines entry
            entry.append(x)
            entry = entry[0].split(" ")
            finished_entry = finished_entry + entry
        else:
            entries.append((finished_entry))
            finished_entry = []
    entries.append((finished_entry))  # Adds lest entry into list.

    return entries
group_answers = fart_attack(customs)

final_count = 0
for x in group_answers:
    for y in answers:
        count = 0
        for z in x:
            if y in z:  # Checks if letter is in answer
                count += 1
        if count == len(x):  # Checks if latter was in each answer.
            final_count += 1
print(final_count)  # I can't fucking believe that worked. First try, was unsure the whole time.