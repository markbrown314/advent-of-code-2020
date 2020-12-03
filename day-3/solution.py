#!/usr/bin/python3

def parse_line(tree_map, pos_y, line):
    pos_x = 0
    #print(line)
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
    pos_x_true = 0
    tree_count = 0

    #print(tree_map.keys())

    while True:
        pos_x += move[0]
        pos_x_true += move[0] 
        pos_x = pos_x % tree_map["max_x"]
        pos_y += move[1]
        #print("move:", pos_x_true, pos_y)
        #print("mod move", pos_x, pos_y)
        #print("")

        if pos_y >= tree_map["max_y"]:
            #print("end of walk")
            break

        if (pos_x, pos_y) in tree_map:
            #print("found tree at", pos_x, pos_y)
            tree_count += 1
            
    print("for move", move, "found", tree_count, "trees")
    return tree_count


def main():
    tree_map = dict()
    pos_y = 0
    moves = [(1,1), (3,1), (5,1), (7,1), (1,2)] 
    res = 1

    #with open('puzzle_input_1.txt') as file_input:
    with open('puzzle_test_1.txt') as file_input:
        for line in file_input:
            parse_line(tree_map, pos_y, line)
            pos_y += 1
    #print("max_x", tree_map["max_x"])
    tree_map["max_y"] = pos_y
    for move in moves:
        res *= toboggan_run(tree_map, move)
    print("result:", res);


if __name__ == "__main__":
    main()
