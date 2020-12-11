#!/usr/bin/python3
"""
🎅 Advent of Code 2020 Day #9
   by Mark F. Brown <mark.brown314@gmail.com>
"""
import itertools
import sys

def main():
    filename = "puzzle_test.txt" if len(sys.argv) < 2 else sys.argv[1]
    file_input = [int(num) for num in open(filename).read().splitlines()]
    print("file_input:", file_input)

    i = 0
    n = 5
    remainder = [*reversed(file_input[n:])]
    while remainder:
        
        selection = file_input[i:n+i]
        pairs = [*itertools.combinations(selection, 2)]
        print("selection:", selection)
        print("remainder:", remainder)
        check = remainder.pop()

        print("check:", check)
        print("pairs:", pairs)
        additions = {a[0]+a[1]: (a[0], a[1]) for a in pairs}
        print("additions:", additions)

        if check in additions:
            print("found", check)
            i += 1
            continue
        else:
            print("could not find", check)
            break
# scan


if __name__ == "__main__":
    main()