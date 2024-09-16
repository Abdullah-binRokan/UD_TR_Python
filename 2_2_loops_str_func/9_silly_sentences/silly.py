import random
import words


def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)

    # We'll append strings into this list for output.
    output = []

    # Keep track of where in the template string we are.
    index = 0

    # Add a while loop here.

    # After the loop has finished, join the output and return it.


if __name__ == '__main__':
    print(silly_string(words.nouns, words.verbs,
        words.templates))
        
