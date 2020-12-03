#!/usr/bin/python3
"""
🎅 Advent of Code 2020 Day #1 report repair part 1 & 2
   by Mark F. Brown <mark.brown314@gmail.com>
"""

import itertools

with open('puzzle_input_1.txt') as input_data:
    entries = sorted([int(a) for a in input_data])

print("find the sum that equals 2020")

indexes = list(range(0, len(entries)))

# find the two entries that sum to 2020 and then multiply those two numbers together

selections = itertools.combinations(indexes, 2)

for select in selections:
    if entries[select[0]] + entries[select[1]] == 2020:
        print("sum of 2:", entries[select[0]], entries[select[1]])
        print("product:", entries[select[0]] * entries[select[1]])
        break

# what is the product of the three entries that sum to 2020?
selections = itertools.combinations(indexes, 3)

for select in selections:
    if entries[select[0]] + entries[select[1]] + entries[select[2]] == 2020:
        print("sum of 3:", entries[select[0]], entries[select[1]], entries[select[2]])
        print("product:", entries[select[0]] * entries[select[1]] * entries[select[2]])
