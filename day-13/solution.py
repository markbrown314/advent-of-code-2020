#!/usr/bin/python3
"""
🎅 Advent of Code 2020 Day #13 Shuttle Search Part 1 & 2
   by Mark F. Brown <mark.brown314@gmail.com>
"""

import math
from crt import chinese_remainder

def main():
    """ solutions """
    timestamp = 1005162
    puzzle_input = "19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,"\
                   "17,x,x,x,x,x,x,x,x,x,x,x,29,x,443,x,x,x,x,x,37,x,x,x,x,x,x,13"
    # convert input to tuple list of positions in input and bus_ids
    bus_ids = [(x[0], int(x[1])) for x in enumerate(puzzle_input.replace('x', '1').split(','))]
    bus_ids = [* filter(lambda x: x[1] != 1, bus_ids)]
    # calculate departure time relative to timestamp
    times = [(x[0], (math.ceil(timestamp/x[1]) * x[1]) - timestamp) for x in bus_ids]

    # calculate the earliest departure time
    min_time = sorted(times, key = lambda x:x[1])[0]
    print("part 1:", min_time[1] * bus_ids[times.index(min_time)][1])

    # find the earliest timestamp such that the first bus ID departs at that time and each
    # subsequent listed bus ID departs at that subsequent minute.
    # this boils down to a chinese remainder theorem problem find the congruent modulo
    seq_n = [x[1] for x in bus_ids]
    coprime_a = [x[1] - x[0] for x in bus_ids]
    print("part 2:", chinese_remainder(seq_n, coprime_a))

if __name__ == "__main__":
    main()
