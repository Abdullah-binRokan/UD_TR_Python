count = 0
your_word = input("Enter you word:")
letter = input("Enter a letter to count it:")

for ch in your_word:
    if ch == letter:
        count = count + 1

print(count)
