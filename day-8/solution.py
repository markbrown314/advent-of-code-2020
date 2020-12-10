#!/usr/bin/python3
"""
🎅 Advent of Code Day 8 Handheld Halting
Mark F. Brown <mark.brown314@gmail.com>
"""
import sys
import copy

def list_program(program):
    line_no = 0
    for line in program:
        print(line_no, ": ", line[0], line[1], sep="")
        line_no += 1

def toggle_jmp_nop(program, line_no):
    if program[line_no][0] == "nop":
        program[line_no][0] = "jmp"
    else:
        program[line_no][0] = "nop"


def debug_program(program):
    change_points = []
    line_no = 0
    for line in program:
        if line[0] == "nop" or line[0] == "jmp":
            change_points.append(line_no)
        line_no += 1

    print(change_points)

    while True:
        test_program = copy.deepcopy(program)

        if not change_points:
            print("exhausted change points")
            return

        change_point = change_points.pop()
        toggle_jmp_nop(test_program, change_point)
        list_program(test_program)
        if exec_program(test_program):
            return

def exec_program(program):
    acc = 0
    line_no = 0
    lines = len(program)
    while True:
        if line_no >= lines:
            print("reached end of program acc", acc)
            return True

        if program[line_no][2]:
            print("loop detected at:", line_no, "acc", acc)
            return False
        if program[line_no][0] == "nop":
            program[line_no][2] = True 
            line_no += 1
            continue
        if program[line_no][0] == "jmp":
            program[line_no][2] = True 
            line_no += int(program[line_no][1])
            continue
        if program[line_no][0] == "acc":
            program[line_no][2] = True 
            acc += int(program[line_no][1])
            line_no += 1
            continue
    return False
def main():
    filename = "puzzle_test.txt" if len(sys.argv) < 2 else sys.argv[1]
    file_input = open(filename).read().splitlines()
    program = [data.split() + [False] for data in file_input]

    print ("first run:")

    list_program(program)
    test_program = copy.deepcopy(program)
    exec_program(test_program)

    print ("debug run:")

    debug_program(program)

if __name__ == "__main__":
    main()