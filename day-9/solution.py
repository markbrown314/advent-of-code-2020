#!/usr/bin/python3
"""
🎅 Advent of Code 2020 Day #9 Part 1 & 2
   by Mark F. Brown <mark.brown314@gmail.com>
"""
import itertools
import sys

def main():
    filename = "puzzle_input.txt" if len(sys.argv) < 2 else sys.argv[1]
    file_input = [int(num) for num in open(filename).read().splitlines()]

    i = 0
    n = 25
    remainder = [*reversed(file_input[n:])]

# find number that is not the sum of a pair in previous 25 numbers
    while remainder:       
        selection = file_input[i:n+i]
        pairs = [*itertools.combinations(selection, 2)]
        check = remainder.pop()

        additions = {a[0]+a[1]: (a[0], a[1]) for a in pairs}

        if check in additions:
            i += 1
            continue
        else:
            print("part 1:", check)
            break
# scan for contiguous range that adds up to number found in part 1
    mode = True
    i = 0
    n = 1
    acc = file_input[0]
    while i < n:
        if acc == check:
            print("part 2:", file_input[i]+file_input[n])
            break
        if mode:
            acc += file_input[n]
            if acc > check:
                mode = False
            n += 1
        else:
            acc -= file_input[i]
            if acc < check:
                mode = True
            i += 1

if __name__ == "__main__":
    main()