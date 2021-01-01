data = open('passes.txt')
passwords = data.readlines()
# passwords = ['1-13 r: gqdrspndrpsrjfjx\n', '5-16 j: jjjjkjjzjjjjjfjzjjj\n']
letters = []
goodpass = []
for x in passwords:
    letters = []
    y = x.split(" ")
    positions = y[0].split("-")
    letter_pos1 = int(positions[0])-1
    letter_pos2 = int(positions[1])-1
    print(letter_pos1)
    print(letter_pos2)
    letter = y[1]
    letter = letter[0]  # There's gotta be a better way than this.
    password = y[2]
    password = password[:-1]  # Get rid of the "/n"
    print(letter)
    print(password)
    for x in password:
        letters.append(x)
    print(letters)
    try:
        if (letters[letter_pos1] == letter and letters[letter_pos2] == letter) or (letters[letter_pos1] != letter and letters[letter_pos2] != letter):
            print("not good")
        else:
            print("it's good")
            goodpass.append(password)
    except IndexError:
        print("nope!")
    print("goodpasses")
    print(goodpass)
    print("")
    print("")

passcount = len(goodpass)
print("The number of good passwords is: " + str(passcount))
