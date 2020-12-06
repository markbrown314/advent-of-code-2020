#!/usr/bin/python3
"""
🎅 Advent of Code 2020 Day #5 Binary Boarding Part 1 & 2
   by Mark F. Brown <mark.brown314@gmail.com>
"""
import sys

MAX_ROWS = 128
MAX_COLS = 8

# partition an array in half
def partition(a):
    return [list(filter(lambda x: x>(a[len(a)-1]+a[0])//2, a)), 
            list(filter(lambda x: x<=(a[len(a)-1]+a[0])//2, a))]

# given direction list find seat id
def find_seat_id(directions):
    rows = [*range(0, MAX_ROWS)]
    cols = [*range(0, MAX_COLS)]

    for direction in directions:
        if direction == 'F':
            rows = partition(rows)[1]
        elif direction == 'B':
            rows = partition(rows)[0]
        elif direction == 'L':
            cols = partition(cols)[1]
        elif direction == 'R':
            cols = partition(cols)[0]

    assert len(rows) == 1 and len(cols) == 1

    return (rows[0] * MAX_COLS) + cols[0]


def main():
    with open('puzzle_input_1.txt') as file_input:
        input_data = file_input.readlines()

    seat_ids = [find_seat_id(list(directions)) for directions in input_data]

    # return highest seat (part 1)
    print("highest seat id:", max(seat_ids))

    # find gap in seats to determine my seat (part 2)
    your_id = set(*[range(min(seat_ids), max(seat_ids) + 1)]) ^ set(seat_ids)        
    print("your id:", your_id)

if __name__ == "__main__":
    main()