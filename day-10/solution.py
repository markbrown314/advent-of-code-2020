#!/usr/bin/python3
import sys

def main():
    filename = "puzzle_test_1.txt" if len(sys.argv) < 2 else sys.argv[1]
    file_input = [int(num) for num in open(filename).read().splitlines()]
    jolts = sorted(file_input)
    jolts.insert(0,0)
    dist = []
    for i in range(0, len(jolts)-1):
        dist.append(jolts[i+1]-jolts[i])
    
    print(jolts)
    print(dist)
    threes = len([*filter(lambda a: a == 3, dist)]) + 1
    ones = len([*filter(lambda b: b == 1, dist)])

    print("ones:", ones, "threes:", threes, ones * threes)

    paths = sorted(file_input, reverse = True)
    first_path = paths[0]
    paths.insert(0, first_path+3)
    paths.append(0)
    print(paths)
    path_dict = {path:0 for path in paths}
    path_dict[paths[0]] = 1
    print(paths)
    print(path_dict)
    for i in paths:
        total = path_dict[i]
        if i+1 in path_dict:
            total += path_dict[i+1]
        if i+2 in path_dict:
            total += path_dict[i+2]
        if i+3 in path_dict:
            total += path_dict[i+3]
        path_dict[i] = total

    print(path_dict)
    print("final count:", path_dict[0])

if __name__ == "__main__":
    main()