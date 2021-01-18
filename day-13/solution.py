#!/usr/bin/python3

import sys
import math
from crt import chinese_remainder

"""
🎅 Advent of Code 2020 Day #13 Shuttle Search Part 1 & 2
   by Mark F. Brown <mark.brown314@gmail.com>
"""

def main():
    timestamp = 1005162
    puzzle_input = "19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,443,x,x,x,x,x,37,x,x,x,x,x,x,13"
    bus_ids = [(x[0], int(x[1])) for x in enumerate(puzzle_input.replace('x', '1').split(','))]
    bus_ids = [*filter(lambda x: x[1] != 1, bus_ids)]
    times = [(x[0], (math.ceil(timestamp/x[1])*x[1])-timestamp) for x in bus_ids]
    sorted_times = sorted(times, key = lambda x:x[1])
    index = times.index(sorted_times[0])
    min_time_bus_id  = bus_ids[index]
    print("part 1:", sorted_times[0][1] * min_time_bus_id[1])

    n = [x[1] for x in bus_ids]
    a = [x[1] - x[0] for x in bus_ids]
    
    print("part 2:", chinese_remainder(n,a))

if __name__ == "__main__":
    main()
