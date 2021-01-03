with open('passports.txt') as f:
    passports = [line.rstrip() for line in f]
entry = []
entries = []
dicts = []
valid = []
valid_total = 0
entry_dict = {}

# Why is only some of these things functions? Why that's a damn good question.

def shitty():
    finished_entry = []
    for x in passports:
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


for x in shitty():  # Boy this is stupid. Just make this part of shitty() and retrun dicts.
    for y in x:
        to_dict = y.split(":")
        entry_dict[to_dict[0]] = to_dict[1]
    dicts.append(entry_dict)
    entry_dict = {}


def part_one(dicts):
    valid_total = 0
    dicts_valid = []
    for x in dicts:
        print(x)
        farts = x.keys()
        print(farts)
        if "byr" in farts and "iyr" in farts and "eyr" in farts and "hgt" in farts and "hcl" in farts and "ecl" in farts and "pid" in farts:
            valid_total += 1
            print("It's Valid")
            dicts_valid.append(x)
        fart_values = len(farts)
        print("Amount of keys: " + str(fart_values))
        print("Valid passports: " + str(valid_total))
    print(valid_total)
    return dicts_valid


valid_total = 0
hcl_values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
ecl_values = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
dict_valid2 = part_one(dicts)
for x in dict_valid2:  # There's gotta be a better way than this.
    print(x)
    good_hairs = 0
    if 1920 <= int(x["byr"]) <= 2002:
        print("goof byr: " + x["byr"])
        if 2010 <= int(x["iyr"]) <= 2020:
            print("good iry: " + x["iyr"])
            if 2020 <= int(x["eyr"]) <= 2030:
                print("good eyr: " + x["eyr"])
                if len(x["pid"]) == 9:
                    print("good pid: " + str(len(x["pid"])))
                    if (x["hgt"][-2:] == "cm" and 150 <= int(x["hgt"][:-2]) <= 193) or (
                            x["hgt"][-2:] == "in" and 59 <= int(x["hgt"][:-2]) <= 76):
                        print("good hgt: " + x["hgt"])
                        if x["hcl"][:1] == "#":
                            for y in x["hcl"][1:]:  # This suuuuuucks. Gotta be a better way.
                                if y in hcl_values:
                                    good_hairs += 1
                            if good_hairs == len(x["hcl"][1:]) and len(x["hcl"]) == 7:
                                print("good hairs: " + x["hcl"])
                                if x["ecl"] in ecl_values:
                                    print("good eyes:" + x["ecl"])
                                    print("fully Valid entry")
                                    valid_total += 1
print(valid_total)


def stolen_answer():
    with open('inputs.txt', "r") as infile:
        passports = infile.read().split('\n\n')
    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    count = 0
    for passport in passports:
        keys = set(map(lambda x: x.split(':')[0], passport.split()))
        if keys.issuperset(required):
            count += 1
    print(count)
