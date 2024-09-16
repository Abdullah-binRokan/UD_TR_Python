# Rude words detector, version 0.2

rude_words = ["crap", "darn", "heck", "jerk", "idiot", "butt", "devil"]


def rude_check(file):
    with open(file) as reader:
        contents = reader.read()
        words = contents.split(" ")
        rude_count = 0
        for word in words:
            if word.lower() in rude_words:
                if rude_count == 0:
                    print("You have a rude word!")
                print(f"rude word #{rude_count+1}: {word}")
                rude_count += 1
        if rude_count == 0:
            print("Congratulations, you have no rude words in your text file")
            print("At least, no rude words I know.")


rude_check("even.txt")
