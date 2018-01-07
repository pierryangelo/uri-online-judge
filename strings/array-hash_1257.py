"""
Name:          Array Hash
Category:      Strings
Number:        1257
Provided by:   TopCoder
Last modified: 01-07-18
"""

__author__ = 'Pierry A. Pereira <pierryangelo@gmail.com>'

tests = int(input())

while tests:
    test = int(input())
    hash = 0

    for i in range(test):
        line = input()
        for p, c in enumerate(line):
            hash += (ord(c) - 65) + i + p
        test -= 1

    print(str(hash))

    tests -= 1
