#!/usr/bin/python3
"""
🎅 Advent of Code 2020 Day #3  Toboggan Trajectory Part 1 & 2
   by Mark F. Brown <mark.brown314@gmail.com>
"""

def parse_line(tree_map, pos_y, line):
    """ parse each file line and build tree map """
    pos_x = 0
    for item in line:
        if item == '#':
            tree_map[(pos_x, pos_y)] = True
        pos_x += 1

    if "max_x" in tree_map:
        assert pos_x - 1 == tree_map["max_x"]
    else:
        tree_map["max_x"] = pos_x - 1

def load_tree_map(file_path):
    """ load tree map file """
    tree_map = dict()
    pos_y = 0

    with open(file_path) as file_input:
        for line in file_input:
            parse_line(tree_map, pos_y, line)
            pos_y += 1
    tree_map["max_y"] = pos_y
    return tree_map

def toboggan_run(tree_map, move):
    """ execute toboggan run and return trees found """
    pos_x = 0
    pos_y = 0
    tree_count = 0

    while True:
        pos_x += move[0]
        pos_x = pos_x % tree_map["max_x"]
        pos_y += move[1]

        if pos_y >= tree_map["max_y"]:
            break

        if (pos_x, pos_y) in tree_map:
            tree_count += 1

    print("for move", move, "found", tree_count, "trees")
    return tree_count

def main():
    """ load puzzle data and execute toboggan run """
    moves = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    result = 1

    tree_map = load_tree_map('puzzle_input_1.txt')

    for move in moves:
        result *= toboggan_run(tree_map, move)

    print("result:", result)

if __name__ == "__main__":
    main()
