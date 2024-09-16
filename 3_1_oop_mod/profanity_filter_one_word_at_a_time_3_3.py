# Rude words detector, version 0.3
import string

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]


def check_line(line):
    rude_count = 0
    words = line.split(" ")
    for word in words:
        word = word.strip(string.punctuation) # Fixing the punctuation bug
        print("strip", word)
        word = word.lower() # Fixing the capitalization bug
        print("lower", word)
        print("\n")
        if word in rude_words:
            rude_count += 1
            print(f"found rude word: {word}")
    return rude_count


def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0
        for line in myfile:
            rude_count += check_line(line)

    if rude_count == 0:
        print("Congratulations, you have no rude words in your text file")
        print("At least, no rude words I know.")


if __name__ == '__main__':
    check_file("even.txt")
