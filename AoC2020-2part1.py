data = open('passes.txt')
passwords = data.readlines()
# passwords = ['1-13 r: gqdrspndrpsrjfjx\n', '5-16 j: jjjjkjjzjjjjjfjzjjj\n']
letters = []
goodpass = []
for x in passwords:
    letters = []
    y = x.split(" ")
    timesneeded = y[0].split("-")
    letter_min = int(timesneeded[0])
    letter_max = int(timesneeded[1])
    letter = y[1]
    letter = letter[0]  # There's gotta be a better way than this.
    password = y[2]
    password = password[:-1]  # Get rid of the "/n"
    print(letter_min)
    print(letter_max)
    print(letter)
    print(password)
    for x in password:
        letters.append(x)
    print(letters)
    letter_count = int(letters.count(letter))
    print(letter_count)
    if letter_min <= letter_count <= letter_max:
        print("it's good")
        goodpass.append(password)
    print("goodpasses")
    print(goodpass)

passcount = len(goodpass)
print("The number of good passwords is: " + str(passcount))
