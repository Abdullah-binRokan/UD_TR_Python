# Rude words detector, version 0.1

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]


def rude_check(file):
    with open(file) as reader:
        contents = reader.read()
        rude_count = 0
        for rude in rude_words:
            if rude in contents.lower():
                if rude_count == 0:
                    print("You have a rude word!")
                print(f"rude word #{rude_count+1}: {rude}")
                rude_count += 1
        if rude_count == 0:
            print("Congratulations, you have no rude words in your text file")
            print("At least, no rude words I know.")


rude_check("even.txt")
