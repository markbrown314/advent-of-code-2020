#!/usr/bin/python3
import sys

def main():
    filename = 'puzzle_input_1.txt'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    with open(filename) as file_input:
        ids = []
        for line in file_input:
            row_count = 128
            row_high = 127
            row = None
            row_low = 0
            col_high = 7
            col_low = 0
            col = None
            directions = list(line)
            for direction in directions:
                #print("row high:", row_high, "row low:", row_low)
                #print("col high:", col_high, "col low:", col_low)
                row_count//=2
                if direction == 'F':
                    row_high = row_high - row_count
                if direction == 'B':
                    row_low = row_low + row_count
                if row_high == row_low:
                    #print("row found:", row_high)
                    col = row_high
                    row = row_high
                    row_high = 127
                    row_count = 8
                    continue
                if direction == 'L':
                    col_high = col_high - row_count
                if direction == 'R':
                    col_low = col_low + row_count
                if col_high == col_low:
                    col = col_high
                    #print("col found:", col_high)
                    seat_id = (row * 8) + col
                    ids.append(seat_id)
                    print("seat ID:", seat_id)
                    break

        ids = sorted(ids)
        print("highest id:", ids[len(ids)-1])
        print(ids)
        for i in range(0, len(ids)-1):
            if ids[i]-ids[i+1] != -1:
                print("your id:", ids[i]+1)
if __name__ == "__main__":
    main()
