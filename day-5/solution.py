#!/usr/bin/python3
import sys

def main():
    filename = 'puzzle_test_1.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as file_input:
        for line in file_input:
            row_count = 128
            row_high = 127
            row_low = 0
            col_high = 7
            col_low = 0
            directions = list(line)
            for direction in directions:
                print("row high:", row_high,"row low:", row_low)
                row_count//=2
                if direction == 'F':
                    row_high = row_high - row_count
                if direction == 'B':
                    row_low = row_low + row_count
                if row_high == row_low:
                    print("found:", row_high)
                    break

if __name__ == "__main__":
    main()
