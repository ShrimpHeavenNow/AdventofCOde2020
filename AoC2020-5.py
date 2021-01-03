import math

with open('seatcodes.txt') as f:
    seatcodes = [line.rstrip() for line in f]

seat_ids = []
for x in seatcodes:
    row = int(x[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(x[7:].replace("L", "0").replace("R", "1"), 2)
    # print(row)
    # print(col)
    seat_id = row * 8 + col
    # print(seat_id)
    seat_ids.append(seat_id)
    # print(seat_ids)


def high_seat(seat_ids):
    high_seat = 0
    for x in seat_ids:
        print(x)
        if x > high_seat:
            high_seat = x
        print(high_seat)
    print(high_seat)
    return high_seat

unseen = list(range(high_seat(seat_ids) + 1))

for x in seat_ids:
    if x in unseen:
        unseen.remove(x)
print(unseen)

# Clearly 607 is the right answer, but is there a way to figure this out without my brain?
# I guess not, as we don't know how many rows don't exist. Unless it's something like a huge leap in value like this.
# But then if your seat was 40, that wouldn't work, right? So maybe it needs human judgement?