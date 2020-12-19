#!/usr/bin/python3
import sys
import copy
"""
🎅 Advent of Code 2020 Day #11 Seating System Part 1
   by Mark F. Brown <mark.brown314@gmail.com>
"""
def adjacency_check(coord, input_set, match):
    for y in range(coord[1]-1, coord[1]+2):
        for x in range(coord[0]-1, coord[0]+2):
            if (x,y) == coord:
                continue
            if match and (x,y) in input_set:
                yield (x,y)
            elif not match and (x,y) not in input_set:
                yield (x,y)

def print_seats(state):
    print()
    for y in range(0, state["max_y"]):
        for x in range(0, state["max_x"]):
            if (x,y) in state["empty_seats"]:
                print('L', end = "")
            if (x,y) in state["floor"]:
                print('.', end = "")
            if (x,y) in state["occupied_seats"]:
                print('#', end = "")
        print()

def apply_rules(state):
    new_state = copy.deepcopy(state)
    changed = False
    new_state["occupied_seats"] = set()
    new_state["empty_seats"] = set()
    for y in range(0, state["max_y"]):
        for x in range(0, state["max_x"]):
            if (x,y) in state["floor"]:
                continue

            # occupied 
            if (x,y) in state["empty_seats"]:
                if not len([*adjacency_check((x,y), state["occupied_seats"], True)]):
                    changed = True
                    new_state["occupied_seats"].add((x,y))
                else:
                    new_state["empty_seats"].add((x,y))

            if (x,y) in state["occupied_seats"]:
                if len([*adjacency_check((x,y), state["occupied_seats"], True)]) >= 4:
                    changed = True
                    new_state["empty_seats"].add((x,y))
                else:
                    new_state["occupied_seats"].add((x,y))

    if changed:
        return(new_state)
    else:
        return None

def main():
    filename="puzzle_input.txt" if len(sys.argv) < 2 else sys.argv
    file_input = open(filename).read().splitlines()
    print(file_input)

    state = {'floor': set(), 'empty_seats': set(), 'occupied_seats': set()}

    # assume max x is constant for all lines
    state["max_x"] = len(file_input[0])
    state["max_y"] = len(file_input)

    for y in range(0, state["max_y"]):
        for x in range(0, state["max_x"]):
            if file_input[y][x] == '.':
                state["floor"].add((x,y))
            elif file_input[y][x] == 'L':
                state["empty_seats"].add((x,y)) 
    print("empty seats:", state["empty_seats"])
    print("floor:", state["floor"])
    print([*adjacency_check((0,0), state["empty_seats"], True)])
    print([*adjacency_check((0,0), state["floor"], True)])
    print([*adjacency_check((0,0), state["occupied_seats"], True)])

    while True:
        print_seats(state)
        new_state = apply_rules(state)
        if new_state:
            state = new_state
        else:
            print("finished")
            print_seats(state)
            print("part 1 # seats occupied:", len(state["occupied_seats"]))
            break

if __name__ == "__main__":
    main()