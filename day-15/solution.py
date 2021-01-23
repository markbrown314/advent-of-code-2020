#!/usr/bin/python3
"""
🎅 Advent of Code 2020 Day #15  Rambunctious Recitation Part 1 & 2
   by Mark F. Brown <mark.brown314@gmail.com>
"""
import collections

puzzle_input = collections.OrderedDict({9:0, 3:0, 1:0, 0:0, 8:0, 4:0})

def main():
    """ solution """
    turn = 1
    spoken = 0

    for spoken in puzzle_input:
        puzzle_input[spoken] = turn
        turn += 1

    while True:
        if spoken in puzzle_input:
            diff = turn - 1 - puzzle_input[spoken]
            puzzle_input[spoken] = turn - 1
            spoken = diff
        else:
            puzzle_input[spoken] = turn - 1
            spoken = 0

        if turn == 2020:
            print("part 1:", spoken)

        if turn == 30000000:
            print("part 2:", spoken)
            break
        turn += 1

if __name__ == "__main__":
    main()
