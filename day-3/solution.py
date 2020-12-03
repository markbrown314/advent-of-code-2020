#!/usr/bin/python3

def parse_line(tree_map, pos_y, line):
    pos_x = 0
    for item in line:
        if item == '#':
            tree_map[(pos_x, pos_y)] = True
        pos_x += 1

    if "max_x" in tree_map:
        assert(pos_x - 1 == tree_map["max_x"])
    else:
        tree_map["max_x"] = pos_x - 1

def toboggan_run(tree_map, move):
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
    tree_map = dict()
    pos_y = 0
    moves = [(1,1), (3,1), (5,1), (7,1), (1,2)] 
    res = 1

    with open('puzzle_input_1.txt') as file_input:
        for line in file_input:
            parse_line(tree_map, pos_y, line)
            pos_y += 1
    tree_map["max_y"] = pos_y
    for move in moves:
        res *= toboggan_run(tree_map, move)
    print("result:", res);


if __name__ == "__main__":
    main()
