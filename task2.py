import sys

arguments = sys.argv[1:]
words = arguments[0].split()
words = list(set(words))
words.sort()
for index, word in enumerate(words):
    print(word, end='')
    if index < len(words) - 1:
        print(' ', end='')
    else:
        print()