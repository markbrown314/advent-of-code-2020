#!/usr/bin/python3

import sys
import math
import crt

"""
The earliest timestamp that matches the list 17,x,13,19 is 3417.
67,7,59,61 first occurs at timestamp 754018.
67,x,7,59,61 first occurs at timestamp 779210.
67,7,x,59,61 first occurs at timestamp 1261476.
1789,37,47,1889 first occurs at timestamp 1202161486.
"""

def main():
    #data_input = "1005162\n19,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,823,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,443,x,x,x,x,x,37,x,x,x,x,x,x,13"
    #data_input = "939\n7,13,x,x,59,x,31,19"
    data_input = "0\n17,x,13,19"
    #data_input = "0\n1789,37,47,1889"
    #data_input = "0\n3,5,x,11"
    #data_input = "0\n17,x,13"
    print_count = 20

    data = data_input.splitlines()
    timestamp = int(data[0])
    bus_ids = [int(x) for x in data[1].split(",") if x != "x"]
    times = [(math.ceil(timestamp/x)*x)-timestamp for x in bus_ids]
    min_time = min(times)
    index = times.index(min_time)
    min_time_bus_id  = bus_ids[index]
    print(min_time * min_time_bus_id)

    timestamp = 0
    time_inc = bus_ids[0]
    found = False
    while True:
        found = True
        for i,bus_id in enumerate(data[1].split(",")):
            if bus_id == "x":
                continue
            bus_id = int(bus_id)
            if not (timestamp+i)%bus_id == 0:
                found = False
                break
        if found == True:
            print("timestamp found:", timestamp)
            print_count -= 1
            if not print_count:
                break
        timestamp += time_inc

if __name__ == "__main__":
    main()
