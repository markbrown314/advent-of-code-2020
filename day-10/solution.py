#!/usr/bin/python3
"""
🎅 Advent of Code 2020 Day #10 Adapter Array Part 1 & 2
   by Mark F. Brown <mark.brown314@gmail.com>
"""
import sys

def main():
    """ solution for Day 10 """
    filename = "puzzle_input.txt" if len(sys.argv) < 2 else sys.argv[1]
    file_input = [int(num) for num in open(filename).read().splitlines()]
    # find distribution of joltage differences 3's and 1's
    jolts = sorted(file_input)
    # add first and last item
    last_item = jolts[-1]
    jolts.insert(0, 0)
    jolts.append(last_item + 3)

    dist = []
    for i in range(0, len(jolts)-1):
        dist.append(jolts[i+1]-jolts[i])

    threes = len([*filter(lambda a: a == 3, dist)])
    ones = len([*filter(lambda b: b == 1, dist)])

    print("part 1: ones:", ones, "threes:", threes, "answer:", ones * threes)

    # model connections as a tree (count leaves inorder to determine total paths)
    jolts = sorted(file_input, reverse = True)
    # add first and last item
    first_item = jolts[0]
    jolts.insert(0, first_item + 3)
    jolts.append(0)

    # use a dictionary to count leaves of tree
    path_dict = {path:0 for path in jolts}
    path_dict[jolts[0]] = 1

    # use memoization technique to cache paths already counted
    for i in jolts:
        total = path_dict[i]
        if i+1 in path_dict:
            total += path_dict[i+1]
        if i+2 in path_dict:
            total += path_dict[i+2]
        if i+3 in path_dict:
            total += path_dict[i+3]
        path_dict[i] = total

    print("part 2: distinct arrangements:", path_dict[0])

if __name__ == "__main__":
    main()
